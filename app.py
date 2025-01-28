# These three bring in streamlit, plotting software, and our favorite - numpy
import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Simple Financial Planner")

st.title("Simple Financial Planner for Students")
st.subheader("Plan your retirement savings with a basic income and expense tracker.")

# Section 1: Monthly Income
st.header("Monthly Income")
annual_salary = st.number_input("Enter your annual salary ($):", min_value=0.0, step=1000.0, value=50000.0)
tax_rate = st.slider("Select your tax rate (%):", min_value=0.0, max_value=50.0, value=20.0, step=1.0)

# Calculate take-home monthly income
tax_rate = tax_rate / 100
monthly_income = (annual_salary * (1 - tax_rate)) / 12
st.write(f"Your monthly take-home income is: **${monthly_income:.2f}**")

# Section 2: Monthly Expenses
st.header("Monthly Expenses")
rent = st.number_input("Monthly Rent ($):", min_value=0.0, step=50.0, value=1000.0)
food = st.number_input("Monthly Food Budget ($):", min_value=0.0, step=50.0, value=500.0)
transport = st.number_input("Monthly Transport Costs ($):", min_value=0.0, step=50.0, value=200.0)

total_expenses = rent + food + transport
monthly_savings = max(monthly_income - total_expenses, 0)

st.write(f"Your total monthly expenses are: **${total_expenses:.2f}**")
st.write(f"Your estimated monthly savings are: **${monthly_savings:.2f}**")

# Section 3: Simple Simulation
st.header("Retirement Savings Simulation")
st.subheader("Estimate your retirement savings based on monthly contributions and expected returns.")

current_savings = st.number_input("Current Savings ($):", min_value=0.0, step=1000.0, value=10000.0)
monthly_contribution = st.slider(
    "Set your monthly contribution to savings ($):",
    min_value=0.0,
    max_value=monthly_savings,
    value=min(500.0, monthly_savings),
    step=50.0
)
annual_return = st.slider("Expected Annual Return on Investments (%):", min_value=0.0, max_value=15.0, value=8.0) / 100
years_to_retirement = st.slider("Years until retirement:", min_value=1, max_value=50, value=30, step=1)

# Projected savings calculation
total_months = years_to_retirement * 12
monthly_return = (1 + annual_return) ** (1 / 12) - 1
future_savings = current_savings * (1 + monthly_return) ** total_months
for month in range(total_months):
    future_savings += monthly_contribution * (1 + monthly_return) ** (total_months - month)

st.write(f"Projected savings at retirement: **${future_savings:,.2f}**")

# Visualization
st.subheader("Savings Over Time")
savings_over_time = [current_savings]
for month in range(1, total_months + 1):
    savings_over_time.append(
        savings_over_time[-1] * (1 + monthly_return) + monthly_contribution
    )
fig = go.Figure()
fig.add_trace(go.Scatter(x=list(range(total_months + 1)), y=savings_over_time, mode='lines', name='Savings'))
fig.update_layout(title="Projected Savings Over Time", xaxis_title="Months", yaxis_title="Total Savings ($)")
st.plotly_chart(fig, use_container_width=True)

# Suggested Enhancements & Requirements
st.header("Project Minimums")
st.markdown("""
From this template, groups should expand their retirement model. For full credit, at least three new variables (e.g., expenses/savings), 1-3 new visualizations, and a new dynamic function (e.g., a slider) should be included.
Groups are also encouraged to use external resources, or create their own retirement model from scratch. Ultimately, we will host these on [Streamlit's Cloud](https://streamlit.io/cloud).
""")

st.header("Suggested Enhancements for Students")
st.markdown("""
1. Add more expense categories (e.g., entertainment, healthcare, education).
2. Include an option for salary growth over time (e.g., annual raises or promotions).
3. Add debt repayment planning (e.g., loan balance and interest rate).
4. Implement advanced simulations (e.g., Monte Carlo scenarios).
5. Include inflation adjustments for expenses and savings goals.
""")
