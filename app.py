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
data = []
current_balance = principal

for year in range(1, time + 1):
    current_balance = current_balance + (rate * current_balance)
    # Store in a dictionary to easily convert to DataFrame later
    data.append({"Year": year, "Balance": current_balance})

# Convert to DataFrame 
df = pd.DataFrame(data)
df.set_index("Year", inplace=True)

# 4. The Visualization
st.header("Projected Growth")
st.metric(label="Final Balance", value=f"${current_balance:,.2f}")


st.line_chart(df)
