import requests

def get_crypto_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    data = requests.get(url).json()
    return float(data["price"])


def get_signal(symbol):
    symbol = symbol.upper()

    # ONLY crypto for now (we expand later)
    if "BTC" in symbol:
        price = get_crypto_price("BTCUSDT")

        if price % 2 == 0:
            return f"BUY 📈 BTC Price: {price}"
        else:
            return f"SELL 📉 BTC Price: {price}"

    return "HOLD ⏸ (Market not supported yet)"
