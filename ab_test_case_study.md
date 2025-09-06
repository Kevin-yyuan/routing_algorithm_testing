<style>
.report-container { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; max-width: 800px; margin: auto; color: #333; line-height: 1.6; }
.header { text-align: center; border-bottom: 2px solid #004080; padding-bottom: 10px; margin-bottom: 20px; }
.header h1 { margin: 0; color: #004080; font-size: 24px; }
.header p { margin: 5px 0 0 0; color: #555; font-size: 12px; }
.summary { background-color: #e6f0ff; border-left: 5px solid #004080; padding: 15px; margin-bottom: 25px; }
.summary h2 { margin-top: 0; font-size: 18px; color: #004080;}
.section-title { color: #004080; font-size: 20px; border-bottom: 1px solid #ccc; padding-bottom: 5px; margin-top: 30px; }
.chart { text-align: center; margin: 20px 0; }
.chart img { max-width: 90%; border: 1px solid #ddd; padding: 2px; }
.chart-caption { font-size: 12px; color: #666; font-style: italic; margin-top: 5px; }
.recommendations ol { padding-left: 20px; }
.recommendations li { margin-bottom: 10px; }
.footer { text-align: center; font-size: 12px; color: #777; margin-top: 40px; border-top: 1px solid #ccc; padding-top: 10px; }
</style>

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
The analysis presents a clear trade-off: cost savings vs. delivery speed. To harness the benefits while managing the drawbacks, I propose the following three-step action plan:

Quantify the Financial Trade-Off (Week of Sep 8): The immediate next step is to translate these findings into a clear financial model, offsetting the dollar value of fuel saved against the increased cost of driver wages and potential SLA penalties.

Initiate a Hybrid Deployment (Q4 2025): Based on the financial model, we will deploy the new algorithm selectively.

"Standard" Shipments: All non-urgent domestic deliveries will default to the new eco-algorithm to maximize fuel savings.

"Priority/Express" Shipments: All time-sensitive and cross-border shipments will continue to use the standard algorithm to guarantee delivery speed.

Monitor and Iterate: We will continuously monitor the performance of both algorithms and customer feedback in Q4 to refine this hybrid model, ensuring we are achieving the optimal balance of cost efficiency and service quality for our Toronto-based operations.

<div class="footer">
For a complete breakdown of the statistical methodology and Python code, please refer to the <a href="https://github.com/Kevin-yyuan/routing_algorithm_testing.git" target="_blank">full analysis in the project's Jupyter Notebook on GitHub</a>.
</div>
