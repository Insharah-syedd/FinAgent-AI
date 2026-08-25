import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

import streamlit as st
import pandas as pd
from ai_finance_intelligence.crew import AiFinanceIntelligence

# Streamlit Page Config
st.set_page_config(
    page_title="AI Finance Intelligence",
    page_icon="🤖",
    layout="wide"
)

st.title("💡 AI Finance Intelligence")
st.write(
    "Upload your financial CSV or enter your financial information manually "
    "to receive an AI-powered financial analysis."
)

st.divider()

# =========================================================
# INPUT METHOD SELECTION
# =========================================================

input_method = st.radio(
    "Choose how you want to provide your financial data:",
    ["Upload CSV", "Enter Manually"],
    horizontal=True
)

csv_data = ""
manual_data = {}

# =========================================================
# CSV INPUT SECTION
# =========================================================

if input_method == "Upload CSV":
    st.subheader("📁 Upload Financial CSV")

    uploaded_file = st.file_uploader(
        "Choose a CSV file",
        type=["csv"]
    )

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("✅ CSV uploaded successfully.")

            # Display Preview & Metrics
            st.subheader("Expense Data Preview")
            st.dataframe(df.head(20), use_container_width=True)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Rows", len(df))
            with col2:
                st.metric("Total Columns", len(df.columns))
            with col3:
                st.metric("Missing Values", int(df.isnull().sum().sum()))

            # Optimized token sending (Summary + First 50 rows)
            data_summary = f"Columns: {list(df.columns)}\nShape: {df.shape}\nMissing Values: {df.isnull().sum().to_dict()}\n"
            data_sample = df.head(50).to_csv(index=False)
            
            csv_data = f"{data_summary}\nData Sample:\n{data_sample}"

        except Exception as e:
            st.error("Unable to read this CSV file.")
            st.exception(e)

# =========================================================
# MANUAL INPUT SECTION
# =========================================================

else:
    st.subheader("✍️ Enter Financial Information")

    col1, col2 = st.columns(2)

    with col1:
        monthly_income = st.number_input(
            "Monthly Income ($)",
            min_value=0.0,
            value=100000.0,
            step=5000.0
        )

        monthly_expenses = st.number_input(
            "Monthly Expenses ($)",
            min_value=0.0,
            value=65000.0,
            step=5000.0
        )

        current_savings = st.number_input(
            "Current Savings ($)",
            min_value=0.0,
            value=150000.0,
            step=5000.0
        )

    with col2:
        expense_categories = st.text_input(
            "Expense Categories",
            value="Rent, Food, Transport, Shopping",
            placeholder="Rent, Food, Transport, Shopping"
        )

        financial_goal = st.text_input(
            "Financial Goal",
            value="Build an emergency fund",
            placeholder="Build an emergency fund"
        )

    manual_data = {
        "monthly_income": monthly_income,
        "monthly_expenses": monthly_expenses,
        "current_savings": current_savings,
        "expense_categories": expense_categories,
        "financial_goal": financial_goal
    }

# =========================================================
# TRIGGER ANALYSIS BUTTON
# =========================================================

st.divider()

if st.button("🚀 Analyze My Finances", type="primary", use_container_width=True):

    # CSV Validation & Execution
    if input_method == "Upload CSV":
        if not csv_data:
            st.warning("⚠️ Please upload a CSV file before starting the analysis.")
        else:
            inputs = {
                "csv_data": csv_data,
                "monthly_income": "",
                "monthly_expenses": "",
                "expense_categories": "",
                "current_savings": "",
                "financial_goal": ""
            }

            with st.spinner("🤖 AI Crew agents are analyzing your financial data..."):
                try:
                    result = AiFinanceIntelligence().crew().kickoff(inputs=inputs)
                    
                    st.success("✨ Financial analysis completed successfully!")
                    st.divider()
                    st.subheader("📋 Your AI Financial Analysis")
                    st.markdown(str(result))

                    # Download button for output
                    st.download_button(
                        label="📥 Download Report",
                        data=str(result),
                        file_name="financial_analysis_report.txt",
                        mime="text/plain"
                    )

                except Exception as e:
                    st.error("An error occurred during financial analysis.")
                    st.exception(e)

    # Manual Validation & Execution
    else:
        if not manual_data["expense_categories"]:
            st.warning("⚠️ Please enter your expense categories.")
        elif not manual_data["financial_goal"]:
            st.warning("⚠️ Please enter your financial goal.")
        else:
            inputs = {
                "monthly_income": str(manual_data["monthly_income"]),
                "monthly_expenses": str(manual_data["monthly_expenses"]),
                "expense_categories": manual_data["expense_categories"],
                "current_savings": str(manual_data["current_savings"]),
                "financial_goal": manual_data["financial_goal"],
                "csv_data": ""
            }

            with st.spinner("🤖 AI Crew agents are formulating your financial plan..."):
                try:
                    result = AiFinanceIntelligence().crew().kickoff(inputs=inputs)
                    
                    st.success("✨ Financial analysis completed successfully!")
                    st.divider()
                    st.subheader("🎯 Your Personalized Financial Plan")
                    st.markdown(str(result))

                    # Download button for output
                    st.download_button(
                        label="📥 Download Plan",
                        data=str(result),
                        file_name="financial_plan.txt",
                        mime="text/plain"
                    )

                except Exception as e:
                    st.error("An error occurred during financial analysis.")
                    st.exception(e)