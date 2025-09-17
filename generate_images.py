#!/usr/bin/env python3
"""
Script to generate static images from Plotly HTML files for GitHub compatibility
"""

import os
import subprocess
import sys

def install_kaleido():
    """Install kaleido package for static image generation"""
    try:
        import kaleido
        print("✅ Kaleido is already installed")
        return True
    except ImportError:
        print("📦 Installing kaleido...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "kaleido"])
        return True

def generate_images():
    """Generate static images from the notebook"""
    print("🖼️  Generating static images for GitHub...")
    
    # Install required packages
    install_kaleido()
    
    # Run the notebook to generate images
    try:
        import subprocess
        result = subprocess.run([
            sys.executable, "-c", 
            """
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Load data
df = pd.read_csv('./dataset/dynamic_pricing.csv')

# 1. Scatter plot
fig1 = px.scatter(df, x='Expected_Ride_Duration', 
                 y='Historical_Cost_of_Ride',
                 title='Expected Ride Duration vs. Historical Cost of Ride', 
                 trendline='ols')
fig1.write_image('plots/scatter_plot.png', width=800, height=600)
print('✅ Generated scatter_plot.png')

# 2. Box plot
fig2 = px.box(df, x='Vehicle_Type', y='Historical_Cost_of_Ride', 
             title='Distribution of Historical Cost of Rides by Vehicle Type')
fig2.write_image('plots/box_plot.png', width=800, height=600)
print('✅ Generated box_plot.png')

# 3. Correlation heatmap
df_numeric = df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = df_numeric.corr()

annotations = []
for i, row in enumerate(correlation_matrix.values):
    for j, value in enumerate(row):
        annotations.append(
            dict(
                x=correlation_matrix.columns[j],
                y=correlation_matrix.columns[i],
                text=f"{value:.2f}",
                showarrow=False,
                font=dict(color="black" if abs(value) < 0.5 else "white")
            )
        )

fig3 = go.Figure(data=go.Heatmap(
    z=correlation_matrix.values,
    x=correlation_matrix.columns,
    y=correlation_matrix.columns,
    colorscale='RdBu'
))
fig3.update_layout(annotations=annotations)
fig3.update_layout(title='Correlation Matrix of Features')
fig3.write_image('plots/correlation_heatmap.png', width=800, height=600)
print('✅ Generated correlation_heatmap.png')

print('🎉 All images generated successfully!')
            """
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(result.stdout)
            print("✅ All static images generated successfully!")
        else:
            print("❌ Error generating images:")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_images()
