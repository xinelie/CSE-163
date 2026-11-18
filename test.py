"""
Megha Nilesh Varma, Sandy Kwong
CSE 163 AB
Final Project

testing data cleaning, merging, and visualization functions using (test_diabetes.csv, test_insurance.csv, test_poverty.csv) extracted directly
from the clean diabetes, SHADAC, and KFF datasets.
"""
import pandas as pd
import clean
import merge

# all testing data
d = pd.read_csv('test_diabetes.csv')
i = pd.read_csv('test_insurance.csv', skiprows=6) # skipping rows cause it is just info abiut the dataset 
p = pd.read_csv('test_poverty.csv', skiprows=2)

def test_clean():
    """
    Tests that clean.py functions filter and format all three test CSVs as intended.
    """

    # Diabetes cleaning (single-state & multi-state)
    d_q1 = clean.diabetes_data_q1(d)
    assert (d_q1['Location'] == 'Washington').all()

    d_q2 = clean.diabetes_data_q2(d)
    assert set(d_q2['Location']) == {'Washington', 'California'} # all staes in datset need to be included

    # Insurance cleaning (Washington-only)
    i_q1 = clean.insurance_data_q1(i)
    assert (i_q1['Location'] == 'Washington').all()

    # Poverty cleaning (Washington-only & multi-state)
    p_wa = clean.poverty_data_q3_just_Wa(p)
    assert (p_wa['Location'] == 'Washington').all()
    assert p_wa['Poverty Rate'].between(0, 100).all() # ensuring all converted to percentages   

    p_multistate = clean.poverty_data_q3_multistate(p)
    assert 'United States' not in list(p_multistate['Location'])


def test_merge():
    """
    Tests that merge.py accurately joins the cleaned test CSVs
    """

    d_q1 = clean.diabetes_data_q1(d)
    i_q1 = clean.insurance_data_q1(i)
    p_wa = clean.poverty_data_q3_just_Wa(p )

    d_q2 = clean.diabetes_data_q2(d)
    p_multi = clean.poverty_data_q3_multistate(p)

    q1 = merge.q1(d_q1, i_q1)
    assert not q1.empty

    q3_wa = merge.q3(d_q1, p_wa)
    assert (q3_wa['Location'] == 'Washington').all()

    q3_multi = merge.q3(d_q2, p_multi)
    assert not q3_multi.empty


def main():
    test_clean()
    test_merge()
    print("All tests passed!")


if __name__ == '__main__':
    main()