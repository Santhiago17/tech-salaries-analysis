import pandas as pd

txt_file = 'database/global_tech_salary.txt'
csv_file = 'global_tech_salary.csv'

try: 
    data = pd.read_csv(txt_file,delimiter=',', encoding='utf-8')
except Exception as e:
    print(f"Erro ao ler o arquivo TXT: {e}")
    raise

try:
    data.to_csv(csv_file, index=False,encoding='utf-8')
    print(f"Arquivo convertido para CSV com sucesso! Salvo como: {csv_file}")
except Exception as e:
    print(f"Erro ao salvar o arquivo como CSV: {e}")
    raise