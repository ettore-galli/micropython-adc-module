from collections.abc import Callable
from math import cos, sin

from adc_module.base import BaseADC


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
    def perform_mod_dft(samples: list[float]) -> list[float]:
        # https://www.audiolabs-erlangen.de/resources/MIR/PCP/PCP_09_dft.html#exercise_freq_index
        n_samples: int = int(len(samples))
        index_range = range(n_samples)
        half_range = range(n_samples // 2)

        def dft_term(samples: list[float], freq_index: float) -> float:
            return (
                (
                    sum(
                        samples[index] * cos(6.28 * index * freq_index / n_samples)
                        for index in index_range
                    )
                    ** 2
                )
                + (
                    sum(
                        samples[index] * sin(6.28 * index * freq_index / n_samples)
                        for index in index_range
                    )
                    ** 2
                )
            ) ** 0.5

        return [dft_term(samples, index) for index in half_range]

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
            dft = self.perform_mod_dft(samples=self.samples)
            self.plot_dft(
                values=dft, fsample=1000 / self.parameter_configuration.adc_delay_ms
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
