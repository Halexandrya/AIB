import pandas as pd
from pathlib import Path

# Define o caminho (path) para chegar à tabela excel
path = str(Path(__file__).parent)

df = pd.read_excel(path + '\\tabela.xlsx')
df['Cf'] = df['C0'] * (1 + df['Taxa'] / 100)**df['Periodo']
df.to_excel(path + '\\tabela.xlsx', index=False)

print(df)