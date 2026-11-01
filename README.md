# agent-playground

A deliberately small repository for exercising an autonomous coding agent.

The agent under test is [dsh-superagent](https://github.com/deepseek-ai/dsh-superagent-prototype):
it listens to GitHub, opens a work item when someone asks, works in its own
session and directory, and answers with a pull request.

This repo gives it something safe to break.

## What is here

- `src/calc.py` — three small functions, all with known defects
- `tests/test_calc.py` — a test suite that fails on those defects
- `ISSUES.md` — the issue texts to paste into the tracker

## Run the tests

```sh
python3 -m venv .venv
.venv/bin/pip install -q pytest
.venv/bin/python -m pytest -q
```

Expected on a clean checkout: **3 failed, 5 passed**. A working agent turns
that into **8 passed**.

## How to ask the agent for work

Comment on an issue, addressing the agent account:

```
@<agent-login> please fix this
```

The agent opens a pull request. Review it like you would review a colleague's.
