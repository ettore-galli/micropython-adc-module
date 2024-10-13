SAMPLE_LENGTH: int = 32
HALF_SAMPLE_LENGTH: int = 16

K_W_TERMS_32 = {
    0: {
        2: (1.0, -0.0),
        4: (1.0, -0.0),
        8: (1.0, -0.0),
        16: (1.0, -0.0),
        32: (1.0, -0.0),
    },
    1: {
        2: (-1.0, -1.2246467991473532e-16),
        4: (6.123233995736766e-17, -1.0),
        8: (0.7071067811865476, -0.7071067811865475),
        16: (0.9238795325112867, -0.3826834323650898),
        32: (0.9807852804032304, -0.19509032201612825),
    },
    2: {
        2: (1.0, 2.4492935982947064e-16),
        4: (-1.0, -1.2246467991473532e-16),
        8: (6.123233995736766e-17, -1.0),
        16: (0.7071067811865476, -0.7071067811865475),
        32: (0.9238795325112867, -0.3826834323650898),
    },
    3: {
        2: (-1.0, -3.6739403974420594e-16),
        4: (-1.8369701987210297e-16, 1.0),
        8: (-0.7071067811865475, -0.7071067811865476),
        16: (0.38268343236508984, -0.9238795325112867),
        32: (0.8314696123025452, -0.5555702330196022),
    },
    4: {
        2: (1.0, 4.898587196589413e-16),
        4: (1.0, 2.4492935982947064e-16),
        8: (-1.0, -1.2246467991473532e-16),
        16: (6.123233995736766e-17, -1.0),
        32: (0.7071067811865476, -0.7071067811865475),
    },
    5: {
        2: (-1.0, -6.123233995736766e-16),
        4: (3.061616997868383e-16, -1.0),
        8: (-0.7071067811865477, 0.7071067811865475),
        16: (-0.3826834323650897, -0.9238795325112867),
        32: (0.5555702330196023, -0.8314696123025452),
    },
    6: {
        2: (1.0, 7.347880794884119e-16),
        4: (-1.0, -3.6739403974420594e-16),
        8: (-1.8369701987210297e-16, 1.0),
        16: (-0.7071067811865475, -0.7071067811865476),
        32: (0.38268343236508984, -0.9238795325112867),
    },
    7: {
        2: (-1.0, -8.572527594031472e-16),
        4: (-4.286263797015736e-16, 1.0),
        8: (0.7071067811865474, 0.7071067811865477),
        16: (-0.9238795325112867, -0.3826834323650899),
        32: (0.19509032201612833, -0.9807852804032304),
    },
    8: {
        2: (1.0, 9.797174393178826e-16),
        4: (1.0, 4.898587196589413e-16),
        8: (1.0, 2.4492935982947064e-16),
        16: (-1.0, -1.2246467991473532e-16),
        32: (6.123233995736766e-17, -1.0),
    },
    9: {
        2: (-1.0, -1.102182119232618e-15),
        4: (5.51091059616309e-16, -1.0),
        8: (0.7071067811865477, -0.7071067811865474),
        16: (-0.9238795325112868, 0.38268343236508967),
        32: (-0.1950903220161282, -0.9807852804032304),
    },
    10: {
        2: (1.0, 1.2246467991473533e-15),
        4: (-1.0, -6.123233995736766e-16),
        8: (3.061616997868383e-16, -1.0),
        16: (-0.7071067811865477, 0.7071067811865475),
        32: (-0.3826834323650897, -0.9238795325112867),
    },
    11: {
        2: (-1.0, -4.899825157862589e-15),
        4: (-2.4499125789312946e-15, 1.0),
        8: (-0.7071067811865467, -0.7071067811865485),
        16: (-0.38268343236509034, 0.9238795325112865),
        32: (-0.555570233019602, -0.8314696123025453),
    },
    12: {
        2: (1.0, 1.4695761589768238e-15),
        4: (1.0, 7.347880794884119e-16),
        8: (-1.0, -3.6739403974420594e-16),
        16: (-1.8369701987210297e-16, 1.0),
        32: (-0.7071067811865475, -0.7071067811865476),
    },
    13: {
        2: (-1.0, 1.9606728399089416e-15),
        4: (-9.803364199544708e-16, -1.0),
        8: (-0.7071067811865472, 0.7071067811865479),
        16: (0.38268343236509, 0.9238795325112866),
        32: (-0.8314696123025453, -0.5555702330196022),
    },
    14: {
        2: (1.0, 1.7145055188062944e-15),
        4: (-1.0, -8.572527594031472e-16),
        8: (-4.286263797015736e-16, 1.0),
        16: (0.7071067811865474, 0.7071067811865477),
        32: (-0.9238795325112867, -0.3826834323650899),
    },
    15: {
        2: (-1.0, -5.3896838775215305e-15),
        4: (-2.6948419387607653e-15, 1.0),
        8: (0.7071067811865466, 0.7071067811865485),
        16: (0.9238795325112865, 0.3826834323650904),
        32: (-0.9807852804032304, -0.1950903220161286),
    },
    16: {
        2: (1.0, 1.959434878635765e-15),
        4: (1.0, 9.797174393178826e-16),
        8: (1.0, 4.898587196589413e-16),
        16: (1.0, 2.4492935982947064e-16),
        32: (-1.0, -1.2246467991473532e-16),
    },
    17: {
        2: (-1.0, 1.4708141202500005e-15),
        4: (-7.354070601250002e-16, -1.0),
        8: (0.7071067811865472, -0.7071067811865478),
        16: (0.9238795325112866, -0.38268343236508995),
        32: (-0.9807852804032304, 0.19509032201612836),
    },
    18: {
        2: (1.0, 2.204364238465236e-15),
        4: (-1.0, -1.102182119232618e-15),
        8: (5.51091059616309e-16, -1.0),
        16: (0.7071067811865477, -0.7071067811865474),
        32: (-0.9238795325112868, 0.38268343236508967),
    },
    19: {
        2: (-1.0, -5.879542597180472e-15),
        4: (-2.939771298590236e-15, 1.0),
        8: (-0.7071067811865465, -0.7071067811865486),
        16: (0.38268343236509045, -0.9238795325112865),
        32: (-0.8314696123025455, 0.555570233019602),
    },
    20: {
        2: (1.0, 2.4492935982947065e-15),
        4: (1.0, 1.2246467991473533e-15),
        8: (-1.0, -6.123233995736766e-16),
        16: (3.061616997868383e-16, -1.0),
        32: (-0.7071067811865477, 0.7071067811865475),
    },
    21: {
        2: (-1.0, 9.809554005910593e-16),
        4: (-4.904777002955296e-16, -1.0),
        8: (-0.7071067811865474, 0.7071067811865477),
        16: (-0.3826834323650899, -0.9238795325112867),
        32: (-0.5555702330196022, 0.8314696123025452),
    },
    22: {
        2: (1.0, 9.799650315725178e-15),
        4: (-1.0, -4.899825157862589e-15),
        8: (-2.4499125789312946e-15, 1.0),
        16: (-0.7071067811865467, -0.7071067811865485),
        32: (-0.38268343236509034, 0.9238795325112865),
    },
    23: {
        2: (-1.0, -6.369401316839413e-15),
        4: (-3.1847006584197066e-15, 1.0),
        8: (0.7071067811865465, 0.7071067811865487),
        16: (-0.9238795325112864, -0.3826834323650905),
        32: (-0.19509032201612866, 0.9807852804032303),
    },
    24: {
        2: (1.0, 2.9391523179536475e-15),
        4: (1.0, 1.4695761589768238e-15),
        8: (1.0, 7.347880794884119e-16),
        16: (-1.0, -3.6739403974420594e-16),
        32: (-1.8369701987210297e-16, 1.0),
    },
    25: {
        2: (-1.0, 4.91096680932118e-16),
        4: (-2.45548340466059e-16, -1.0),
        8: (0.7071067811865475, -0.7071067811865477),
        16: (-0.9238795325112867, 0.38268343236508984),
        32: (0.1950903220161283, 0.9807852804032304),
    },
    26: {
        2: (1.0, -3.921345679817883e-15),
        4: (-1.0, 1.9606728399089416e-15),
        8: (-9.803364199544708e-16, -1.0),
        16: (-0.7071067811865472, 0.7071067811865479),
        32: (0.38268343236509, 0.9238795325112866),
    },
    27: {
        2: (-1.0, -6.859260036498355e-15),
        4: (-3.4296300182491773e-15, 1.0),
        8: (-0.7071067811865464, -0.7071067811865488),
        16: (-0.38268343236509056, 0.9238795325112864),
        32: (0.5555702330196018, 0.8314696123025455),
    },
    28: {
        2: (1.0, 3.429011037612589e-15),
        4: (1.0, 1.7145055188062944e-15),
        8: (-1.0, -8.572527594031472e-16),
        16: (-4.286263797015736e-16, 1.0),
        32: (0.7071067811865474, 0.7071067811865477),
    },
    29: {
        2: (-1.0, 1.2379612731767154e-18),
        4: (-6.189806365883577e-19, -1.0),
        8: (-0.7071067811865476, 0.7071067811865476),
        16: (0.3826834323650898, 0.9238795325112867),
        32: (0.8314696123025452, 0.5555702330196022),
    },
    30: {
        2: (1.0, 1.0779367755043061e-14),
        4: (-1.0, -5.3896838775215305e-15),
        8: (-2.6948419387607653e-15, 1.0),
        16: (0.7071067811865466, 0.7071067811865485),
        32: (0.9238795325112865, 0.3826834323650904),
    },
    31: {
        2: (-1.0, -7.349118756157295e-15),
        4: (-3.674559378078648e-15, 1.0),
        8: (0.7071067811865462, 0.7071067811865488),
        16: (0.9238795325112864, 0.3826834323650906),
        32: (0.9807852804032303, 0.19509032201612872),
    },
}


