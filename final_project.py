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
    Scatter plot to show the relationship between uninsured rates and diabetes prevalence.
    """
    uninsured = data[data['Coverage Type'] == 'Uninsured']

    graph = sns.relplot(
        data=uninsured,
        x='Data',
        y='Data Value',
        hue='Race / Ethnicity',
        style='Race / Ethnicity',
        s=250
)

    sns.move_legend(graph, "upper right", bbox_to_anchor=(0.975, 0.9))

    plt.xlabel("Percentage of Uninsured (%)")
    plt.ylabel("Diabetes Prevalence Rate (Per 100)")
    plt.title("Diabetes Prevalence Rate vs. Percentage of Uninsured by Race")

    # plt.xticks([])
    plt.ylim(6, 15)
    plt.tight_layout()

    plt.savefig("q1_1.jpg")


def visualize_q1_fig2(data: pd.DataFrame):
    # Separate insured and uninsured data
    insurance = data.pivot_table(
        index='Race / Ethnicity',
        columns='Coverage Type',
        values='Data',
        aggfunc='first')

    # Get diabetes prevalence for each race
    diabetes = data.groupby('Race / Ethnicity')['Data Value'].first()

    # Calculate the proportional diabetes prevalence
    insured = diabetes * (insurance['Insured'] / 100)
    uninsured = diabetes * (insurance['Uninsured'] / 100)

    plt.figure(figsize=(10, 6))

    plt.bar(diabetes.index, insured, label="Insured")
    plt.bar(diabetes.index, uninsured, bottom=insured, label="Uninsured")

    plt.xlabel("Race / Ethnicity")
    plt.ylabel("Diabetes Prevalence (per 100)")
    plt.title("Diabetes Prevalence Divided by Insurance Status")

    plt.xticks(rotation=45)
    plt.legend(title="Insurance Status")
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