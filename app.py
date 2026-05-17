from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():

    signals = ["BUY", "SELL", "WAIT"]
    signal = random.choice(signals)

    confidence = random.randint(70, 95)

    pairs = [
        "EUR/USD",
        "GBP/USD",
        "USD/JPY",
        "XAU/USD"
    ]

    pair = random.choice(pairs)

    html = f"""
    <html>
    <head>
        <title>Titan AI Trader</title>

        <style>
            body {{
                background-color: #0f172a;
                color: white;
                font-family: Arial;
                text-align: center;
                padding-top: 50px;
            }}

            .card {{
                background: #1e293b;
                margin: auto;
                width: 80%;
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 0 20px rgba(0,0,0,0.5);
            }}

            h1 {{
                color: #38bdf8;
            }}

            .signal {{
                font-size: 50px;
                margin: 20px;
            }}

            .confidence {{
                font-size: 30px;
                color: #22c55e;
            }}
        </style>
    </head>

    <body>

        <div class="card">
            <h1>TITAN AI TRADER</h1>

            <h2>{pair}</h2>

            <div class="signal">
                {signal}
            </div>

            <div class="confidence">
                Confidence: {confidence}%
            </div>

        </div>

    </body>
    </html>
    """

    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
