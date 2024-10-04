from math import sin

from adc_module.fft import arrange_samples, fft


def test_arrange_samples() -> None:
    assert arrange_samples([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 5, 3, 7, 2, 6, 4, 8]
    assert arrange_samples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == [
        1,
        9,
        5,
        13,
        3,
        11,
        7,
        15,
        2,
        10,
        6,
        14,
        4,
        12,
        8,
        16,
    ]


def test_fft() -> None:
    domain = range(32)
    samples = [
        (
            sin(3 * 6.28 * index / len(domain))
            + sin(3 * 6.28 * 2 * index / len(domain))
            + sin(3 * 6.28 * 3 * index / len(domain))
        )
        for index in domain
    ]

    calc_dft = fft(samples)

    assert len(calc_dft) == len(domain) / 2

    exoected_dft = [
        0.029046,
        0.029118,
        0.029334,
        16.001723,
        0.030225,
        0.03092,
        15.994754,
        0.032898,
        0.034234,
        15.986482,
        0.037805,
        0.040164,
        0.043023,
        0.046517,
        0.05083,
        0.056236,
    ]
    assert [round(point, 6) for point in calc_dft] == exoected_dft
