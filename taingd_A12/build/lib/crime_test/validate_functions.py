import pandas as pd

def validate_sex_and_age(df):
    sex_validated = ((df['Vict Sex'] == 'M') | (df['Vict Sex'] == 'F')) & df['Vict Sex'].notnull()
    age_validated = ((df['Vict Age'] >= 1) & (df['Vict Age'] <= 100)) & df['Vict Age'].notnull()

    if(sex_validated.all() & age_validated.all()):
        return 'Data is valid'
    else:
        return 'Data is invalid'