"""Tests for calc. Two of these fail until the open issues are fixed."""

import pytest

from src.calc import average, divide, parse_duration


def test_divide_returns_quotient():
    assert divide(6, 3) == 2


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_parse_duration_minutes():
    assert parse_duration("5m") == 300


def test_parse_duration_hours():
    assert parse_duration("2h") == 7200


def test_parse_duration_rejects_unknown_unit():
    with pytest.raises(ValueError):
        parse_duration("5x")


def test_parse_duration_rejects_empty_input():
    with pytest.raises(ValueError):
        parse_duration("")


def test_average_of_values():
    assert average([1, 2, 3]) == 2


def test_average_of_empty_list_is_zero():
    assert average([]) == 0
