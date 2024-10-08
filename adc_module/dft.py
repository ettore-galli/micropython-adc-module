from math import cos, pi, sin


class DftCalculator:
    def __init__(self, data_length: int) -> None:
        self.data_length: int = data_length
        self.twiddle_factors: dict[tuple[int, int], tuple[float, float]] = (
            self.precompute_twiddle_factors(data_length=data_length)
        )
        self.index_range: list[int] = list(range(self.data_length))
        self.half_range: list[int] = list(range(self.data_length // 2))

    @staticmethod
    def precompute_twiddle_factors(
        data_length: int,
    ) -> dict[tuple[int, int], tuple[float, float]]:
        return {
            (index, k_index): (
                cos(-2.0 * pi * index * k_index / data_length),
                sin(-2.0 * pi * index * k_index / data_length),
            )
            for index in range(data_length)
            for k_index in range(data_length)
        }

    def dft(
        self, samples: list[float], *, compute_half_range: bool = True
    ) -> list[tuple[float, float]]:
        """
        Reference:
        https://scistatcalc.blogspot.com/2013/12/fft-calculator.html
        https://www.audiolabs-erlangen.de/resources/MIR/PCP/PCP_09_dft.html#exercise_k_index
        https://en.wikipedia.org/wiki/Discrete_Fourier_transform
        """

        def dft_term(samples: list[float], k_index: int) -> tuple[float, float]:
            return (
                sum(
                    samples[index] * self.twiddle_factors[(index, k_index)][0]
                    for index in self.index_range
                ),
                sum(
                    samples[index] * self.twiddle_factors[(index, k_index)][1]
                    for index in self.index_range
                ),
            )

        return [
            dft_term(samples=samples, k_index=index)
            for index in (self.half_range if compute_half_range else self.index_range)
        ]


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
