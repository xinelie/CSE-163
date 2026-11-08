"""
Megha Nilesh Varma, Sandy Kwong
CSE 163 AB
Final Project

DOCUMENT!!!
"""

# import libraries
import pandas as pd

# import helper functions from other files
import clean
import merge
import visualize


def main():
    # complete data processing here and call methods for visualization or analysis
    
    # read csv files
    diabetes_data = pd.read_csv("diabetes.csv")
    poverty_data = pd.read_csv("poverty.csv", skiprows=2)
    insurance_data = pd.read_csv("insurance.csv", skiprows=6)

    # filter data
    diabetes = clean.diabetes_data_q1(diabetes_data)
    poverty = poverty_data[poverty_data['Location'] == 'Washington'].dropna()
    insurance = clean.insurance_data_q1(insurance_data)
    q2 = clean.diabetes_data_q2(diabetes_data)

    # merge data frames
    q1 = merge.q1(diabetes, insurance)

    # visualizations
    visualize.q1_fig1(q1) 
    visualize.q1_fig2(q1)
    visualize.q2_fig1(q2)
    visualize.q2_fig2(q2)


if __name__ == "__main__":
    main()