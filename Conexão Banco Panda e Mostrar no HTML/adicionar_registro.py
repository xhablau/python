import pandas as pd

# Cria um DataFrame vazio com as colunas desejadas
df = pd.DataFrame(columns=['Nome', 'Idade', 'Cidade'])

# Cria um novo registro como um dicionário
novo_registro = {'Nome': 'Maria', 'Idade': 30, 'Cidade': 'Rio de Janeiro'}

# Adiciona o novo registro ao DataFrame
df = pd.concat([df, pd.DataFrame(novo_registro, index=[0])], ignore_index=True)

# Salva o DataFrame em um arquivo CSV
df.to_csv('meu_dataframe.csv', index=False)
