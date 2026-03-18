# 🚀 Dynamic Pricing API Engine

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)

> **Transforming Ride-Sharing Data Science into a highly available Full-Stack Pricing Service.**

## 🎯 The Business Problem: Market Imbalance
In ride-sharing platforms, static pricing leads to **lost revenue** and **poor UX**:
- **High Demand, Low Supply**: Riders can't find cars. The platform loses out on premium willingness-to-pay.
- **Low Demand, High Supply**: Drivers sit idle, earning nothing.

## 💡 The Solution: Real-Time Dynamic Pricing
This project implements a **dynamic multiplier system** based on real market data. By analyzing historical rides, this engine instantly calculates pricing multipliers to balance the market—incentivizing drivers during surges and attracting riders during lulls. 

### Interactive Dashboard Preview
![Dashboard Surge](./static/dashboard_surge.png)
🎨 **Premium UI**: Real-time interactive sliders with dynamic `Chart.js` visualizations.

---

## 🏗️ Architecture & Business Logic

The mathematical logic is decoupled into a dedicated `pricing_engine.py` to ensure unit testability and clean architecture. It relies on the absolute 25th (Low) and 75th (High) percentiles of our historical dataset as its baselines.

### The Pricing Multiplier Rules:
1. **Demand Factor**: `Current Riders / Baseline Riders`
2. **Supply Factor**: `Baseline Drivers / Current Drivers`
3. **Safety Threshold (0.8x)**: Implemented a strict floor to ensure prices **never drop below 80%** of the standard cost, protecting baseline profitability.
4. **Final Cost**: `Base Cost × max(Demand, 0.8) × max(Supply, 0.8)`

## 🚀 Run It Locally (Full-Stack)

Want to see the API and the Interactive Dashboard in action?

```bash
# 1. Clone the repository
git clone https://github.com/NguyenThuan-data/Dynamic_Pricing_Strategy.git
cd Dynamic_Pricing_Strategy

# 2. Set up a virtual environment
python -m venv venv
source venv/Scripts/activate  # On Windows

# 3. Install requirements
pip install -r requirements.txt

# 4. Run the FastAPI server
uvicorn main:app --reload
```

Then, open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your browser to interact with the visual pricing engine!

To view the interactive API Swagger docs, visit **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**.

## 👨‍💻 Tech Stack
- **Backend API**: FastAPI, Uvicorn, Python
- **Data Engine**: Pandas, Numpy (for initial baseline extraction)
- **Frontend Dashboard**: HTML5, Vanilla CSS (Glassmorphism), JavaScript (Fetch API, Chart.js)

## 📂 Repository Structure
```text
Dynamic_Pricing_Strategy/
├── main.py                 # FastAPI Application Server
├── pricing_engine.py       # Core isolated business logic
├── requirements.txt
├── dataset/
│   └── dynamic_pricing.csv # Historical baseline data
├── static/
│   ├── style.css           # Premium Glassmorphism styling
│   └── script.js           # Chart interaction and API fetching
└── templates/
    └── index.html          # Interactive Dashboard Markup
```

*Note: The original Jupyter Notebook analysis that sourced these pricing multipliers is still available in the history for reference.*
