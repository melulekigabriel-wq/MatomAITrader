import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


# -----------------------------
# GET MARKET DATA
# -----------------------------
def get_data(symbol="BTC-USD"):
    data = yf.download(symbol, period="6mo", interval="1d")
    data = data.dropna()

    data["Target"] = (data["Close"].shift(-1) > data["Close"]).astype(int)

    return data


# -----------------------------
# TRAIN MODEL
# -----------------------------
def train_model(data):
    features = ["Open", "High", "Low", "Close", "Volume"]

    X = data[features][:-1]
    y = data["Target"][:-1]

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)

    return model


# -----------------------------
# PREDICT SIGNAL
# -----------------------------
def predict_signal(symbol="BTC-USD"):
    data = get_data(symbol)

    model = train_model(data)

    latest = data[["Open", "High", "Low", "Close", "Volume"]].iloc[-1].values.reshape(1, -1)

    prediction = model.predict(latest)[0]

    price = data["Close"].iloc[-1]

    if prediction == 1:
        return f"{symbol} {price:.2f} → BUY 📈 (AI Prediction)"
    else:
        return f"{symbol} {price:.2f} → SELL 📉 (AI Prediction)"


# -----------------------------
# MAIN FUNCTION
# -----------------------------
def get_signal(symbol):
    symbol = symbol.upper()

    # Crypto
    if "BTC" in symbol:
        return predict_signal("BTC-USD")

    # Forex
    elif "EURUSD" in symbol:
        return predict_signal("EURUSD=X")

    elif "GBPUSD" in symbol:
        return predict_signal("GBPUSD=X")

    # Gold
    elif "XAU" in symbol or "GOLD" in symbol:
        return predict_signal("GC=F")

    else:
        return "Market not supported ❌"
