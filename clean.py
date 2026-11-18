"""
Megha Nilesh Varma, Sandy Kwong
CSE 163 AB
Final Project

Cleaning and filtering data for visualizations
"""

# import libraries
import pandas as pd

# methods
def diabetes_data_q1(data: pd.DataFrame) -> pd.DataFrame:
    """
    
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


def insurance_data_q1(data: pd.DataFrame) -> pd.DataFrame:
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

def diabetes_data_q2(data: pd.DataFrame) -> pd.DataFrame:
    """
    DOCUMENT!!!
    """
    # masks
    condition = data['Short Indicator Text'].str.contains('Diabet')
    rate = data['Data Type'].str.contains('Rate')
    year = data['Year'] == 2021
    stratification1 = data['Stratification 1'] == 'Race-Ethnicity'
    stratification2 = data['Stratification 2'] == 'Race-Ethnicity'

    # apply masks
    diabetes = data[condition
                    & rate
                    & year
                    & (stratification1 | stratification2)]

    # additional cleaning
    diabetes['Data Value'] = pd.to_numeric(diabetes['Data Value'])
    diabetes = diabetes.dropna()

    return diabetes


def poverty_data_q3_just_Wa(data: pd.DataFrame) -> pd.DataFrame:
    """
    DOCUMENT!!!
    """
    # masks
    location = data['Location'] == 'Washington'
    poverty = data[location].drop(columns=['Location', 'Total'], errors='ignore')
    # turning columns into rows
    poverty = poverty.T.reset_index()
    poverty.columns = ['Race/Ethnicity', 'Poverty Rate']
    # additional Cleaning
    poverty['Poverty Rate'] = pd.to_numeric(poverty['Poverty Rate'], errors='coerce')
    poverty['Poverty Rate'] = poverty['Poverty Rate'] * 100 # converting to percentage

    poverty = poverty.dropna() # ensuring no null values in the data frame

    return poverty

def poverty_data_q3_multistate(data: pd.DataFrame) -> pd.DataFrame:
    """
    DOCUMENT!!!
    """
    poverty_all = data[data['Location'] != 'United States'].copy()
    poverty_all = poverty_all.drop(columns=['Total'], errors='ignore')

    # turning columns into rows
    poverty_all = poverty_all.set_index('Location').stack().reset_index()
    poverty_all.columns = ['Location', 'Race/Ethnicity', 'Poverty Rate']
    # additional Cleaning
    poverty_all['Poverty Rate'] = pd.to_numeric(poverty_all['Poverty Rate'], errors='coerce')
    poverty_all['Poverty Rate'] = poverty_all['Poverty Rate'] * 100 # converting to percentage

    poverty_all = poverty_all.dropna() # ensuring no null values in the data frame

    return poverty_all