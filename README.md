# Eco-Friendly Routing Algorithm Analysis

This project analyzes the results of an A/B test for a new eco-friendly routing algorithm. The goal is to determine the impact of the new algorithm on fuel consumption and delivery times, and to provide a recommendation on whether to deploy the new algorithm.

## File Descriptions

-   `ab_test_case_study.md`: A formal report summarizing the A/B test results and providing a recommendation for a hybrid deployment strategy.
-   `style.css`: The stylesheet for the `ab_test_case_study.md` report.
-   `Eco-Friendly_routing_algorithm.ipynb`: A Jupyter notebook with the detailed analysis of the A/B test, including statistical tests and financial modeling.
-   `ab_test_results.csv`: The raw data from the A/B test, containing the results for the control group (Group A) and the treatment group (Group B).
-   `fuel_distribution.png`: A chart showing the distribution of fuel consumption for both groups.
-   `time_distribution.png`: A chart showing the distribution of delivery times for both groups.

## How to Run

To run the analysis, you need to have Jupyter Notebook installed. You can then run the following command in your terminal:

```bash
jupyter notebook Eco-Friendly_routing_algorithm.ipynb
```

This will open the Jupyter notebook in your browser. You can then run the cells in the notebook to see the analysis.

## Analysis Summary

The A/B test shows that the new eco-friendly routing algorithm has the following effects:

-   **Fuel Consumption:** The new algorithm significantly reduces fuel consumption by an average of 2.04 litres per trip.
-   **Delivery Time:** The new algorithm slightly increases delivery times by an average of 2.32 minutes per trip.

The financial analysis shows that the fuel savings outweigh the costs of the increased delivery times, resulting in a **net saving of $2.10 per trip**.

Based on these results, the recommendation is to proceed with a **hybrid deployment** of the new algorithm, using it for standard shipments and retaining the standard algorithm for priority shipments.
