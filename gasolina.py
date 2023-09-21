import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data_gas = pd.read_csv('gasolina.csv')

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=data_gas, x="dia", y="venda", palette="pastel")
  grafico.set(title='Preço da gasolina', xlabel='Dia', ylabel='Preço');

plt.savefig('gasolina.png')
