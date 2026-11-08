"""
Megha Nilesh Varma, Sandy Kwong
CSE 163 AB
Final Project

DOCUMENT!!!
"""

# import libraries
import pandas as pd

# methods
def merge_q1(diabetes: pd.DataFrame, insurance: pd.DataFrame) -> pd.DataFrame:
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

def merge_q2(poverty: pd.DataFrame, insurance: pd.DataFrame) -> pd.DataFrame:
    """
    DOCUMENT!!!
    """
    race_mapping = {
        'White': 'White',
        'Black': 'African-American / Black',
        'Hispanic': 'Hispanic / Latino',
        'American Indian or Alaska Native':
            'American Indian / Alaska Native',
        'Multiple Races': 'Other / Multiple Races'
    }

    poverty = poverty.copy()

    poverty['Race / Ethnicity'] = (poverty['Race / Ethnicity'].replace(race_mapping))

    merged = pd.merge(poverty,
        insurance,
        on=['Location', 'Race / Ethnicity'],
        how='inner')

    return merged