def preorder_samples_32(samples: list[float]) -> list[float]:
    order = [
        0,
        16,
        8,
        24,
        4,
        20,
        12,
        28,
        2,
        18,
        10,
        26,
        6,
        22,
        14,
        30,
        1,
        17,
        9,
        25,
        5,
        21,
        13,
        29,
        3,
        19,
        11,
        27,
        7,
        23,
        15,
        31,
    ]

    return [samples[index] for index in order]


def fft_term_32(
    initial_fft_term: list[tuple[float, float]],
    w_terms: dict[int, tuple[float, float]],
) -> tuple[float, float]:

    fft_term: list[tuple[float, float]] = list(initial_fft_term)

    size = 1

    while size < SAMPLE_LENGTH:
        size = size << 1

        w_k_term_r, w_k_term_i = w_terms[size]

        step: int = size // 2

        for index in range(0, SAMPLE_LENGTH, size):
            fft_term[index] = (
                (
                    fft_term[index][0]
                    + w_k_term_r * fft_term[index + step][0]
                    - w_k_term_i * fft_term[index + step][1]
                ),
                (
                    fft_term[index][1]
                    + w_k_term_i * fft_term[index + step][0]
                    + w_k_term_r * fft_term[index + step][1]
                ),
            )

    return fft_term[0]


def fft32(
    samples: list[float], *, compute_half_range: bool = True
) -> list[tuple[float, float]]:

    reordered_samples = preorder_samples_32(samples=samples)

    initial_fft_term: list[tuple[float, float]] = [
        (sample, 0.0) for sample in reordered_samples
    ]

    return [
        fft_term_32(
            initial_fft_term=initial_fft_term,
            w_terms=K_W_TERMS_32[k_index],
        )
        for k_index in (
            range(HALF_SAMPLE_LENGTH) if compute_half_range else range(SAMPLE_LENGTH)
        )
    ]


def fft32_power(samples: list[float]) -> list[float]:
    return [
        (point[0] ** 2 + point[1] ** 2) ** 0.5
        for point in fft32(samples, compute_half_range=True)
    ]
