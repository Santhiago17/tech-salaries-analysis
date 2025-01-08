import pandas as pd

# Lê o arquivo original
df = pd.read_csv('database/global_tech_salary.csv')

# Converte as colunas para o tipo string
string_columns = [
    'job_title', 'experience_level', 'employment_type',
    'salary_currency', 'employee_residence',
    'company_location', 'company_size'
]
df[string_columns] = df[string_columns].astype('string')

# Salva o arquivo atualizado
df.to_csv('database/global_tech_salary_atualizado.csv', index=False)

# Especifica os tipos das colunas ao recarregar o arquivo
dtype_map = {col: 'string' for col in string_columns}

new_df = pd.read_csv('database/global_tech_salary_atualizado.csv', dtype=dtype_map)

# Exibe as informações do dataframe ajustado
print(new_df.info())
