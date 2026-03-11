# test_portfolio.py — Unit tests for Trade Vectors demo

import unittest
from portfolio import calculate_pnl, calculate_portfolio_value, get_risk_exposure, calculate_stop_loss

class TestPortfolio(unittest.TestCase):

    def test_calculate_pnl_profit(self):
        # Buy 100 shares at 500, sell at 550 = profit of 5000
        self.assertEqual(calculate_pnl(500, 550, 100), 5000)

    def test_calculate_pnl_loss(self):
        # Buy 50 shares at 200, sell at 180 = loss of 1000
        self.assertEqual(calculate_pnl(200, 180, 50), -1000)

    def test_portfolio_value(self):
        holdings = {
            "RELIANCE": (10, 2500),
            "INFY": (20, 1500),
        }
        # 10*2500 + 20*1500 = 25000 + 30000 = 55000
        self.assertEqual(calculate_portfolio_value(holdings), 55000)

    def test_risk_exposure(self):
        # Portfolio = 80000, Cash = 20000, Total = 100000
        # Risk exposure (invested) = 80000/100000 = 80%
        result = get_risk_exposure(80000, 20000)
        self.assertAlmostEqual(result, 80.0)

    def test_stop_loss(self):
        # Entry = 1000, Risk = 5% → Stop loss should be 950 (below entry)
        result = calculate_stop_loss(1000, 5)
        self.assertEqual(result, 950)

if __name__ == "__main__":
    unittest.main()
