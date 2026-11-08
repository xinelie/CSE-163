"""
Megha Nilesh Varma, Sandy Kwong
CSE 163 AB
Final Project
"""

# import libraries
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

# methods
def clean_diabetes_data(data: pd.DataFrame) -> pd.DataFrame:
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


def clean_insurance_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    DOCUMENT!!!
    """
    # masks
    coverage = data['Coverage Type'] == 'Uninsured'
    data_type = data['Data Type'] == 'Percent'

    # apply masks
    insurance = data[coverage & data_type]
    #insurance = data[data_type]

    return insurance


def merge_q1(diabetes: pd.DataFrame, insurance: pd.DataFrame) -> pd.DataFrame:
    """
    DOCUMENT!!!
    """
    race_mapping = {
        "Non-Hispanic White": "White",
        "Non-Hispanic Black": "African-American / Black",
        "Hispanic": "Hispanic / Latino"}

    diabetes['Stratification Group 1'] = (diabetes['Stratification Group 1'].replace(race_mapping))

    merged = pd.merge(diabetes,
                      insurance,
                      left_on=["Stratification Group 1"],
                      right_on=["Race / Ethnicity"])

    return merged


def visualize_q1(data: pd.DataFrame): 
    """
    How is health insurance coverage by race associated with the
    burden of diabetes across Washington State?
    """
    sns.barplot(
        data=data,
        x='Coverage Type',
        y='Data Value',
        hue='Race / Ethnicity',
    )

    plt.xlabel("Percentage of Uninsured (%)")
    plt.ylabel("Percentage of Population (%)")
    plt.title("Health Insurance Coverage Type by Race in Washington")

    plt.ylim(6, 20)
    plt.tight_layout()

    plt.show()

def main():
    """
    plan:
    races: non-hispanic black, non-hispanic white, hispanic, and non-hispanic other races
        the other data comes with additional races. 
    data types: estimated cases (in thousands), rate (per 100)
        we will need to work with these cases separately. we can probably pick just one. 
    """
    # complete data processing here and call methods for visualization or analysis
    
    # read csv files
    diabetes_data = pd.read_csv("diabetes.csv")
    poverty_data = pd.read_csv("poverty.csv", skiprows=2)
    insurance_data = pd.read_csv("insurance.csv", skiprows=6)

    # filter data
    diabetes = clean_diabetes_data(diabetes_data)
    poverty = poverty_data[poverty_data['Location'] == 'Washington']
    insurance = clean_insurance_data(insurance_data)

    # merge data frames
    q1 = merge_q1(diabetes, insurance)

    # visualizations
    visualize_q1(q1)

if __name__ == "__main__":
    main()