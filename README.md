# The Compounder

A small interactive calculator that shows how money grows with compound interest, built with Python and Streamlit. Adjust the starting amount, interest rate, and number of years, and the app shows the final balance and a growth chart.

**[View the live app](https://oladipupo-david-compounder-app.streamlit.app/)** (if it has been idle, it may take a few seconds to wake up)

> Built with AI assistance. I led the design and feature decisions, then reviewed and tested the code.

## What it does

Three sliders in the sidebar control the inputs:

| Input | Range | Default |
|---|---|---|
| Initial investment | $0 to $10,000 (steps of $1,000) | $1,000 |
| Interest rate | 0.00 to 0.15 (as a decimal, so 0.05 is 5%) | 0.05 |
| Time | 1 to 50 years | 20 |

The app then shows:
* The **final balance** after the chosen number of years
* A **line chart** of the balance for each year

With the defaults ($1,000 at 5% for 20 years), the final balance is **$2,653.30**.

## How it works

The code compounds the balance once per year. For each year, it adds interest to the current balance and stores the result in a list. The list becomes a pandas DataFrame, which Streamlit plots as a line chart. The result is the same as the standard formula: starting amount x (1 + rate) ^ years. Streamlit re-runs the script whenever a slider changes, so the results update as you move it.

## Tech stack

* **Python:** the calculation
* **Streamlit:** the web interface and sliders
* **pandas:** holds the yearly balances for the chart

## Run locally

```bash
git clone https://github.com/oladipupo-david-gideon/my-compounder-app.git
cd my-compounder-app
pip install -r requirements.txt
streamlit run app.py
```

If `streamlit` isn't recognized on Windows, run `python -m streamlit run app.py` instead.

## Limitations

* Interest compounds once per year only. There is no monthly compounding.
* There are no recurring deposits, and no inflation or tax adjustments.
* The sliders cap the starting amount at $10,000 and the rate at 15%.

## Disclaimer

This is an educational tool, not financial advice.
