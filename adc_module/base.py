from abc import ABC, abstractmethod


class BaseADC(ABC):
    @abstractmethod
    def __init__(self, pin: int) -> None: ...

    @abstractmethod
    def read_u16(self) -> int: ...


class BaseDisplay(ABC):
    @abstractmethod
    def __init__(self, sda_pin: int, scl_pin: int) -> None: ...

    @abstractmethod
    def clear(self) -> None: ...

    @abstractmethod
    def text(self, text: str, x: int, y: int, color: int) -> None: ...

    @abstractmethod
    def show_value(self, value: int) -> None: ...

    @abstractmethod
    def hline(self, x: int, y: int, width: int, color: int) -> None: ...

    @abstractmethod
    def plot_dft(self, values: list[int]) -> None: ...
