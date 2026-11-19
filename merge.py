"""
Megha Nilesh Varma, Sandy Kwong
CSE 163 AB
Final Project

Implements multiple methods to merge diabetes dataframe with
insurance and poverty dataframes.
"""

# import libraries
import pandas as pd


# methods
def q1(diabetes: pd.DataFrame, insurance: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a merged pandas dataframe with both diabetes and insurance data
    by race/ethnicity.
    """
    # change race strings in diabetes data
    race_mapping = {
        "Non-Hispanic White": "White",
        "Non-Hispanic Black": "African-American / Black",
        "Hispanic": "Hispanic / Latino"}

    # replace headers
    diabetes = diabetes.copy()
    diabetes['Stratification Group 1'] = (
        diabetes['Stratification Group 1'].replace(race_mapping))

    # merge diabetes and insurance data
    merged = pd.merge(diabetes,
                      insurance,
                      left_on=["Stratification Group 1"],
                      right_on=["Race / Ethnicity"])

    return merged


def q3(diabetes: pd.DataFrame, poverty: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a merged pandas dataframe with both diabetes and poverty data
    by race/ethnicity.
    """
    # change race strings in diabetes data
    race_mapping = {
        "Non-Hispanic White": "White",
        "Non-Hispanic Black": "Black",
        "Hispanic": "Hispanic"
    }

    # replace headers
    diabetes = diabetes.copy()
    diabetes['Stratification Group 1'] = (
        diabetes['Stratification Group 1'].replace(race_mapping)
    )

    # merge diabetes and poverty data
    merged = pd.merge(
        diabetes,
        poverty,
        left_on=["Location", "Stratification Group 1"],
        right_on=["Location", "Race/Ethnicity"]
    )

    return merged
