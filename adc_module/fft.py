from math import cos, sin


def dft(samples: list[float]) -> list[float]:
    # https://www.audiolabs-erlangen.de/resources/MIR/PCP/PCP_09_dft.html#exercise_freq_index
    n_samples: int = int(len(samples))
    index_range = range(n_samples)
    half_range = range(n_samples // 2)

    def dft_term(samples: list[float], freq_index: float) -> float:
        return (
            (
                sum(
                    samples[index] * cos(6.28 * index * freq_index / n_samples)
                    for index in index_range
                )
                ** 2
            )
            + (
                sum(
                    samples[index] * sin(6.28 * index * freq_index / n_samples)
                    for index in index_range
                )
                ** 2
            )
        ) ** 0.5

    return [dft_term(samples, index) for index in half_range]


def arrange_samples(samples: list[float]) -> list[float]:
    if len(samples) == 1:
        return samples

    return arrange_samples(samples[0 : len(samples) : 2]) + arrange_samples(
        samples[1 : len(samples) : 2]
    )


def calculate_w_k_term(size: int, k_index: int) -> tuple[float, float]:
    return (cos(-6.28 * k_index / size), sin(-6.28 * k_index / size))


def complex_mult(
    alfa: tuple[float, float], beta: tuple[float, float]
) -> tuple[float, float]:
    return alfa[0] * beta[0] - alfa[1] * beta[1], alfa[1] * beta[0] + alfa[0] * beta[1]


def complex_sum(
    alfa: tuple[float, float], beta: tuple[float, float]
) -> tuple[float, float]:
    return alfa[0] + beta[0], alfa[1] + beta[1]


def complex_mod(term: tuple[float, float]) -> float:
    return (term[0] ** 2 + term[1] ** 2) ** 0.5


def fft_term(reordered_samples: list[float], freq_index: int) -> tuple[float, float]:
    size = 1
    fft_term: list[tuple[float, float]] = [
        (sample, 0.0) for sample in reordered_samples
    ]
    while len(fft_term) > 1:
        size = size << 1
        w_k_term = calculate_w_k_term(size=size, k_index=freq_index)

        fft_term = [
            complex_sum(fft_term[index], complex_mult(w_k_term, fft_term[index + 1]))
            for index in range(0, len(fft_term), 2)
        ]
    return fft_term[0]


def fft(
    samples: list[float], *, compute_half_range: bool = True
) -> list[tuple[float, float]]:
    reordered_samples = arrange_samples(samples=samples)
    n_samples: int = int(len(samples))
    half_range = range(n_samples // 2)

    return [
        fft_term(reordered_samples=reordered_samples, freq_index=index)
        for index in (half_range if compute_half_range else range(len(samples)))
    ]


def fft_power(samples: list[float]) -> list[float]:
    return [complex_mod(point) for point in fft(samples, compute_half_range=True)]
