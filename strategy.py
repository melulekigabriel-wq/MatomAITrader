import requests

# -------------------------
# LIVE CRYPTO PRICE
# -------------------------
def get_crypto_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    return float(requests.get(url).json()["price"])


# -------------------------
# SIMPLE AI SCORING ENGINE
# -------------------------
def ai_score(price):
    """
    Fake but structured AI logic:
    We simulate "market pressure scoring"
    """

    score = 0

    # randomness-based trend simulation (temporary AI behavior)
    if price % 2 < 1:
        score += 2
    else:
        score -= 1

    if price % 5 < 2:
        score += 1
    else:
        score -= 1

    return score


# -------------------------
# MAIN SIGNAL ENGINE
# -------------------------
def get_signal(symbol):
    symbol = symbol.upper()

    # ₿ CRYPTO
    if "BTC" in symbol:
        price = get_crypto_price("BTCUSDT")
        score = ai_score(price)

        if score >= 2:
            return f"BTC {price} → STRONG BUY 📈 (AI Score: {score})"
        elif score <= -1:
            return f"BTC {price} → SELL 📉 (AI Score: {score})"
        else:
            return f"BTC {price} → HOLD ⏸ (AI Score: {score})"


    # 💱 FOREX (simple simulated logic for now)
    elif "EURUSD" in symbol:
        score = 1
        return f"EUR/USD → BUY 📈 (AI Score: {score})"

    elif "GBPUSD" in symbol:
        score = -1
        return f"GBP/USD → SELL 📉 (AI Score: {score})"


    # 🪙 GOLD
    elif "XAU" in symbol or "GOLD" in symbol:
        score = 0
        return f"XAUUSD → HOLD ⏸ (AI Score: {score})"


    else:
        return "Market not supported ❌"
