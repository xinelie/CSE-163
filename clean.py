"""
Megha Nilesh Varma, Sandy Kwong
CSE 163 AB
Final Project

DOCUMENT!!!
"""

# import libraries
import pandas as pd

# methods
def clean_diabetes_data_q1(data: pd.DataFrame) -> pd.DataFrame:
    """
    DOCUMENT!!!
    """
    # masks
    location = data['Location'] == 'Washington'
    condition = data['Short Indicator Text'].str.contains('Diabet')
    rate = data['Data Type'].str.contains('Rate')
    year = data['Year'] == 2021
    stratification1 = data['Stratification 1'] == 'Race-Ethnicity'
    stratification2 = data['Stratification 2'] == 'Race-Ethnicity'

    # apply masks
    diabetes = data[location
                    & condition
                    & rate
                    & year
                    & (stratification1 | stratification2)]

    # additional cleaning
    diabetes['Data Value'] = pd.to_numeric(diabetes['Data Value'])
    diabetes = diabetes.dropna()

    return diabetes


def clean_insurance_data_q1(data: pd.DataFrame) -> pd.DataFrame:
    """
    DOCUMENT!!!
    """
    # masks
    data_type = data['Data Type'] == 'Percent'

    # apply masks
    insurance = data[data_type]

    # additional cleaning
    insurance['Data'] = pd.to_numeric(insurance['Data'])
    insurance['Data'] = insurance['Data'] * 100
    insurance = insurance.dropna()

    return insurance