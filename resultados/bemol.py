import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
ind = np.arange(12)

# # # IMPORT DADOS EXCEL # # #
d1_xls = pd.read_excel('dados.xlsx', 'realizado', index= False) # Plan. 1
d2_xls = pd.read_excel('dados.xlsx', 'orcado', index= False) # Plan. 2


# # # TRATAMENTO PLANILHA 1 # # #
d1_xls = d1_xls.drop('Unnamed: 0',axis=1) # Apagando Coluna Nula 
d1_xls = d1_xls.transpose() # Transposicao da Tabela
d1_xls.columns = ['mes', 'realizado'] # Renomeando colunas de d1_xls
d1_xls['realizado'] = d1_xls['realizado'].astype('float') # Alterando tipo de dado para Float

# # # TRATAMENTO PLANILHA 2 # # #
d2_xls['orcado'] = d2_xls['orcado'].astype('float') # Alterando tipo de dado para Float
d2_xls.columns = ['mesO', 'orcado']  # Renomeando colunas de d2_xls

# # # TRATAMENTO TABELA DATAFRAME FINAL # # #
df = d1_xls.merge(d2_xls, left_on='mes', right_on='mesO') # Merge entre PLAN1 e PLAN2
df = df.drop('mesO', axis = 1) # Apagando coluna mesO (repetida)

# # # DIFERENCA REALIZADO x ORCADO # # #
df['diferenca'] = 0 # Criando uma nova coluna
df['diferenca'] = df['orcado'] - df['realizado']  # Calculando Diferenca

# # # DEBUG # # #
print('Realizado:')
print(d1_xls.head())
print('------')
print('Orcado:')
print(d2_xls.head())
print('------')
print('Resultado(Merge)')
print(df.head())
print('------')

# # # CSV # # #
df.to_csv('dados_orcamento.csv', encoding='utf-8', index=False) # CSV

# # # GRAFICO # # #
plt.rcParams["figure.figsize"] = [20, 7] # Tamanho do grafico
p1 = plt.bar(ind, d2_xls['orcado'], 0.6) # Barras orcados
p2 = plt.bar(ind, d1_xls['realizado'], 0.6) # Barras realizados
plt.title('Grafico Orcamento') # Titulo
plt.xticks(ind, d1_xls['mes']) # Eixo x - meses
plt.xlabel('Meses') # Nome eixo x
plt.ylabel('R$') # Nome eixo y
plt.legend((p1[0], p2[0]), ('Orcado', 'Realizado')) # Legendas
plt.savefig('grafico_orcamento.png', transparent = False) # Salvar em arquivo
plt.show() # Exibir Grafico