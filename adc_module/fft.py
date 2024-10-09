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


def fft_term(
    initial_fft_term: list[tuple[float, float]], k_index: int
) -> tuple[float, float]:

    fft_term: list[tuple[float, float]] = initial_fft_term

    size = 1

    while len(fft_term) > 1:
        size = size << 1

        w_k_term = (cos(-2.0 * pi * k_index / size), sin(-2.0 * pi * k_index / size))

        fft_term = [
            twiddle(fft_term[index], w_k_term, fft_term[index + 1])
            for index in range(0, len(fft_term), 2)
        ]

    return fft_term[0]


def twiddle(
    a: tuple[float, float], w: tuple[float, float], b: tuple[float, float]
) -> tuple[float, float]:
    ar, ai = a
    wr, wi = w
    br, bi = b
    return (ar + wr * br - wi * bi, ai + wi * br + wr * bi)


def fft(
    samples: list[float], *, compute_half_range: bool = True
) -> list[tuple[float, float]]:

    reordered_samples = arrange_samples(samples=samples)

    initial_fft_term: list[tuple[float, float]] = [
        (sample, 0.0) for sample in reordered_samples
    ]
    n_samples: int = int(len(samples))

    return [
        fft_term(initial_fft_term=initial_fft_term, k_index=index)
        for index in (
            range(n_samples // 2) if compute_half_range else range(len(samples))
        )
    ]


def fft_power(samples: list[float]) -> list[float]:
    return [
        (point[0] ** 2 + point[1] ** 2) ** 0.5
        for point in fft(samples, compute_half_range=True)
    ]
