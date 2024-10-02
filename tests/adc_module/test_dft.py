from datetime import UTC, datetime
from math import sin

from adc_module.fft import dft


def test_dft() -> None:
    domain = range(32)
    samples = [
        (
            sin(3 * 6.28 * index / len(domain))
            + sin(3 * 6.28 * 2 * index / len(domain))
            + sin(3 * 6.28 * 3 * index / len(domain))
        )
        for index in domain
    ]

    calc_dft = dft(samples)

    assert len(calc_dft) == len(domain) / 2

    assert calc_dft == [
        0.029045950679708277,
        0.02911756937521813,
        0.02933403343541255,
        16.001723069350735,
        0.03022470518647224,
        0.030919911319971193,
        15.994754412546285,
        0.03289761484139758,
        0.03423379716590294,
        15.986482089356826,
        0.03780488800478127,
        0.040163523552789716,
        0.04302343216516519,
        0.046516605985673275,
        0.05082988318139054,
        0.056236398960222214,
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
        _ = dft(samples)
    t1 = datetime.now(tz=UTC)
    delta2 = t1 - t0

    assert delta2.microseconds > 0
