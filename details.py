"""
Megha Nilesh Varma, Sandy Kwong
CSE 163 AB
Final Project

Looks at dataset dimensions, missing data statistics, 7-number quantitative
summaries, and categorical value counts across the CDC diabetes, SHADAC
insurance, and KFF poverty datasets.
"""

import pandas as pd


def check_dimensions(name: str, df: pd.DataFrame):
    """
    Prints the number of rows, number of columns, and column names for df.
    """
    print("=" * 60)
    print("DATASET SIZE:", name)
    print("Rows:", df.shape[0], "Columns:", df.shape[1])
    print("Column names:", list(df.columns))


def check_missing_values(name: str, df: pd.DataFrame):
    """
    Prints missing value counts and missing percentages for each column in df.
    """
    print("\nMISSING DATA:", name)
    missing_count = df.isna().sum()
    missing_percent = (df.isna().mean() * 100).round(2)

    missing_summary = pd.DataFrame({
        'Missing Count': missing_count,
        'Missing %': missing_percent
    })
    print(missing_summary)


def check_quantitative(name: str, df: pd.DataFrame, quant_cols: list[str]):
    """
    Prints the 7-number summary (mean, std, min, 25%, 50%, 75%, max) for each
    quantitative variable of interest.
    """
    print("\nQUANTITATIVE VARIABLES (7-NUMBER SUMMARY):", name)
    for col in quant_cols:
        numeric_col = pd.to_numeric(df[col], errors='coerce')
        print("\n---", col, "---")
        print(numeric_col.describe())


def check_categorical(name: str, df: pd.DataFrame, cat_cols: list[str]):
    """
    Prints all unique values and their counts for each categorical variable.
    """
    print("\nCATEGORICAL VARIABLES (UNIQUE VALUES & COUNTS):", name)
    for col in cat_cols:
        print("\n---", col, "(Total unique:", df[col].nunique(), ") ---")
        print(df[col].value_counts(dropna=False))


def main():
    diabetes = pd.read_csv('diabetes.csv')
    insurance = pd.read_csv('insurance.csv', skiprows=6)
    poverty = pd.read_csv('poverty.csv', skiprows=2)

    # 1. CDC Diabetes dataset
    check_dimensions('CDC Diabetes', diabetes)
    check_missing_values('CDC Diabetes', diabetes)
    check_quantitative('CDC Diabetes', diabetes, ['Data Value'])
    check_categorical(
        'CDC Diabetes',
        diabetes,
        ['Location', 'Short Indicator Text',
         'Stratification Group 1', 'Data Type']
    )

    # 2. SHADAC Insurance dataset
    check_dimensions('SHADAC Insurance', insurance)
    check_missing_values('SHADAC Insurance', insurance)
    check_quantitative('SHADAC Insurance', insurance, ['Data'])
    check_categorical(
        'SHADAC Insurance',
        insurance,
        ['Location', 'Coverage Type', 'Race / Ethnicity', 'Data Type']
    )

    # 3. KFF Poverty dataset
    check_dimensions('KFF Poverty', poverty)
    check_missing_values('KFF Poverty', poverty)
    check_quantitative(
        'KFF Poverty',
        poverty,
        [
            'White',
            'Black',
            'Hispanic',
            'Asian/Native Hawaiian or Pacific Islander',
            'American Indian or Alaska Native',
            'Multiple Races',
            'Total'
        ]
    )
    check_categorical('KFF Poverty', poverty, ['Location'])


if __name__ == '__main__':
    main()
