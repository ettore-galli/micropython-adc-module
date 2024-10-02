from collections.abc import Callable

from adc_module.base import BaseADC
from adc_module.fft import dft


class HardwareInformation:
    adc_pin: int = 0


class ParameterConfiguration:
    adc_delay_ms: int = 2
    dft_chunk_size: int = 32


class GhostDetector:
    def __init__(
        self,
        adc_class: type[BaseADC],
        sleep_ms: Callable[[float], None],
        hardware_information: HardwareInformation | None = None,
        parameter_configuration: ParameterConfiguration | None = None,
    ) -> None:

        self.hardware_information = (
            hardware_information
            if hardware_information is not None
            else HardwareInformation()
        )

        self.parameter_configuration = (
            parameter_configuration
            if parameter_configuration is not None
            else ParameterConfiguration()
        )

        self.adc_class: type[BaseADC] = adc_class
        self.sleep_ms = sleep_ms

        self.adc = self.adc_class(self.hardware_information.adc_pin)

        self.samples: list[float] = []

    def read_adc_values_loop(
        self,
        sample_value_reader: Callable[[], int],
        sample_value_consumer: Callable[[int], None],
    ) -> None:

        while True:
            raw_adc_value = sample_value_reader()
            sample_value_consumer(raw_adc_value)
            self.sleep_ms(self.parameter_configuration.adc_delay_ms)

    @staticmethod
    def normalize(values: list[float], top: int) -> list[int]:
        bottom = min(*values)
        peaks = max(*values) - min(*values)
        return [int((point - bottom) * top / peaks) for point in values]

    def plot_dft(self, values: list[float], fsample: float) -> None:
        print("\n")  # noqa: T201
        funit = fsample / len(values)
        for index, point in enumerate(self.normalize(values, 64)):
            freq = funit * index
            dsp_freq = (" " * 7 + str(freq))[-7:]
            print(  # noqa: T201
                dsp_freq, ("-" * (point - 1) if point > 1 else "") + "*"
            )

    def send_to_dft(self, raw_adc_value: int) -> None:
        self.samples.append(raw_adc_value)

        if len(self.samples) == self.parameter_configuration.dft_chunk_size:
            dft_data = dft(samples=self.samples)
            self.plot_dft(
                values=dft_data,
                fsample=1000 / self.parameter_configuration.adc_delay_ms,
            )
            self.samples = []

    def notify_value(self, value: int) -> None:
        stars = int(value / 1024)
        lines = 64 - stars
        print("#" * stars + ":" * lines)  # noqa: T201

    def main(self) -> None:
        self.read_adc_values_loop(
            sample_value_reader=self.adc.read_u16,
            sample_value_consumer=self.send_to_dft,
        )
