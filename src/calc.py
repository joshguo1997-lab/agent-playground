"""A tiny calculator, used as a playground for an autonomous coding agent.

The functions below are deliberately incomplete: the test suite fails on them.
That is the point. Each failure maps to an issue in the tracker.
"""


def divide(a: float, b: float) -> float:
    """Return a / b."""
    return a / b


def parse_duration(text: str) -> int:
    """Parse a duration such as '90s', '5m' or '2h' into seconds."""
    value = int(text[:-1])
    unit = text[-1]
    return value * {"s": 1, "m": 60, "h": 3600}[unit]


def average(values: list[float]) -> float:
    """Return the arithmetic mean of values."""
    return sum(values) / len(values)
