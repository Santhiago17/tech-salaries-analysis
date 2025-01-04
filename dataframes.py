import pandas as pd

df = pd.read_csv('database/global_tech_salary.csv')

df['job_title'] = df['job_title'].astype('string')

