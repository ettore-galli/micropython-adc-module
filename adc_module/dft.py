from math import cos, pi, sin


def dft(
    samples: list[float], *, compute_half_range: bool = True
) -> list[tuple[float, float]]:
    """
    Reference:
    https://scistatcalc.blogspot.com/2013/12/fft-calculator.html
    https://www.audiolabs-erlangen.de/resources/MIR/PCP/PCP_09_dft.html#exercise_k_index
    https://en.wikipedia.org/wiki/Discrete_Fourier_transform
    """

    n_samples: int = int(len(samples))
    index_range = range(n_samples)
    half_range = range(n_samples // 2)

    def dft_term(samples: list[float], k_index: float) -> tuple[float, float]:
        return (
            sum(
                samples[index] * cos(-2.0 * pi * index * k_index / n_samples)
                for index in index_range
            ),
            sum(
                samples[index] * sin(-2.0 * pi * index * k_index / n_samples)
                for index in index_range
            ),
        )

    return [
        dft_term(samples=samples, k_index=index)
        for index in (half_range if compute_half_range else index_range)
    ]


def complex_mod(term: tuple[float, float]) -> float:
    return (term[0] ** 2 + term[1] ** 2) ** 0.5


def dft_power(samples: list[float]) -> list[float]:
    return [complex_mod(item) for item in dft(samples, compute_half_range=True)]
