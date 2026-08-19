import streamlit as st
import pandas as pd

from ai_finance_intelligence.crew import AiFinanceIntelligence


st.set_page_config(
    page_title="AI Finance Intelligence",
    page_icon="AI",
    layout="wide"
)

st.title("AI Finance Intelligence")
st.write(
    "Upload your financial CSV or enter your financial information manually "
    "to receive an AI-powered financial analysis."
)

st.divider()

# =========================================================
# INPUT METHOD
# =========================================================

input_method = st.radio(
    "Choose how you want to provide your financial data:",
    ["Upload CSV", "Enter Manually"],
    horizontal=True
)

csv_data = ""
manual_data = {}

# =========================================================
# CSV INPUT
# =========================================================

if input_method == "Upload CSV":

    st.subheader("Upload Financial CSV")

    uploaded_file = st.file_uploader(
        "Choose a CSV file",
        type=["csv"]
    )

    if uploaded_file is not None:

        try:
            df = pd.read_csv(uploaded_file)

            st.success("CSV uploaded successfully.")

            st.subheader("Expense Data Preview")

            st.dataframe(
                df,
                use_container_width=True
            )

            st.subheader("Dataset Summary")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Rows", len(df))

            with col2:
                st.metric("Columns", len(df.columns))

            with col3:
                st.metric(
                    "Missing Values",
                    int(df.isnull().sum().sum())
                )

            csv_data = df.to_string(index=False)

        except Exception as e:

            st.error("Unable to read this CSV file.")
            st.exception(e)


# =========================================================
# MANUAL INPUT
# =========================================================

else:

    st.subheader("Enter Financial Information")

    col1, col2 = st.columns(2)

    with col1:

        monthly_income = st.number_input(
            "Monthly Income",
            min_value=0.0,
            value=100000.0,
            step=5000.0
        )

        monthly_expenses = st.number_input(
            "Monthly Expenses",
            min_value=0.0,
            value=65000.0,
            step=5000.0
        )

        current_savings = st.number_input(
            "Current Savings",
            min_value=0.0,
            value=150000.0,
            step=5000.0
        )

    with col2:

        expense_categories = st.text_input(
            "Expense Categories",
            placeholder="Rent, Food, Transport, Shopping"
        )

        financial_goal = st.text_input(
            "Financial Goal",
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
# ANALYZE BUTTON
# =========================================================

st.divider()

if st.button(
    "Analyze My Finances",
    type="primary",
    use_container_width=True
):

    # -----------------------------
    # CSV validation
    # -----------------------------

    if input_method == "Upload CSV":

        if not csv_data:

            st.warning(
                "Please upload a CSV file before starting the analysis."
            )

        else:

            inputs = {
                "csv_data": csv_data,
                "monthly_income": "",
                "monthly_expenses": "",
                "expense_categories": "",
                "current_savings": "",
                "financial_goal": ""
            }

            with st.spinner(
                "AI agents are analyzing your financial data..."
            ):

                try:

                    result = AiFinanceIntelligence().crew().kickoff(
                        inputs=inputs
                    )

                    st.success(
                        "Financial analysis completed successfully."
                    )

                    st.divider()

                    st.subheader(
                        "Your AI Financial Analysis"
                    )

                    st.markdown(str(result))

                except Exception as e:

                    st.error(
                        "An error occurred during financial analysis."
                    )

                    st.exception(e)

    # -----------------------------
    # Manual validation
    # -----------------------------

    else:

        if not manual_data["expense_categories"]:

            st.warning(
                "Please enter your expense categories."
            )

        elif not manual_data["financial_goal"]:

            st.warning(
                "Please enter your financial goal."
            )

        else:

            inputs = {
                "monthly_income": str(
                    manual_data["monthly_income"]
                ),
                "monthly_expenses": str(
                    manual_data["monthly_expenses"]
                ),
                "expense_categories": manual_data[
                    "expense_categories"
                ],
                "current_savings": str(
                    manual_data["current_savings"]
                ),
                "financial_goal": manual_data[
                    "financial_goal"
                ],
                "csv_data": ""
            }

            with st.spinner(
                "AI agents are analyzing your financial information..."
            ):

                try:

                    result = AiFinanceIntelligence().crew().kickoff(
                        inputs=inputs
                    )

                    st.success(
                        "Financial analysis completed successfully."
                    )

                    st.divider()

                    st.subheader(
                        "Your Personalized Financial Plan"
                    )

                    st.markdown(str(result))

                except Exception as e:

                    st.error(
                        "An error occurred during financial analysis."
                    )

                    st.exception(e)