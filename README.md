# Dynamic Pricing Implementation

## Excecutive Summary
Undertanding **Dynamic Pricing** unlocks powerful business value—enabling companies to boost revenue, respond to market shifts, and optimize customer experience. This project demonstrates, through a practical case study, how data-driven pricing strategies can be transformed into an effective **Price Recommendation System**. Learning these techniques provides actionable insights that drive real business impact and create a strong competitive edge.

### What is Dynamic Pricing? Why is it necessary?

**Dynamic Pricing** is a strategy where the price of a product or service is adjusted in real-time based on current market demand, supply, competition, and other external factors. Instead of having a fixed price, businesses use algorithms and data analysis to set prices that can change frequently—sometimes with specific threshhold(daoly, weekly or even minutes by minutes).

**Why is it necessary?**
- **Maximizes Revenue:** By increasing prices during periods of high demand (like rush hour for ride-sharing), companies can earn more from customers willing to pay extra.
- **Balances Supply and Demand:** Dynamic pricing helps ensure that supply (like available drivers) matches demand, reducing wait times and improving service efficiency.
- **Stays Competitive:** It allows businesses to respond quickly to market changes and competitor pricing, ensuring they remain attractive to customers.
- **Encourages Efficient Resource Use:** For services with limited resources (like hotel rooms or rides), dynamic pricing helps allocate those resources where they are most valued.
- **Improves Customer Experience:** By lowering prices during off-peak times, companies can attract more customers and increase utilization.

In summary, dynamic pricing is essential for optimizing both business revenue and customer satisfaction in fast-changing markets.

## Project Overview
This project using a Ride-sharing [dataset](https://statso.io/2023/06/25/dynamic-pricing-case-study/), which has information about:
- Number of Riders
- Number of Drivers
- Location
- Historical cost
- ....  

This project begins with a thorough analysis of the original dataset, followed by clear visualizations to identify the most impactful factors influencing pricing. Leveraging these insights, we implement a dynamic pricing strategy tailored to real-world demand and supply patterns. Building on this foundation, we develop a predictive model capable of recommending optimal price adjustments in real time. The approach is designed for scalability and can be further developed into a robust, automated pricing solution—empowering businesses to maximize revenue, respond quickly to market changes, and deliver greater value to both customers and stakeholders. This solution is accessible and actionable for decision-makers, by directly addressing key business challenges such as profitability, competitiveness, and operational efficiency.

## Data Analysis Visualizations(**[View Interactive Plots →](https://NguyenThuan-data.github.io/Dynamic_Pricing_Strategy/)**)

### 1. Ride Duration vs Cost Analysis
![Scatter Plot](plots/scatter_plot.png)  
*This scatter plot shows the relationship between expected ride duration and historical cost, with a trend line indicating the correlation.*  
*Insights:* We can see that the relationship between the expected duration with the cost the positvely increasing with very few dots far from the trend line. This suggest the duration is a good prediction factor of cost.

### 2. Vehicle Type Cost Distribution
![Box Plot](plots/box_plot.png)  
*Box plot comparing cost distributions between Economy and Premium vehicle types.*

### 3. Feature Correlation Matrix
![Correlation Matrix](plots/correlation_heatmap.png)  
*This heatmap visualizes the correlations between all numeric features in the dataset, helping to identify which features most strongly influence the historical cost of rides.*  
*Insight:* Use this matrix to select the features that have the highest correlation with historical cost, which is expected ride duration, for further analysis and model building

### Conclusion:
With the outcome, the company shows that the company only take expected ride duration for determine the cost and we can use that as primary factor for dynamic pricing implementation. 

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


## Predictive Model:

## Result
### Business Benefits:
- Increased revenue during high demand periods
- Competitive pricing during low demand
- Customer satisfaction through reasonable pricing
- Driver retention through stable earnings

## References:
* [Dynamic Pricing: Case Study](https://statso.io/2023/06/25/dynamic-pricing-case-study/)
* [Article](https://amanxai.com/2023/06/26/dynamic-pricing-strategy-using-python/)
