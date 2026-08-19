#!/usr/bin/env python

import sys
import warnings

from ai_finance_intelligence.crew import AiFinanceIntelligence

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the AI Finance Intelligence crew.
    """

    print("\n" + "=" * 60)
    print("AI FINANCE INTELLIGENCE")
    print("=" * 60)

    monthly_income = input("Monthly income: ")

    monthly_expenses = input("Monthly expenses: ")

    expense_categories = input(
        "Expense categories "
        "(example: Rent, Food, Transport, Shopping): "
    )

    current_savings = input("Current savings: ")

    financial_goal = input(
        "Financial goal "
        "(example: Emergency fund, Education, House): "
    )

    inputs = {
        "monthly_income": monthly_income,
        "monthly_expenses": monthly_expenses,
        "expense_categories": expense_categories,
        "current_savings": current_savings,
        "financial_goal": financial_goal,
    }

    try:
        result = AiFinanceIntelligence().crew().kickoff(inputs=inputs)

        print("\n" + "=" * 60)
        print("FINAL FINANCIAL PLAN")
        print("=" * 60)
        print(result)
        print("=" * 60)

    except Exception as e:
        raise Exception(
            f"An error occurred while running the crew: {e}"
        )


def train():
    """
    Train the crew.
    """

    inputs = {
        "monthly_income": "100000",
        "monthly_expenses": "65000",
        "expense_categories": "Rent, Food, Transport, Shopping",
        "current_savings": "150000",
        "financial_goal": "Build an emergency fund",
    }

    try:
        AiFinanceIntelligence().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )

    except Exception as e:
        raise Exception(
            f"An error occurred while training the crew: {e}"
        )


def replay():
    """
    Replay the crew execution from a specific task.
    """

    try:
        AiFinanceIntelligence().crew().replay(
            task_id=sys.argv[1]
        )

    except Exception as e:
        raise Exception(
            f"An error occurred while replaying the crew: {e}"
        )


def test():
    """
    Test the crew execution.
    """

    inputs = {
        "monthly_income": "100000",
        "monthly_expenses": "65000",
        "expense_categories": "Rent, Food, Transport, Shopping",
        "current_savings": "150000",
        "financial_goal": "Build an emergency fund",
    }

    try:
        AiFinanceIntelligence().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs
        )

    except Exception as e:
        raise Exception(
            f"An error occurred while testing the crew: {e}"
        )


def run_with_trigger():
    """
    Run the crew with a trigger payload.
    """

    import json

    if len(sys.argv) < 2:
        raise Exception(
            "No trigger payload provided. "
            "Please provide JSON payload as argument."
        )

    try:
        trigger_payload = json.loads(sys.argv[1])

    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "monthly_income": "",
        "monthly_expenses": "",
        "expense_categories": "",
        "current_savings": "",
        "financial_goal": "",
    }

    try:
        result = AiFinanceIntelligence().crew().kickoff(
            inputs=inputs
        )

        return result

    except Exception as e:
        raise Exception(
            f"An error occurred while running the crew "
            f"with trigger: {e}"
        )