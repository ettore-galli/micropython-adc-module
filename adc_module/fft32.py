from math import cos, pi, sin


def arrange_samples(samples: list[float]) -> list[float]:
    size: int = len(samples)
    arranged: list[float] = samples

    while size > 1:

        arranged_buffer: list[float] = []

        for start in range(0, len(samples), size):
            buffer: list[float] = arranged[start : start + size]
            buffer = buffer[0 : len(buffer) : 2] + buffer[1 : len(buffer) : 2]
            arranged_buffer += buffer

        arranged = arranged_buffer

        size = size >> 1

    return arranged


def preorder_samples(samples: list[float]) -> list[float]:
    size: int = len(samples)
    arranged: list[float] = samples

    while size > 1:

        for start in range(0, len(samples), size):
            for chunk_index in range(size // 2):
                for swap_delta in range(chunk_index):
                    (
                        arranged[start + chunk_index],
                        arranged[start + chunk_index + swap_delta + 1],
                    ) = (
                        arranged[start + chunk_index + swap_delta + 1],
                        arranged[start + chunk_index],
                    )

        size = size >> 1

    return arranged


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


def fft_term(
    initial_fft_term: list[tuple[float, float]],
    k_index: int,
) -> tuple[float, float]:

    fft_term: list[tuple[float, float]] = initial_fft_term

    size = 1

    while len(fft_term) > 1:
        size = size << 1

        w_k_term = (cos(-2.0 * pi * k_index / size), sin(-2.0 * pi * k_index / size))

        fft_term = [
            (
                (
                    fft_term[index][0]
                    + w_k_term[0] * fft_term[index + 1][0]
                    - w_k_term[1] * fft_term[index + 1][1]
                ),
                (
                    fft_term[index][1]
                    + w_k_term[1] * fft_term[index + 1][0]
                    + w_k_term[0] * fft_term[index + 1][1]
                ),
            )
            for index in range(0, len(fft_term), 2)
        ]

    return fft_term[0]


def twiddle(
    a: tuple[float, float], w: tuple[float, float], b: tuple[float, float]
) -> tuple[float, float]:
    "For reference only, not actually used for performance"
    ar, ai = a
    wr, wi = w
    br, bi = b
    return (ar + wr * br - wi * bi, ai + wi * br + wr * bi)


def fft32(
    samples: list[float], *, compute_half_range: bool = True
) -> list[tuple[float, float]]:

    reordered_samples = arrange_samples(samples=samples)

    initial_fft_term: list[tuple[float, float]] = [
        (sample, 0.0) for sample in reordered_samples
    ]

    return [
        fft_term(
            initial_fft_term=initial_fft_term,
            k_index=index,
        )
        for index in (
            range(len(samples) // 2) if compute_half_range else range(len(samples))
        )
    ]


def fft32_power(samples: list[float]) -> list[float]:
    return [
        (point[0] ** 2 + point[1] ** 2) ** 0.5
        for point in fft32(samples, compute_half_range=True)
    ]
