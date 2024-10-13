import profile
from math import sin

from adc_module.dft import dft
from adc_module.fft import fft


def profile_fft(data_size: int, number_of_runs: int) -> None:
    domain = range(data_size)
    samples = [
        (
            sin(3 * 6.28 * index / len(domain))
            + sin(3 * 6.28 * 2 * index / len(domain))
            + sin(3 * 6.28 * 3 * index / len(domain))
        )
        for index in domain
    ]
    for _ in range(number_of_runs):
        fft(samples)


def profile_dft(data_size: int, number_of_runs: int) -> None:
    domain = range(data_size)
    samples = [
        (
            sin(3 * 6.28 * index / len(domain))
            + sin(3 * 6.28 * 2 * index / len(domain))
            + sin(3 * 6.28 * 3 * index / len(domain))
        )
        for index in domain
    ]

    for _ in range(number_of_runs):
        dft(samples)


if __name__ == "__main__":
    number_of_runs: int = 100
    data_size: int = 2**7
    profile.run("profile_fft(data_size, number_of_runs)")
    profile.run("profile_dft(data_size, number_of_runs)")