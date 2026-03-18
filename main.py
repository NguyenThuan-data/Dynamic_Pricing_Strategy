from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

from pricing_engine import PricingEngine

app = FastAPI(
    title="Dynamic Pricing Engine API",
    description="A real-time pricing engine that balances supply and demand.",
    version="1.0.0"
)

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (we will create this directory later)
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Request Schema
class PricingRequest(BaseModel):
    historical_cost: float
    riders_count: int
    drivers_count: int

@app.post("/api/calculate")
async def calculate_dynamic_price(request: PricingRequest):
    """
    Calculates the new dynamic price based on historical cost, 
    current rider demand, and current driver supply.
    """
    if request.historical_cost <= 0 or request.riders_count < 0 or request.drivers_count <= 0:
        raise HTTPException(status_code=400, detail="Invalid input values. Drivers count must be > 0.")
        
    result = PricingEngine.calculate_price(
        historical_cost=request.historical_cost,
        riders_count=request.riders_count,
        drivers_count=request.drivers_count
    )
    
    return result

@app.get("/", response_class=HTMLResponse)
async def serve_dashboard():
    """
    Serves the interactive HTML dashboard.
    """
    template_path = os.path.join(os.path.dirname(__file__), "templates", "index.html")
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1 style='color: white; font-family: sans-serif; text-align: center; margin-top: 20%;'>Dashboard initializing... (Template not found)</h1>"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
