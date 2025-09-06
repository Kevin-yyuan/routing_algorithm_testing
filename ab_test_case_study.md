<link rel="stylesheet" href="style.css">

<div class="report-container">

<div class="header">
<h1>XYZ Logistics Inc. | Toronto Operations</h1>
<p>Internal Memo: For Immediate Management Review</p>
</div>

TO: Senior Logistics Management, Toronto

FROM: Kevin Yuan, Business & Data Analyst

SUBJECT: Final Recommendation on Eco-Algorithm Deployment

<div class="summary">
<h2>Executive Recommendation</h2>
<p>I recommend we move forward with a <strong>strategic, hybrid deployment</strong> of the new eco-friendly routing algorithm. The A/B test has conclusively shown that the algorithm <strong>successfully reduces fuel consumption</strong> but at the cost of a <strong>statistically significant increase in delivery times.</strong> A full rollout is therefore inadvisable. Instead, a targeted approach will allow us to capture the cost savings while mitigating risk to our service-level agreements and customer satisfaction.</p>
</div>

<h3 class="section-title">Analysis of Fuel Consumption (Primary Metric)</h3>
The primary goal was to reduce fuel costs. The test data confirms the new algorithm is highly effective. Group B (Eco-Algorithm) demonstrated a visibly lower average fuel consumption than the control group. A formal t-test yielded a p-value of 0.0000, confirming with high statistical confidence that these fuel savings are a real effect.

<div class="chart">
<img src="fuel_distribution.png" alt="Distribution chart showing Group B's fuel consumption is lower than Group A's.">
<p class="chart-caption">Figure 1: Group B shows a clear leftward shift, indicating a consistent reduction in fuel consumed per trip.</p>
</div>

<h3 class="section-title">Analysis of Delivery Time (Guardrail Metric)</h3>
Our critical guardrail metric was delivery time. The data shows a small but consistent increase for Group B. While minor, a t-test confirmed this increase is a real and predictable side effect, with a p-value of 0.0197—below our 0.05 significance threshold.

<div class="chart">
<img src="time_distribution.png" alt="Distribution chart showing Group B's delivery time is slightly higher than Group A's.">
<p class="chart-caption">Figure 2: Group B's distribution is shifted slightly right, indicating a statistically significant trend of longer delivery times.</p>
</div>

<h3 class="section-title">Strategic Path Forward</h3>
<p>The analysis presents a clear trade-off: cost savings vs. delivery speed. The financial model shows a net saving of <strong>$2.10 per trip</strong> with the new algorithm. To harness the benefits while managing the drawbacks, I propose the following three-step action plan:</p>
<ol>
<li><strong>Financial Summary:</strong>
<ul>
<li><strong>Average Fuel Savings:</strong> 2.04 litres per trip, valued at <strong>$3.06</strong>.</li>
<li><strong>Average Time Increase:</strong> 2.32 minutes per trip, costing <strong>$0.97</strong> in driver wages.</li>
<li><strong>Net Financial Impact:</strong> A net saving of <strong>$2.10 per trip</strong>.</li>
</ul>
</li>
<li><strong>Initiate a Hybrid Deployment (Q4 2025):</strong> Based on the financial model, we will deploy the new algorithm selectively.
<ul>
<li><strong>"Standard" Shipments:</strong> All non-urgent domestic deliveries will default to the new eco-algorithm to maximize fuel savings.</li>
<li><strong>"Priority/Express" Shipments:</strong> All time-sensitive and cross-border shipments will continue to use the standard algorithm to guarantee delivery speed.</li>
</ul>
</li>
<li><strong>Monitor and Iterate:</strong> We will continuously monitor the performance of both algorithms and customer feedback in Q4 to refine this hybrid model, ensuring we are achieving the optimal balance of cost efficiency and service quality for our Toronto-based operations.</li>
</ol>

<div class="footer">
For a complete breakdown of the statistical methodology and Python code, please refer to the <a href="Eco-Friendly_routing_algorithm.ipynb" target="_blank">full analysis in the project's Jupyter Notebook</a>.
</div>
