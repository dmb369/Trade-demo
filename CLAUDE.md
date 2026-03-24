# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run all tests
python3 -m unittest test_portfolio.py -v

# Run a single test
python3 -m unittest test_portfolio.TestPortfolio.test_calculate_pnl_profit -v
```

## Architecture

This is a small Python demo project with two files:

- **`portfolio.py`** — Core trading utility functions: P&L calculation, portfolio valuation, risk exposure, stop-loss pricing, and diversification scoring.
- **`test_portfolio.py`** — `unittest`-based tests for the functions in `portfolio.py`.

No dependencies beyond the Python standard library.
