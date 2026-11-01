# Issues to file

Paste each block below into a separate GitHub issue on this repository.
They are written the way a teammate would write them: symptom first, no
solution prescribed.

---

## 1. Dividing by zero crashes instead of failing cleanly

`divide(1, 0)` raises `ZeroDivisionError`, which escapes as an unhandled
exception. Callers cannot distinguish "you asked something impossible" from
"the program is broken".

It should raise `ValueError` with a message that says what went wrong.

`tests/test_calc.py::test_divide_by_zero_raises_value_error` covers this.

---

## 2. Duration parser accepts garbage

`parse_duration("5x")` raises `KeyError`, and `parse_duration("")` raises
`IndexError`. Both are accidents of the implementation leaking out.

Any input that is not a positive integer followed by `s`, `m` or `h` should
raise `ValueError` with a message naming the offending input.

Covered by `test_parse_duration_rejects_unknown_unit` and
`test_parse_duration_rejects_empty_input`.

---

## 3. average() of an empty list divides by zero

`average([])` raises `ZeroDivisionError`. The agreed behaviour is to return
`0` for an empty sequence.

Covered by `test_average_of_empty_list_is_zero`.
