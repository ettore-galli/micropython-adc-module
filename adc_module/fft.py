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
