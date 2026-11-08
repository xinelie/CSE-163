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

# methods
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


def visualize_q2_fig1(data: pd.DataFrame):
    """
    DOCUMENT!!!
    """
    fig = px.scatter(data,
                     x='Poverty Rate',
                     y='Data',
                     color='Race / Ethnicity',
                     symbol='Race / Ethnicity',
                     hover_name='Race / Ethnicity',
                     hover_data={'Poverty Rate': ':.2f',
                                 'Data': ':.2f'},
                     title='Poverty Rate vs. Uninsured Rate by Race in Washington',
                     labels={'Poverty Rate': 'Percentage Living in Poverty (%)',
                             'Data': 'Percentage Uninsured (%)',
                             'Race / Ethnicity': 'Race / Ethnicity'})

    fig.update_traces(marker={'size': 14})

    fig.update_layout(
        width=900,
        height=600,
        legend_title_text='Race / Ethnicity',
        template='plotly_white')

    fig.show()

    plt.tight_layout()
    plt.savefig('q2_1.jpg')
    plt.show()