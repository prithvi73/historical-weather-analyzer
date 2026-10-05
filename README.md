# Historical Weather Data Analyzer 🌤️📊

A Python script that dynamically fetches the past week's weather metrics for Patna using the Open-Meteo API, processes the raw data with Pandas, and visualizes temperature trends with Matplotlib.

## Features
* **Dynamic Date Calculation:** Automatically computes a rolling 7-day window relative to execution time using `datetime` and `timedelta`.
* **API Integration:** Queries Open-Meteo's REST API for target coordinates (Patna: 25.59°N, 85.14°E) to retrieve daily maximum and minimum temperatures without requiring an API key.
* **Data Processing:** Parses raw JSON responses into a structured Pandas DataFrame, converts date strings to datetime objects, and calculates daily average temperatures.
* **Data Visualization:** Generates a clean multi-line plot displaying Max (red), Min (blue), and Average (green dashed) temperatures with formatted axes, grid lines, and legends.

## Tech Stack
* **Language:** Python
* **Libraries:** `requests`, `pandas`, `matplotlib`

## How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/prithvi73/Python-OpenMeteoAPI.git](https://github.com/prithvi73/Python-OpenMeteoAPI.git)
   cd Python-OpenMeteoAPI
