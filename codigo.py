###########################
# Autor: Fabrício Reis
###########################

# bibliotecas -----------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats

# configurações ---------------------------------------------------------
set_matplotlib_formats('svg')
plt.style.use('seaborn-whitegrid')
plt.rcParams['font.family'] = 'Liberation Sans'

# lendo o arquivo -------------------------------------------------------
arquivo = 'dados/inf.csv'
df = pd.read_csv(arquivo)

# traçando o gráfico ----------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 3.5))

cores = ['grey', 'grey', 'grey', 'grey', 'grey', '#fc475c'] 
grafico = df.groupby('ano')['dados'].mean()
grafico.plot(kind='bar', rot=0, width=0.55,
             color=cores, legend=None, ax=ax)
plt.xlabel(None)

#------------------------------------------------------------------------
# removendo grids e eixos
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.grid(b=False, axis='x') 

# texto
plt.title('Desmatamento na Amazônia: 2015-2021\n\n\n', 
          fontsize=15, weight='bold', loc='left')

fig.text(x=0.125, 
         y=1.05,
         s='De agosto a julho, em km²',
         fontsize=11,
         fontstyle='italic',
         color='black')

fig.text(x=0.125,
         y=0.85,
         s='O desmatamento em 2020-2021 é o\n'
         '2° pior da história recente\n',
         fontsize=12,
         color='black')

fig.text(x=0.125,
         y=0,
         s='Fonte: Inpe, Deter | Autor: Fabrício Reis (@fabricioreisbr)',
         fontsize=11,
         weight='bold',
         color='black')   

# valores nas barras
ax.bar_label(ax.containers[0], 
             labels=['5.377,08 km²', '4.639,47 km²', '4.570,63 km²', 
                     '6.843,91 km²', '9.215,88 km²', '8.711,74 km²'])

#-------------------------------------------------------------------------
plt.show()