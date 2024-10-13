from adc_module.fft import arrange_samples, fft, fft_power, preorder_samples

EXAMPLE_SAMPLES = [
    0.0,
    2.46,
    1.25,
    -0.23,
    0.41,
    0.37,
    -0.6,
    -0.11,
    0.0,
    -1.94,
    -2.02,
    1.12,
    2.42,
    0.54,
    -0.17,
    0.61,
    0.01,
    -0.62,
    0.16,
    -0.51,
    -2.41,
    -1.17,
    1.99,
    1.97,
    0.01,
    0.09,
    0.6,
    -0.35,
    -0.43,
    0.24,
    -1.21,
    -2.47,
]

# Expected result generated by:
# https://scistatcalc.blogspot.com/2013/12/fft-calculator.html
EXPECTED_DFT = [
    (0.010000, 0.000000),
    (0.038967, 0.003318),
    (0.041498, 0.049306),
    (-0.034344, -15.976670),
    (0.015858, -0.008284),
    (0.011494, 0.058204),
    (-0.118578, -15.978237),
    (0.029466, -0.035880),
    (0.010000, 0.060000),
    (-0.207241, -16.031065),
    (0.033726, -0.078641),
    (0.028097, -0.057099),
    (0.044142, -0.048284),
    (0.039606, -0.014791),
    (0.043355, -0.011099),
    (0.013955, 0.005316),
    (0.010000, 0.000000),
    (0.013955, -0.005316),
    (0.043355, 0.011099),
    (0.039606, 0.014791),
    (0.044142, 0.048284),
    (0.028097, 0.057099),
    (0.033726, 0.078641),
    (-0.207241, 16.031065),
    (0.010000, -0.060000),
    (0.029466, 0.035880),
    (-0.118578, 15.978237),
    (0.011494, -0.058204),
    (0.015858, 0.008284),
    (-0.034344, 15.976670),
    (0.041498, -0.049306),
    (0.038967, -0.003318),
]


def complex_mod(term: tuple[float, float]) -> float:
    return (term[0] ** 2 + term[1] ** 2) ** 0.5


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


def test_preorder_samples() -> None:
    assert preorder_samples([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 5, 3, 7, 2, 6, 4, 8]
    assert preorder_samples(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    ) == [
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
    samples = EXAMPLE_SAMPLES

    calc_fft = fft(samples, compute_half_range=False)

    assert len(calc_fft) == len(domain)

    expected_fft = EXPECTED_DFT
    assert [(round(real, 6), round(imag, 6)) for real, imag in calc_fft] == expected_fft


def test_fft_power() -> None:
    domain = range(32)
    samples = EXAMPLE_SAMPLES

    calc_fft_power = fft_power(samples)

    assert len(calc_fft_power) == len(domain) / 2

    assert [round(value, 4) for value in calc_fft_power] == [
        round(complex_mod(value), 4) for value in EXPECTED_DFT[: len(calc_fft_power)]
    ]
