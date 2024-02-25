# importa as libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from   sklearn.linear_model import LinearRegression
from   sklearn.metrics import r2_score
import statsmodels.api as sm
import os
df_dados = pd.read_csv('../input/insolv1/Insol.csv',sep=';',header=0)

#verificando a estrutura dos dados importados: são 200 linhas e 5 colunas
print(df_dados.shape)

#verificando o conteúdo das peimeiras linhas do dataset
df_dados.head()

#print(df_dados.describe())
ow()


X = df_dados['Numero_Empregados'].values.reshape(-1,1)
y = df_dados['Fundo_de_maneio'].values.reshape(-1,1)


reg = LinearRegression()
reg.fit(X, y)

print("O modelo é: Maneio = {:.5} + {:.5}X".format(reg.intercept_[0], reg.coef_[0][0]))
f_previsaoes = reg.predict(X)

plt.figure(figsize = (16,8))
plt.scatter(
    df_dados['Numero_Empregados'], 
    df_dados['Fundo_de_maneio'], 
    c='red')
plt.plot(
    df_dados['Numero_Empregados'],
    f_previsaoes,
    c='blue',
    linewidth=3,
    linestyle=':'
)

plt.xlabel(" ($) Numero de Empregados")
plt.ylabel(" ($) Maneio ")
plt.show()

X = df_dados['Numero_Empregados']
y = df_dados['Fundo_de_maneio']
X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())

