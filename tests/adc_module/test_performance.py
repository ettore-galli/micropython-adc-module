from datetime import UTC, datetime
from math import sin

from adc_module.dft import dft
from adc_module.fft import fft_power


def test_performance() -> None:
    domain = range(1024)
    samples = [
        (
            sin(3 * 6.28 * index / len(domain))
            + sin(3 * 6.28 * 2 * index / len(domain))
            + sin(3 * 6.28 * 3 * index / len(domain))
        )
        for index in domain
    ]

    number_of_test_iterations = 10

    t0d = datetime.now(tz=UTC)
    for _ in range(number_of_test_iterations):
        _ = dft(samples)
    t1d = datetime.now(tz=UTC)
    time_dft = t1d - t0d

    t0f = datetime.now(tz=UTC)
    for _ in range(number_of_test_iterations):
        _ = fft_power(samples)
    t1f = datetime.now(tz=UTC)
    time_fft = t1f - t0f

    assert time_dft.microseconds > 0
    assert time_fft.microseconds > 0
