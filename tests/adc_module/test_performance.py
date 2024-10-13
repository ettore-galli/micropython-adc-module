from datetime import UTC, datetime
from math import sin

from adc_module.dft import DftCalculator, dft
from adc_module.fft import arrange_samples, fft, preorder_samples
from adc_module.fft32 import fft32, preorder_samples_32


def test_performance() -> None:
    domain = range(32)
    samples = [
        (
            sin(3 * 6.28 * index / len(domain))
            + sin(3 * 6.28 * 2 * index / len(domain))
            + sin(3 * 6.28 * 3 * index / len(domain))
        )
        for index in domain
    ]

    dft_calculator = DftCalculator(data_length=len(samples))

    number_of_test_iterations = 100

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
        _ = fft(samples)
    t1f = datetime.now(tz=UTC)
    time_fft = t1f - t0f

    t0f32 = datetime.now(tz=UTC)
    for _ in range(number_of_test_iterations):
        _ = fft32(samples)
    t1f32 = datetime.now(tz=UTC)
    time_fft32 = t1f32 - t0f32

    assert time_dft.microseconds > 0
    assert time_fft.microseconds > 0

    print(  # noqa: T201
        f"\nDFT/standard : {time_dft.microseconds} "
        f"\nDFT/precalc  : {time_dft_ptf.microseconds}"
        f"\nFFT/standard : {time_fft.microseconds}"
        f"\nFFT/fft32    : {time_fft32.microseconds}"
    )


def test_performance_preorder() -> None:
    samples = [float(sample) for sample in list(range(32))]
    number_of_test_iterations = 1000

    t0_arrange = datetime.now(tz=UTC)
    for _ in range(number_of_test_iterations):
        _ = arrange_samples(samples)
    t1_arrange = datetime.now(tz=UTC)
    time_arrange = t1_arrange - t0_arrange

    t0_preorder = datetime.now(tz=UTC)
    for _ in range(number_of_test_iterations):
        _ = preorder_samples(samples)
    t1_preorder = datetime.now(tz=UTC)
    time_preorder = t1_preorder - t0_preorder

    t0_preorder_32 = datetime.now(tz=UTC)
    for _ in range(number_of_test_iterations):
        _ = preorder_samples_32(samples)
    t1_preorder_32 = datetime.now(tz=UTC)
    time_preorder_32 = t1_preorder_32 - t0_preorder_32
    print(  # noqa: T201
        f"\narrange  : {time_arrange.microseconds} "
        f"\npreorder : {time_preorder.microseconds}"
        f"\npreorder_32 : {time_preorder_32.microseconds}"
    )
