import pandas as pd

def mean_age(df):
    return df['Vict Age'].mean()

def median_age(df):
    return df['Vict Age'].median()