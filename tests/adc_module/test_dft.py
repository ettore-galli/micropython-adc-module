from datetime import UTC, datetime
from math import sin

from adc_module.adc_module_logic import GhostDetector


def normalize(values: list[float], top: int) -> list[int]:
    bottom = min(*values)
    peaks = max(*values) - min(*values)
    return [int((point - bottom) * top / peaks) for point in values]


def plot(values: list[float]) -> None:
    for point in normalize(values, 64):
        print(("-" * (point - 1) if point > 1 else "") + "*")  # noqa: T201


def test_perform_mod_dft() -> None:
    domain = range(32)
    samples = [
        (
            sin(3 * 6.28 * index / len(domain))
            + sin(3 * 6.28 * 2 * index / len(domain))
            + sin(3 * 6.28 * 3 * index / len(domain))
        )
        for index in domain
    ]

    dft = GhostDetector.perform_mod_dft(samples)

    assert len(dft) == len(domain) / 2

    assert dft == [
        0.04107717738326346,
        0.041069782325346256,
        0.04104747844926989,
        0.041009903442527154,
        0.04095643214248368,
        0.04088614228788678,
        0.04079776160146007,
        0.040689590199818375,
        0.04055938882751079,
        0.04040421790439347,
        0.04022020334111717,
        0.04000218967330871,
        0.039743213726489625,
        0.03943368128446656,
        0.03906003015414369,
        0.03860245747810537,
    ]


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

    number_of_test_iterations = 2

    t0 = datetime.now(tz=UTC)
    for _ in range(number_of_test_iterations):
        _ = GhostDetector.perform_mod_dft(samples)
    t1 = datetime.now(tz=UTC)
    delta2 = t1 - t0

    assert delta2.microseconds > 0
