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
    Plots a stacked bar chart of proportional diabetes prevalence by insured and
uninsured status across racial/ethnic groups in Washington State.

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

    # create dataframe to have one insured and uninsured value per race category
    proportions = pd.DataFrame({'Race / Ethnicity': diabetes.index,
                                'Insured': insured.values,
                                'Uninsured': uninsured.values})

    # create stacked bar chart
    fig = px.bar(proportions,
                 x='Race / Ethnicity',
                 y=['Insured', 'Uninsured'],
                 barmode='stack',
                 title='Diabetes Prevalence vs. Insurance Status',
                 labels={'value': 'Diabetes Prevalence (per 100 people)',
                         'variable': 'Insurance Status'})

    fig.write_html("q1_1.html")
    fig.show()


def q1_fig2(data: pd.DataFrame):
    """
    Plots a stacked bar chart breaking down proportional diabetes prevalence by
    health insurance coverage types across racial/ethnic groups in Washington.
    """
    # group insurance data by race and coverage type
    insurance = data.copy()
    insurance = insurance.groupby(['Race / Ethnicity', 'Coverage Type'])['Data'].first()

    # remove insured and uninsured categories to only consider types of insurance
    insurance = insurance.drop(labels=['Insured', 'Uninsured'],
                               level='Coverage Type')

    # get diabetes prevalence for each race
    diabetes = data.groupby('Race / Ethnicity')['Data Value'].first()

    # calculate proportional diabetes prevalence
    proportions = insurance / 100
    proportions = proportions * diabetes / 2

    # reset index to plot without multi index
    proportions = proportions.reset_index(name='Diabetes Prevalence')

    # create stacked bar chart
    fig = px.bar(
        proportions,
        x='Race / Ethnicity',
        y='Diabetes Prevalence',
        color='Coverage Type',
        barmode='stack',
        title='Diabetes Prevalence vs. Insurance Coverage Type',
        labels={'value': 'Diabetes Prevalence (per 100 people)',
                'variable': 'Coverage Type'})
    
    fig.write_html("q1_2.html")
    fig.show()


def q2_fig1(data: pd.DataFrame):
    """
    Plots a grouped bar chart comparing 2021 diabetes prevalence across racial/ethnic
    groups in six selected U.S. states.
    """
    # filter states
    states = ['Washington','California','Texas', 'New York','Florida','Illinois']
    data = data[data['Location'].isin(states)]

    # create grouped bar chart
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

def q2_fig2(data: pd.DataFrame):
    """
    Plots a scatter plot showing 2021 diabetes prevalence by race and ethnicity
    across all U.S. states in the dataset.
    """
    # create scatter plot
    fig = px.scatter(data,
                     x='Location',
                     y='Data Value',
                     color='Stratification Group 1',
                     symbol='Stratification Group 1',
                     title='Diabetes Prevalence Vs. Race/Ethnicity Based on State',
                     labels={'Race / Ethnicity': 'Race / Ethnicity',
                             'Data Value': 'Diabetes Prevalence (per 100 people)',
                             'Year': 'Year'})

    fig.update_layout(width=900,
                      height=600,
                      template='plotly_white',
                      xaxis_title='State')

    fig.write_html("q2_1.html")
    fig.show()

# q3
def q3_fig1(data: pd.DataFrame):
    """
    Creates a grouped bar chart comparing diabetes prevalence (per 100
    people) and poverty rate (%) across racial and ethnic groups in Washington.
    """
    fig = px.bar(
        data,
        x='Race/Ethnicity',
        y=['Data Value', 'Poverty Rate'],
        barmode='group',
        title='Diabetes Prevalence vs. Poverty Rate by Race/Ethnicity in Washington (2021)',
        labels={
            'Race/Ethnicity': 'Race / Ethnicity',
            'value': 'Percentage / Rate (per 100 people)',
            'variable': 'Metric'
        }
    )

    # legend
    newnames = {
        'Data Value': 'Diabetes Prevalence (per 100)',
        'Poverty Rate': 'Poverty Rate (%)'
    }
    fig.for_each_trace(lambda t: t.update(name=newnames.get(t.name, t.name)))

    fig.update_layout(
        width=900,
        height=600,
        template='plotly_white',
        xaxis_title='Race / Ethnicity',
        yaxis_title='Rate / Percentage'
    )

    fig.write_html("q3_1.html")
    fig.show()


def q3_fig2(data: pd.DataFrame):
    """
    Creates and saves a scatter plot comparing poverty rate (%) against diabetes
    prevalence (per 100 people) across racial and ethnic groups in Washington.
    """
    fig = px.scatter(
        data,
        x='Poverty Rate',
        y='Data Value',
        color='Race/Ethnicity',
        symbol='Race/Ethnicity',
        text='Race/Ethnicity',
        title='Association Between Poverty Rate and Diabetes Prevalence in Washington (2021)',
        labels={
            'Poverty Rate': 'Poverty Rate (%)',
            'Data Value': 'Diabetes Prevalence (per 100 people)',
            'Race/Ethnicity': 'Race / Ethnicity'
        }
    )

    fig.update_traces(textposition='top center', marker=dict(size=12))
    fig.update_layout(
        width=900,
        height=600,
        template='plotly_white'
    )

    fig.write_html("q3_2.html")
    fig.show()