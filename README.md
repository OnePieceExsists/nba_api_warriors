NBA Warriors vs. Raptors Analysis

This project demonstrates how to use the [nba_api](https://github.com/swar/nba_api) to analyze NBA game data, specifically focusing on the Golden State Warriors' performance against the Toronto Raptors.

# Project Structure

- **nbaapi.py**  
  A standalone Python script that downloads, processes, and visualizes the data. Run this file directly for a quick analysis and plot.

- **nbaapi.ipynb**  
  A Jupyter Notebook version of the analysis, with inline code cells, outputs, and visualizations. This format is ideal for step-by-step exploration, explanations, and interactive data analysis.

# What does it do?

- Downloads pre-saved Warriors game data.
- Loads and processes the data using pandas.
- Filters games where the Warriors played against the Raptors (home and away).
- Calculates and prints the average `PLUS_MINUS` for both home and away games.
- Visualizes the `PLUS_MINUS` over time for both scenarios.

# What does it show?

This analysis helps compare the Warriors' performance against the Raptors when playing at home versus away, using the `PLUS_MINUS` statistic as a measure. The included plot provides a visual comparison of these performances over time.

---

Feel free to use either the Python script or the Jupyter Notebook, depending on your workflow preference!
