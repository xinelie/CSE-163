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
    diabetes = clean.clean_diabetes_data_q1(diabetes_data)
    poverty = poverty_data[poverty_data['Location'] == 'Washington'].dropna()
    insurance = clean.clean_insurance_data_q1(insurance_data)

    # merge data frames
    q1 = merge.merge_q1(diabetes, insurance)
    # q2 = merge.merge_q2(poverty, insurance)

    # visualizations
    visualize.visualize_q1_fig1(q1) 
    visualize.visualize_q1_fig2(q1)


if __name__ == "__main__":
    main()