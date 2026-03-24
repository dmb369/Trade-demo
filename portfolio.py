# portfolio.py — Trade Vectors Demo Project

def calculate_pnl(buy_price, sell_price, quantity):
    """Calculate profit and loss for a trade."""
    return (sell_price - buy_price) * quantity

def calculate_portfolio_value(holdings):
    """Calculate total portfolio value from a dict of {ticker: (quantity, current_price)}"""
    total = 0
    for ticker, data in holdings.items():
        quantity, price = data
        total += quantity * price
    return total

def get_risk_exposure(portfolio_value, cash_balance):
    """Returns percentage of total capital that is invested."""
    total_capital = portfolio_value + cash_balance
    return (portfolio_value / total_capital) * 100

def calculate_stop_loss(entry_price, risk_percent):
    """Calculate stop loss price given entry and risk percentage."""
    return entry_price - (entry_price * risk_percent / 100)

def diversification_score(holdings):
    """Returns number of unique sectors — placeholder for demo."""
    return len(holdings)
