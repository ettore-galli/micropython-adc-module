import ssd1306  # type: ignore[import-not-found]
from machine import I2C, Pin  # type: ignore[import-not-found]

from adc_module.base import BaseDisplay


class Display(BaseDisplay):
    def __init__(self, sda_pin: int, scl_pin: int) -> None:
        i2c = I2C(sda=Pin(sda_pin), scl=Pin(scl_pin))
        self.display: ssd1306.SSD1306_I2C = ssd1306.SSD1306_I2C(128, 64, i2c)

    def clear(self) -> None:
        self.display.fill(0)

    def text(self, text: str, x: int, y: int, color: int) -> None:
        self.display.text(text, x, y, color)

    def show(self) -> None:
        self.display.show()

    def show_value(self, value: int) -> None:
        self.clear()
        self.text(f"v: {value}", 10, 1, 1)
        self.show()

    def plot_dft(self, values: list[int]) -> None:
        self.clear()
        span = 64 // len(values)
        for index, value in enumerate(values):
            y_coord = span * index
            self.hline(1, y_coord, value, 1)
        self.show()

    def hline(self, x: int, y: int, width: int, color: int) -> None:
        self.display.hline(x, y, width, color)
