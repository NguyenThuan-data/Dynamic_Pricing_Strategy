# Dynamic Pricing Implementation

## 🌐 Interactive Visualizations

### **[View Interactive Plots →](https://NguyenThuan-data.github.io/Dynamic_Pricing_Strategy/)**

## Overview
This project implements a sophisticated dynamic pricing algorithm for ride-sharing services, analyzing demand and supply patterns to optimize pricing strategies.

## Data Analysis Visualizations

### 1. Ride Duration vs Cost Analysis
![Scatter Plot](plots/scatter_plot.png)
*This scatter plot shows the relationship between expected ride duration and historical cost, with a trend line indicating the correlation.*

**Interactive Version**: [View Interactive Plot](plots/Expected_Ride_Duration_vs_Historical_Cost_of_Ride.html)
*Insights:* We can see that the relationship between the expected duration with the cost the positvely increasing with very few dots far from the trend line. This suggest the duration is a good prediction factor of cost.

### 2. Vehicle Type Cost Distribution
![Box Plot](plots/box_plot.png)
*Box plot comparing cost distributions between Economy and Premium vehicle types.*

**Interactive Version**: [View Interactive Plot](plots/Distribution_of_Historical_Cost_of_Rides_by_Vehicle_Type.html)

### 3. Feature Correlation Matrix
![Correlation Matrix](plots/correlation_heatmap.png)
*This heatmap visualizes the correlations between all numeric features in the dataset, helping to identify which features most strongly influence the historical cost of rides.*

**Interactive Version**: [View Interactive Plot](plots/Correlation_Matrix_of_Features.html)
*Insight:* Use this matrix to select the features that have the highest correlation with historical cost, which is expected ride duration, for further analysis and model building

### Conclusion:
With the outcome, the company shows that the company only take expected ride duration for determine the cost and we can use that for dynamic pricing implementation. 

## Dynamic Pricing Implementation

### Complete Workflow:
1. Calculate raw multipliers from demand/supply data
2. Apply safety thresholds to prevent extremes
3. Multiply with base price to get final dynamic price
4. Result: Smart, balanced dynamic pricing! 🎯

### Key Components:
- **Demand Multiplier**: Uses 75th and 25th percentiles to categorize demand levels
- **Supply Multiplier**: Monitors driver availability patterns
- **price adjustment factors(Thresholds)**: Prevents extreme price fluctuations (20% max change)
- **Adjusted Price Cost**: Real-time price adjustments based on market conditions

## Result
### Business Benefits:
- Increased revenue during high demand periods
- Competitive pricing during low demand
- Customer satisfaction through reasonable pricing
- Driver retention through stable earnings
