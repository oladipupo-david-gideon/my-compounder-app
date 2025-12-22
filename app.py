import streamlit as st
import pandas as pd

# 1. Title & Description
st.title('The Compounder')
st.write("Experiment with different rates to see how money grows over time.")

# 2. Sidebar Inputs (Moves the sliders to the left side)
st.sidebar.header("Settings")
principal = st.sidebar.slider("Initial Investment ($)", 0, 10000, 1000)
rate = st.sidebar.slider("Interest Rate (Decimal)", 0.0, 0.15, 0.05)
time = st.sidebar.slider("Time (Years)", 1, 50, 20)

# 3. The Logic Engine
values = []
current_balance = principal

for i in range(time):
    current_balance = current_balance + (rate * current_balance)
    values.append(current_balance)

# 4. The Visualization
st.header("Projected Growth")

# Display the final amount big and bold
st.metric(label="Final Balance", value=f"${current_balance:,.2f}")

# The Chart
st.line_chart(values)