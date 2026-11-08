"""
Megha Nilesh Varma, Sandy Kwong
CSE 163 AB
Final Project

DOCUMENT!!!
"""

# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

sns.set_theme()

# methods
def q1_fig1(data: pd.DataFrame):
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


def q1_fig2(data: pd.DataFrame):
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

    # get diabetes prevalence for each race
    diabetes = data.groupby('Race / Ethnicity')['Data Value'].first()

    # calculate proportional diabetes prevalence
    insurance = insurance / 100

    plt.figure(figsize=(10, 8))

    # create stacked bars
    bottom = 0

    for coverage in insurance.columns:
        proportion = diabetes * insurance[coverage] / 2

        plt.bar(diabetes.index,
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


def q2_fig1(data: pd.DataFrame):
    """
    DOCUMENT!!!!
    """
    fig = px.bar(data,
                 x='Stratification Group 1',
                 y='Data Value',
                 color='Location',
                 barmode='group',
                 title='Diabetes Prevalence Vs. Race/Ethnicity Based on State',
                 labels={'Race / Ethnicity': 'Race / Ethnicity',
                         'Data Value': 'Diabetes Prevalence (per 100 people)',
                         'Year': 'Year'})

    fig.update_layout(width=900,
                      height=600,
                      template='plotly_white',
                      xaxis_title='Race / Ethnicity')

    fig.write_html("q2_1.html")
    fig.show()
    