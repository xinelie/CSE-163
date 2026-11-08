"""
Megha Nilesh Varma, Sandy Kwong
CSE 163 AB
Final Project

DOCUMENT!!!
"""

# import libraries
import pandas as pd

# methods
def q1(diabetes: pd.DataFrame, insurance: pd.DataFrame) -> pd.DataFrame:
    """
    DOCUMENT!!!
    """
    race_mapping = {
        "Non-Hispanic White": "White",
        "Non-Hispanic Black": "African-American / Black",
        "Hispanic": "Hispanic / Latino"}

    diabetes = diabetes.copy()

    diabetes['Stratification Group 1'] = (diabetes['Stratification Group 1'].replace(race_mapping))

    merged = pd.merge(diabetes,
                      insurance,
                      left_on=["Stratification Group 1"],
                      right_on=["Race / Ethnicity"])

    return merged
