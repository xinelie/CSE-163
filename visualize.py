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
    # group insurance data by race and coverage type
    insurance = data.groupby(['Race / Ethnicity', 'Coverage Type'])['Data'].first()

    # get diabetes prevalence for each race
    diabetes = data.groupby('Race / Ethnicity')['Data Value'].first()

    # get insured and uninsured values
    insured = insurance.loc[(slice(None), 'Insured')]
    uninsured = insurance.loc[(slice(None), 'Uninsured')]

    # calculate proportional diabetes prevalence
    insured = diabetes * (insured / 100)
    uninsured = diabetes * (uninsured / 100)

    # create dataframe to cleanly plot
    proportions = pd.DataFrame({'Race / Ethnicity': diabetes.index,
                                'Insured': insured.values,
                                'Uninsured': uninsured.values})

    # create stacked bar chart
    fig = px.bar(proportions,
                 x='Race / Ethnicity',
                 y=['Insured', 'Uninsured'],
                 barmode='stack',
                 title='Diabetes Prevalence vs. Insurance Status',
                 labels={'value': 'Diabetes Prevalence (per 100)',
                         'variable': 'Insurance Status'})

    fig.show()


def q1_fig2(data: pd.DataFrame):
    # group insurance data by race and coverage type
    insurance = data.groupby(['Race / Ethnicity', 'Coverage Type'])['Data'].first()

    # remove insured and uninsured
    insurance = insurance.drop(labels=['Insured', 'Uninsured'],
                               level='Coverage Type')

    # get diabetes prevalence for each race
    diabetes = data.groupby('Race / Ethnicity')['Data Value'].first()

    # calculate proportional diabetes prevalence
    proportions = insurance / 100
    proportions = proportions * diabetes / 2

    proportions = proportions.reset_index(name='Diabetes Prevalence')

    fig = px.bar(
        proportions,
        x='Race / Ethnicity',
        y='Diabetes Prevalence',
        color='Coverage Type',
        barmode='stack',
        title='Diabetes Prevalence vs. Insurance Coverage Type')

    fig.show()


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
