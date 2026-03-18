document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const costInput = document.getElementById('historical-cost');
    const ridersInput = document.getElementById('riders-count');
    const driversInput = document.getElementById('drivers-count');
    
    const valCost = document.getElementById('val-cost');
    const valRiders = document.getElementById('val-riders');
    const valDrivers = document.getElementById('val-drivers');
    
    const resBase = document.getElementById('res-base');
    const resDynamic = document.getElementById('res-dynamic');
    const resDemand = document.getElementById('res-demand');
    const resSupply = document.getElementById('res-supply');
    const resStatus = document.getElementById('res-status');
    const calcBtn = document.getElementById('calculate-btn');

    // Chart.js Setup
    const ctx = document.getElementById('multiplierChart').getContext('2d');
    
    // Create gradient for chart
    const gradientDemand = ctx.createLinearGradient(0, 0, 0, 400);
    gradientDemand.addColorStop(0, 'rgba(56, 189, 248, 0.8)');
    gradientDemand.addColorStop(1, 'rgba(56, 189, 248, 0.1)');
    
    const gradientSupply = ctx.createLinearGradient(0, 0, 0, 400);
    gradientSupply.addColorStop(0, 'rgba(0, 204, 150, 0.8)');
    gradientSupply.addColorStop(1, 'rgba(0, 204, 150, 0.1)');

    let multiplierChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Demand Multiplier', 'Supply Multiplier', 'Total Adjustment'],
            datasets: [{
                label: 'Multiplier Impact',
                data: [1, 1, 1],
                backgroundColor: [gradientDemand, gradientSupply, 'rgba(99, 110, 250, 0.8)'],
                borderColor: ['#38bdf8', '#00cc96', '#636efa'],
                borderWidth: 1,
                borderRadius: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false }
            },
            scales: {
                y: {
                    title: { display: true, text: 'Factor', font: {family: 'Outfit', color: '#94a3b8'} },
                    beginAtZero: true,
                    grid: { color: 'rgba(255, 255, 255, 0.1)' },
                    ticks: { color: '#94a3b8' }
                },
                x: {
                    grid: { display: false },
                    ticks: { color: '#94a3b8', font: {family: 'Outfit'} }
                }
            },
            animation: {
                duration: 400,
                easing: 'easeOutQuart'
            }
        }
    });

    // Update labels on input scroll
    costInput.addEventListener('input', () => valCost.textContent = costInput.value);
    ridersInput.addEventListener('input', () => valRiders.textContent = ridersInput.value);
    driversInput.addEventListener('input', () => valDrivers.textContent = driversInput.value);

    // Dynamic Calculation API Call
    async function calculatePrice() {
        const payload = {
            historical_cost: parseFloat(costInput.value),
            riders_count: parseInt(ridersInput.value),
            drivers_count: parseInt(driversInput.value)
        };

        // Add a pulsing effect while calculating
        calcBtn.style.opacity = '0.7';
        calcBtn.innerText = 'Calculating...';

        try {
            const response = await fetch('/api/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                throw new Error("Network response was not ok");
            }

            const data = await response.json();
            
            // Update UI
            resBase.textContent = `$${data.original_cost.toFixed(2)}`;
            
            // Animate number count up (simplified)
            resDynamic.textContent = `$${data.adjusted_price.toFixed(2)}`;
            
            resDemand.textContent = `${data.demand_multiplier.toFixed(2)}x`;
            resSupply.textContent = `${data.supply_multiplier.toFixed(2)}x`;
            resStatus.textContent = data.market_condition;

            // Change colors based on status
            if (data.market_condition.includes('Surge')) {
                resStatus.style.color = '#ef4444'; // Danger/Surge
                resDynamic.style.color = '#ef4444';
                resDynamic.style.textShadow = '0 0 20px rgba(239, 68, 68, 0.4)';
            } else if (data.market_condition.includes('Discounted')) {
                resStatus.style.color = '#38bdf8'; // Blue/Cool
                resDynamic.style.color = '#38bdf8';
                resDynamic.style.textShadow = '0 0 20px rgba(56, 189, 248, 0.4)';
            } else {
                resStatus.style.color = '#00cc96'; // Balanced
                resDynamic.style.color = '#00cc96';
                resDynamic.style.textShadow = '0 0 20px rgba(0, 204, 150, 0.4)';
            }

            // Update Chart
            multiplierChart.data.datasets[0].data = [
                data.demand_multiplier, 
                data.supply_multiplier, 
                data.final_multiplier
            ];
            multiplierChart.update();

        } catch (error) {
            console.error('Error calculating price:', error);
            resDynamic.textContent = 'Error';
        } finally {
            // Restore button state
            calcBtn.style.opacity = '1';
            calcBtn.innerText = 'Calculate Dynamic Price';
        }
    }

    // Attach Event Listeners
    calcBtn.addEventListener('click', calculatePrice);
    
    // Auto-calculate on slider release (change) for better UX
    costInput.addEventListener('change', calculatePrice);
    ridersInput.addEventListener('change', calculatePrice);
    driversInput.addEventListener('change', calculatePrice);

    // Initial load calculation
    calculatePrice();
});
