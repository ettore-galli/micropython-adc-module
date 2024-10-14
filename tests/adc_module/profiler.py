import profile
from math import sin

from adc_module.dft import dft
from adc_module.fft import fft
from adc_module.fft32 import fft32, fft32_power, fft_term_32


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


def profile_fft32(data_size: int, number_of_runs: int) -> None:
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
        fft32(samples)


def profile_fft32_power(data_size: int, number_of_runs: int) -> None:
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
        fft32_power(samples)


def profile_fft_term_32(data_size: int, number_of_runs: int) -> None:
    domain = range(data_size)
    samples = [
        (
            sin(3 * 6.28 * index / len(domain))
            + sin(3 * 6.28 * 2 * index / len(domain))
            + sin(3 * 6.28 * 3 * index / len(domain)),
            0.0,
        )
        for index in domain
    ]

    for _ in range(number_of_runs):
        fft_term_32(
            fft_term=samples,
            w_terms={
                2: (1.0, 1.7145055188062944e-15),
                4: (-1.0, -8.572527594031472e-16),
                8: (-4.286263797015736e-16, 1.0),
                16: (0.7071067811865474, 0.7071067811865477),
                32: (-0.9238795325112867, -0.3826834323650899),
            },
        )


if __name__ == "__main__":
    number_of_runs: int = 10
    data_size: int = 32
    # Not necessary: profile.run("profile_fft(data_size, number_of_runs)")
    # Not necessary: profile.run("profile_dft(data_size, number_of_runs)")
    # Not necessary: profile.run("profile_fft32(data_size, number_of_runs)")
    profile.run("profile_fft32_power(data_size, number_of_runs)")
    # Not necessary: profile.run("profile_fft_term_32(data_size, number_of_runs)")
