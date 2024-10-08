from datetime import UTC, datetime
from math import sin

from adc_module.dft import DftCalculator, dft
from adc_module.fft import fft_power


def test_performance() -> None:
    domain = range(256)
    samples = [
        (
            sin(3 * 6.28 * index / len(domain))
            + sin(3 * 6.28 * 2 * index / len(domain))
            + sin(3 * 6.28 * 3 * index / len(domain))
        )
        for index in domain
    ]

    dft_calculator = DftCalculator(data_length=len(samples))

    number_of_test_iterations = 5

    t0d = datetime.now(tz=UTC)
    for _ in range(number_of_test_iterations):
        _ = dft(samples)
    t1d = datetime.now(tz=UTC)
    time_dft = t1d - t0d

    t0dp = datetime.now(tz=UTC)
    for _ in range(number_of_test_iterations):
        _ = dft_calculator.dft(samples)
    t1dp = datetime.now(tz=UTC)
    time_dft_ptf = t1dp - t0dp

    t0f = datetime.now(tz=UTC)
    for _ in range(number_of_test_iterations):
        _ = fft_power(samples)
    t1f = datetime.now(tz=UTC)
    time_fft = t1f - t0f

    assert time_dft.microseconds > 0
    assert time_fft.microseconds > 0

    print(  # noqa: T201
        f"\nDFT/standard : {time_dft.microseconds} "
        f"\nDFT/precalc  : {time_dft_ptf.microseconds}"
        f"\nFFT/standard : {time_fft.microseconds}"
    )
