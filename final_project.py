"""
Megha Nilesh Varma, Sandy Kwong
CSE 163 AB
Final Project
"""

# import libraries
import pandas as pd
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
    insurance = data[data_type]
    # insurance = data[coverage & data_type]

    # additional cleaning
    insurance['Data'] = pd.to_numeric(insurance['Data'])
    insurance['Data'] = insurance['Data'] * 100

    return insurance


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


def visualize_q1_fig1(data: pd.DataFrame):
    """
    DOCUMENT!!!
    """
    # separate insured and uninsured data
    insurance = data.pivot_table(
        index='Race / Ethnicity',
        columns='Coverage Type',
        values='Data',
        aggfunc='first')

    # get diabetes prevalence for each race
    diabetes = data.groupby('Race / Ethnicity')['Data Value'].first()

    # calculate the proportional diabetes prevalence
    insured = diabetes * (insurance['Insured'] / 100)
    uninsured = diabetes * (insurance['Uninsured'] / 100)

    plt.figure(figsize=(10, 7))

    plt.bar(diabetes.index, insured, label="Insured")
    plt.bar(diabetes.index, uninsured, bottom=insured, label="Uninsured")

    plt.xlabel("Race / Ethnicity")
    plt.ylabel("Diabetes Prevalence (per 100)")
    plt.title("Diabetes Prevalence Vs. Insurance Status")

    plt.xticks(rotation=45)
    plt.legend(title="Insurance Status")
    plt.tight_layout()

    plt.savefig('q1_1.jpg')


def visualize_q1_fig2(data: pd.DataFrame):
    """
    DOCUMENT!!!
    """
    # separate insurance coverage categories
    insurance = data.pivot_table(
        index='Race / Ethnicity',
        columns='Coverage Type',
        values='Data',
        aggfunc='first')

    # remove insured and uninsured
    insurance = insurance.drop(columns=['Insured', 'Uninsured'])

    # normalize the remaining coverage percentages
    insurance = insurance.div(insurance.sum(axis=1), axis=0)

    # get diabetes prevalence for each race
    diabetes = data.groupby('Race / Ethnicity')['Data Value'].first() * 100

    # calculate proportional diabetes prevalence
    insurance = insurance / 100

    plt.figure(figsize=(10, 8))

    # create stacked bars
    bottom = 0

    for coverage in insurance.columns:
        proportion = diabetes * insurance[coverage]

        plt.bar(
            diabetes.index,
            proportion,
            bottom=bottom,
            label=coverage)

        bottom = bottom + proportion

    plt.xlabel("Race / Ethnicity")
    plt.ylabel("Diabetes Prevalence (per 100)")
    plt.title("Diabetes Prevalence Vs. Insurance Coverage Type")

    plt.xticks(rotation=45)
    plt.legend(title="Insurance Coverage Type")
    plt.tight_layout()

    plt.savefig('q1_2.jpg')
    plt.show()


def main():
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
    visualize_q1_fig1(q1) 
    visualize_q1_fig2(q1)


if __name__ == "__main__":
    main()