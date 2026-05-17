import requests

# -----------------------
# CRYPTO (Binance)
# -----------------------
def get_crypto_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    data = requests.get(url).json()
    return float(data["price"])


# -----------------------
# FOREX (free API)
# -----------------------
def get_forex_price(base="EUR", target="USD"):
    url = f"https://api.exchangerate.host/latest?base={base}&symbols={target}"
    data = requests.get(url).json()
    return data["rates"][target]


# -----------------------
# SIGNAL ENGINE
# -----------------------
def get_signal(symbol):
    symbol = symbol.upper()

    # CRYPTO
    if "BTC" in symbol:
        price = get_crypto_price("BTCUSDT")
        return f"BTC Live Price: {price} | SIGNAL: BUY 📈"

    # FOREX
    elif "EUR" in symbol and "USD" in symbol:
        price = get_forex_price("EUR", "USD")
        return f"EUR/USD: {price} | SIGNAL: SELL 📉"

    elif "GBP" in symbol and "USD" in symbol:
        price = get_forex_price("GBP", "USD")
        return f"GBP/USD: {price} | SIGNAL: BUY 📈"

    # GOLD (simple placeholder for now)
    elif "GOLD" in symbol or "XAU" in symbol:
        return "XAUUSD: Market data coming next step ⏳"

    else:
        return "Market not supported yet ❌"
