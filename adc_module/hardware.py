import utime  # type: ignore[import-not-found]
from machine import ADC  # type: ignore[import-not-found]

from adc_module.base import BaseADC


def sleep_ms(ms: float) -> None:
    utime.sleep_ms(ms)


class MachineADC(BaseADC):
    def __init__(self, pin: int) -> None:
        self.adc = ADC(pin)

    def read_u16(self) -> int:
        return self.adc.read_u16()
