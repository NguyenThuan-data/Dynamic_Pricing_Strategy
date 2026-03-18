import pandas as pd
import numpy as np
import os

# Load dataset once to compute baseline percentiles
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'dataset', 'dynamic_pricing.csv')

def load_baselines():
    try:
        df = pd.read_csv(DATA_PATH)
        return {
            "demand_high_p75": np.percentile(df['Number_of_Riders'], 75),
            "demand_low_p25": np.percentile(df['Number_of_Riders'], 25),
            "supply_high_p75": np.percentile(df['Number_of_Drivers'], 75),
            "supply_low_p25": np.percentile(df['Number_of_Drivers'], 25)
        }
    except Exception as e:
        # Fallback values if dataset is missing
        return {
            "demand_high_p75": 70.0,
            "demand_low_p25": 40.0,
            "supply_high_p75": 30.0,
            "supply_low_p25": 10.0
        }

BASELINES = load_baselines()

class PricingEngine:
    """
    Core engine for dynamic pricing calculations.
    Isolated from the API layer for testability and clean architecture.
    """
    
    DEMAND_THRESHOLD_LOW = 0.8
    SUPPLY_THRESHOLD_HIGH = 0.8
    
    @classmethod
    def calculate_price(cls, historical_cost: float, riders_count: int, drivers_count: int) -> dict:
        """
        Calculates the dynamic price based on the current market conditions.
        """
        # 1. Calculate Demand Multiplier
        if riders_count > BASELINES["demand_high_p75"]:
            demand_multiplier = riders_count / BASELINES["demand_high_p75"]
        else:
            demand_multiplier = riders_count / BASELINES["demand_low_p25"]
            
        # 2. Calculate Supply Multiplier
        if drivers_count > BASELINES["supply_low_p25"]:
            supply_multiplier = BASELINES["supply_high_p75"] / drivers_count
        else:
            supply_multiplier = BASELINES["supply_low_p25"] / drivers_count
            
        # 3. Apply Thresholds (preventing extreme price drops)
        final_demand_multiplier = max(demand_multiplier, cls.DEMAND_THRESHOLD_LOW)
        final_supply_multiplier = max(supply_multiplier, cls.SUPPLY_THRESHOLD_HIGH)
        
        # 4. Calculate Final Price
        adjusted_price = historical_cost * (final_demand_multiplier * final_supply_multiplier)
        
        # 5. Business Logic Meta-data (for transparency and UI display)
        market_condition = "Balanced"
        if demand_multiplier > 1.2 and supply_multiplier > 1.2:
            market_condition = "High Demand, Low Supply (Surge)"
        elif demand_multiplier < 0.8 and supply_multiplier < 0.8:
            market_condition = "Low Demand, High Supply (Discounted)"
        elif demand_multiplier > 1.0:
            market_condition = "High Demand"
        elif supply_multiplier > 1.0:
            market_condition = "Low Supply"
            
        return {
            "original_cost": round(historical_cost, 2),
            "adjusted_price": round(adjusted_price, 2),
            "demand_multiplier": round(demand_multiplier, 2),
            "supply_multiplier": round(supply_multiplier, 2),
            "final_multiplier": round(final_demand_multiplier * final_supply_multiplier, 2),
            "market_condition": market_condition
        }
