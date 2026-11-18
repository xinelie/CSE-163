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
    # change race strings in diabetes data
    race_mapping = {
        "Non-Hispanic White": "White",
        "Non-Hispanic Black": "African-American / Black",
        "Hispanic": "Hispanic / Latino"}

    diabetes = diabetes.copy()
    diabetes['Stratification Group 1'] = (diabetes['Stratification Group 1'].replace(race_mapping))

    # merge diabetes and insurance data
    merged = pd.merge(diabetes,
                      insurance,
                      left_on=["Stratification Group 1"],
                      right_on=["Race / Ethnicity"])

    return merged


# q3 poverty and diabetes prevalence by race
def q3(diabetes: pd.DataFrame, poverty: pd.DataFrame) -> pd.DataFrame:
    """
    Standardizes racial/ethnic group labels in the cleaned diabetes dataset and
    merges with poverty data on both state ('Location') and race/ethnicity.
    """
    race_mapping = {
        "Non-Hispanic White": "White",
        "Non-Hispanic Black": "Black",
        "Hispanic": "Hispanic"
    }

    diabetes = diabetes.copy()
    diabetes['Stratification Group 1'] = (
        diabetes['Stratification Group 1'].replace(race_mapping)
    )

    merged = pd.merge(
        diabetes,
        poverty,
        left_on=["Location", "Stratification Group 1"],
        right_on=["Location", "Race/Ethnicity"]
    )

    return merged
