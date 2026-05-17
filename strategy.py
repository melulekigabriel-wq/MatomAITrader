import requests

def get_crypto_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    return float(requests.get(url).json()["price"])


def get_signal(symbol):
    symbol = symbol.upper()

    # ₿ CRYPTO
    if "BTC" in symbol:
        price = get_crypto_price("BTCUSDT")
        return f"BTC Price: {price} | SIGNAL: BUY 📈"

    # 💱 FOREX
    elif "EURUSD" in symbol:
        return "EUR/USD SIGNAL: SELL 📉"

    elif "GBPUSD" in symbol:
        return "GBP/USD SIGNAL: BUY 📈"

    # 🪙 GOLD (XAUUSD FIXED DATA SOURCE)
    elif "XAU" in symbol or "GOLD" in symbol:
        # simple proxy price (we upgrade to broker feed later)
        gold_price = 2030.50
        return f"XAUUSD Price: {gold_price} | SIGNAL: BUY 📈"

    else:
        return "Market not supported yet ❌"
