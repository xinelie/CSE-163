"""
Megha Nilesh Varma, Sandy Kwong
CSE 163 AB
Final Project
"""

# import libraries
import pandas as pd
import matplotlib.pyplot as plt

# methods


def main():
    # complete data processing here and call methods for visualization or analysis
    
    # read csv files
    diabetes_data = pd.read_csv("diabetes.csv")
    poverty_data = pd.read_csv("poverty.csv", skiprows=2)
    insurance_data = pd.read_csv("insurance.csv", skiprows=6)

    # filter diabetes data
    location_condition = diabetes_data['Location'] == 'Washington'
    diabetes_condition = diabetes_data['Short Indicator Text'].str.contains('Diabet')
    stratification1 = diabetes_data['Stratification 1'] == 'Race-Ethnicity'
    stratification2 = diabetes_data['Stratification 2'] == 'Race-Ethnicity'
    time_condition = diabetes_data['Year'] == 2021
    diabetes = diabetes_data[location_condition
                             & diabetes_condition 
                             & time_condition 
                             & (stratification1 | stratification2)]
    # print(diabetes['Stratification Group 1'])

    # filter poverty data
    poverty = poverty_data[poverty_data['Location'] == 'Washington']


if __name__ == "__main__":
    main()