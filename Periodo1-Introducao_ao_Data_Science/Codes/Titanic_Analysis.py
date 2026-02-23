#!/usr/bin/env python
# coding: utf-8

# O projeto deverá ser desenvolvido de forma estruturada, contemplando as etapas de importação dos dados, compreensão do conjunto de informações,

# In[12]:


#iniciando a biblioteca pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

#lendo o arquivo csv e armazenando em um dataframe
df = pd.read_csv('../Src/titanic_dataset.csv')

#reduzindo o numero de caracteres exibidos para cada coluna
#pd.set_option('display.max_colwidth', 10)

#definindo a opção para não quebrar o dataframe em várias linhas
#pd.set_option("display.expand_frame_repr", False)

#exibindo as primeiras linhas do dataframe
print(tabulate(df.head(10), headers=df.columns, tablefmt="grid"))
print("---------------------------------------------------------")
print("\n")


# ## Apresentando outras informações do dataset

# In[15]:


#Exibindo a quantidade de linhas e colunas do dataframe
print("Quantidade de linhas e colunas do dataframe:")
linhas = (df.shape[0])
colunas = (df.shape[1])
print(f"Linhas: {linhas}")
print(f"Colunas: {colunas}")
print("---------------------------------------------------------")
print("\n")

#Exibindo outras informações sobre o dataframe
print("Informações sobre o dataframe:")
print(df.info())

print("---------------------------------------------------------")
print("\n")

#Exibindo a quantidade de valores nulos em cada coluna
print("Quantidade de valores nulos em cada coluna:")
print(df.isnull().sum())
print("---------------------------------------------------------")
print("\n")

#Verificando a quantidade de linhas repetidas no dataframe
linhas_repetidas = df.duplicated().sum()
print(f"Quantidade de linhas repetidas: {linhas_repetidas}")
print("---------------------------------------------------------")
print("\n")


print(df.describe())


# preparação e tratamento dos dados, incluindo a verifi cação e o tratamento de valores nulos ou duplicados, ajustes de tipagem e organização das colunas.

# Tratatando os valores nulos

# In[16]:


#iniciando a biblioteca pandas
import pandas as pd

#Lendo o arquivo CSV do dataset do Titanic
df = pd.read_csv('../Src/titanic_dataset.csv')

#Exibindo a quantidade de valores nulos em cada coluna
print("Quantidade de valores nulos em cada coluna:")
print(df.isnull().sum())
print("---------------------------------------------------------")
print("\n")


# Tratatando os valores nulos para idade (177 ocorrências)

# In[17]:


#verificando quantos valores nulos existem na coluna 'Age'
Age_null_count = df['Age'].isnull().sum()
print("---------------------------------------------------------")
print("Quantidade de valores nulos na coluna 'Age':", Age_null_count)
print("---------------------------------------------------------")

#Verificando os valores existentes na coluna 'Age'
print("Valores únicos na coluna 'Age':")
print(df['Age'].unique())
print("---------------------------------------------------------")

#substituindo os valores nulos da coluna 'Age' por 0
df['Age'] = df['Age'].fillna(0)

#verificando se os valores nulos foram substituídos por 0
Age_null_count = df['Age'].isnull().sum()
print("Todos os valores nulos da coluna 'Age' foram substituídos por 0.")
print("Quantidade de valores nulos na coluna 'Age':", Age_null_count)
print("---------------------------------------------------------")


# Tratando os dados nulos no campo cabine

# In[18]:


#verificando quantos valores nulos existem na coluna 'Age'
Cabin_null_count = df['Cabin'].isnull().sum()
print("---------------------------------------------------------")
print("Quantidade de valores nulos na coluna 'Cabine':", Cabin_null_count)
print("---------------------------------------------------------")

#Verificando os valores existentes na coluna 'Cabin'
print("Valores únicos na coluna 'Cabin':")
print(df['Cabin'].unique())
print("---------------------------------------------------------")

#substituindo os valores nulos da coluna 'Cabin' por 'Not known'
df['Cabin'] = df['Cabin'].fillna('Not known')

#verificando se os valores nulos foram substituídos por 'Not known'
Cabin_null_count = df['Cabin'].isnull().sum()
print("Todos os valores nulos da coluna 'Cabin' foram substituídos por 'Not known'.")
print("Quantidade de valores nulos na coluna 'Cabin':", Cabin_null_count)
print("---------------------------------------------------------")


# Tratadando os valores nulos para Porto de Embarque

# In[19]:


#verificando quantos valores nulos existem na coluna 'Embarked'
Embarked_null_count = df['Embarked'].isnull().sum()
print("---------------------------------------------------------")
print("Quantidade de valores nulos na coluna 'Embarked':", Embarked_null_count)
print("---------------------------------------------------------")

#Verificando os valores existentes na coluna 'Embarked'
print("Valores únicos na coluna 'Embarked':")
print(df['Embarked'].unique())
print("---------------------------------------------------------")

#substituindo os valores nulos da coluna 'Embarked' por 'Not known'
df['Embarked'] = df['Embarked'].fillna('Not known')

#verificando se os valores nulos foram substituídos por 'Not known'
Embarked_null_count = df['Embarked'].isnull().sum()
print("Todos os valores nulos da coluna 'Embarked' foram substituídos por 'Not known'.")
print("Quantidade de valores nulos na coluna 'Embarked':", Embarked_null_count)
print("---------------------------------------------------------")


# A análise deverá envolver a compreensão das variáveis, a aplicação de fi ltros, ordenações e agrupamentos (GroupBy), bem como a construção de pelo menos uma visualização gráfi ca que represente a distribuição dos dados ou a relação entre variáveis relevantes, utilizando a linguagem Python e bibliotecas adequadas ao contexto da análise exploratória.

# ##Renomeando as colunas para tornar o dataset mais legível

# In[20]:


#renomeando as colunas do dataframe
df.columns = ['ID_Passageiro',
              'Sobrevivente',
              'Classe',
              'Nome',
              'Genero',
              'Idade',
              'Irmãos_Esposas_Bordo',
              'Pais_Filhos_Bordo',
              'Bilhete',
              'Tarifa',
              'Cabine',
              'Porto_Embarque']

# Informando a tradução das colunas do dataset Titanic para português
# Colunas originais do dataset Titanic
colunas_originais = [
    "PassengerId", "Survived", "Pclass", "Name", "Sex", "Age",
    "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"
]

# Tradução para português
colunas_novas = [
    'ID_Passageiro', 'Sobrevivente', 'Classe', 'Nome', 'Genero', 'Idade',
    'Irmãos_Esposas_Bordo', 'Pais_Filhos_Bordo','Bilhete', 'Tarifa', 'Cabine', 'Porto_Embarque'
]

# Criar DataFrame comparativo
df_colunas = pd.DataFrame({
    "Original": colunas_originais,
    "Português": colunas_novas
})

print("Tradução das colunas do dataset Titanic para português:")
print(tabulate(df_colunas, headers=df_colunas.columns, tablefmt="grid"))

#exibindo as primeiras linhas do dataframe
print("\n")
print("Head (10 registros) do dataframe com as colunas renomeadas:")
print(tabulate(df.head(10), headers=df.columns, tablefmt="grid"))
#print(df.head(10))
print("---------------------------------------------------------")
print("\n")


# Removendo as colunas que não serão utilizadas na análise

# In[21]:


#remover as colunas que não serão utilizadas na análise
df = df.drop(columns=['ID_Passageiro', 'Irmãos_Esposas_Bordo', 'Pais_Filhos_Bordo', 'Bilhete', 'Tarifa', 'Cabine'])

#exibindo as primeiras linhas do dataframe
print(tabulate(df.head(10), headers=df.columns, tablefmt="grid"))


# Alterando os dados da tabela para tornar mais legível

# In[22]:


#substituindo os valores da coluna 'Sobrevivente' para 'Sobrevivente" e 'Não Sobrevivente'
df['Sobrevivente'] = df['Sobrevivente'].replace({0: 'Não Sobrevivente', 1: 'Sobrevivente'})

#substituindo os valores da coluna 'Genero' para 'Masculino' e 'Feminino'
df['Genero'] = df['Genero'].replace({'male': 'Masculino', 'female': 'Feminino'})

#substituindo os valores da coluna 'Porto_Embarque' para 'Southampton', 'Cherbourg' e 'Queenstown'
df['Porto_Embarque'] = df['Porto_Embarque'].replace({'S': 'Southampton', 'C': 'Cherbourg', 'Q': 'Queenstown'})


#exibindo as primeiras linhas do dataframe
print("Head (10 registros) do dataframe os valores das colunas alterados:")
print(tabulate(df.head(10), headers=df.columns, tablefmt="grid"))
#print(df.head(10))
print("---------------------------------------------------------")
print("\n")


# Alterando a ordem das colunas

# In[23]:


# alterando a ordem das colunas do dataframe
df = df[['Nome', 'Genero', 'Idade', 'Classe', 'Porto_Embarque', 'Sobrevivente']]
#exibindo as primeiras linhas do dataframe
print("Head (10 registros) do dataframe os valores das colunas alterados:")
print(tabulate(df.head(10), headers=df.columns, tablefmt="grid"))


# Analise comparativa entre a população que embarcou e população que sobreviveu

# In[24]:


#POPULAÇÃO QUE EMBARCOU X POPULAÇÃO QUE SOBREVIVEU
# Totais absolutos
total_embarcados = len(df)
total_sobreviventes = (df['Sobrevivente'] == 'Sobrevivente').sum()
total_nao_sobreviventes = (df['Sobrevivente'] == 'Não Sobrevivente').sum()

#calcula a proporção de sobreviventes em relação ao total de passageiros
Proporcao = df['Sobrevivente'].value_counts(normalize=True)
proporcao_sobreviveu = Proporcao['Sobrevivente'] * 100
proporcao_nao_sobreviveu = Proporcao['Não Sobrevivente'] * 100

#mostra total de passageiros embarcados, total de sobreviventes e total de não sobreviventes, além das proporções
print(f"Total de passageiros embarcados: {total_embarcados}")
print(f"Total sobrevivente: {total_sobreviventes}"+f" ({proporcao_sobreviveu:.2f}%)")
print(f"Total não sobrevivente: {total_nao_sobreviventes}"+f" ({proporcao_nao_sobreviveu:.2f}%)")


# Criar DataFrame para o gráfico
dados = pd.DataFrame({
    'Total': [total_embarcados],
    'Sobreviveu': [total_sobreviventes],
    'Não sobreviveu': [total_nao_sobreviventes]
})
plt.figure(figsize=(8, 6))
plt.title("População embarcada vs sobrevivência")
plt.ylabel("Total") #altera o rótulo do eixo Y para "Total"
ax = sns.barplot(data=dados)

# Adicionar os totais e porcentagens em cima das barras
for p in ax.patches:
    height = p.get_height()
    percent = (height / total_embarcados) * 100
    ax.annotate(f'{int(height)} ({percent:.1f}%)',
                (p.get_x() + p.get_width() / 2., height),
                ha='center', va='bottom')


plt.show()



# Analise comparativa entre a população que embarcou e população que sobreviveu por gênero

# In[25]:


#POPULAÇÃO QUE EMBARCOU X POPULAÇÃO QUE SOBREVIVEU POR GÊNERO

#EMBARCARAM
print("Totais de homens e mulheres que embarcaram:")

#soma a quantidade de ocorrencias de cada genero
Total_masculino = df['Genero'].value_counts()['Masculino']
Total_feminino = df['Genero'].value_counts()['Feminino']

#calcula a proporção de cada genero em relação ao total de passageiros
Proporcao = df['Genero'].value_counts(normalize=True)
proporcao_masculino = Proporcao['Masculino'] * 100
proporcao_feminino = Proporcao['Feminino'] * 100

#mostra total e proporção de cada genero
print(f"Total masculino: {Total_masculino}"+f" ({proporcao_masculino:.2f}%)")
print(f"Total feminino: {Total_feminino}"+f" ({proporcao_feminino:.2f}%)")



#SOBREVIVENTES
#filtrando o dataframe para obter apenas os sobreviventes
sobreviventes = df[df['Sobrevivente'] == 'Sobrevivente']
sobreviventes['Genero'].value_counts(normalize=True)

# Comparação por genero
pd.crosstab(df['Genero'], df['Sobrevivente'], normalize='index')

# Criando a figura do gráfico
plt.figure(figsize=(8, 6))

#Configurações do gráfico
plt.title("Distribuição de sobrevivência por gênero")
plt.ylabel("Total") #altera o rótulo do eixo Y para "Total"
ax = sns.countplot(x='Genero', hue='Sobrevivente', data=df)

#inclui os totais da quantidade de sobreviventes e não sobreviventes em cada barra do gráfico
#em valores inteiros
for p in ax.patches:
    height = p.get_height()
    if height > 0:  # só anota se a barra tiver altura > 0 por que estavam aparecendo valores zerados no gráfico
        percent = (height / total_embarcados) * 100
        ax.annotate(f'{int(height)} ({percent:.1f}%)',
                (p.get_x() + p.get_width() / 2., height),
                ha='center', va='bottom')


plt.show()


# Analise comparativa entre a população que embarcou e população que sobreviveu por idade

# In[26]:


#distribuição de frequências da coluna idade
#resumo estatístico da coluna Idade
print("Resumo estatístico dos dados sobre Idade:")

dados = df['Idade'].describe()
dados = dados.rename({
    'count': 'Total de passageiros com idade registrada',
    'mean': 'Média',
    'std': 'Desvio padrão',
    'min': 'Idade mínima',
    '25%': '25% - 1º Quartil',
    '50%': '50% - Mediana',
    '75%': '75% - 3º Quartil',
    'max': 'Idade máxima'
})

#imprime o resumo estatístico da coluna Idade em formato de tabela
print(tabulate(dados.to_frame(), headers=["Estatística", "Valor"], tablefmt="grid"))

# Criar quartis de idade
df['Quartil_Idade'] = pd.qcut(df['Idade'], q=3, labels=['1º Quartil','2º Quartil','3º Quartil'])

# contar totais por quartil
total_por_quartil = df.groupby('Quartil_Idade').size().reset_index(name='Total')

# Contar totais sobreviventes por quartil
sobreviventes_por_quartil = df[df['Sobrevivente'] == 'Sobrevivente'].groupby('Quartil_Idade').size().reset_index(name='Total')

# Contar totais nao sobreviventes por quartil
nao_sobreviventes_por_quartil = df[df['Sobrevivente'] == 'Não Sobrevivente'].groupby('Quartil_Idade').size().reset_index(name='Total')

#print('Total de passageiros por quartil de idade:')
#print(total_por_quartil)

#print("Número de sobreviventes por quartil de idade:")
#print(sobreviventes_por_quartil)

#print("Número de não sobreviventes por quartil de idade:")
#print(nao_sobreviventes_por_quartil)

# Gráfico
plt.figure(figsize=(8,6))
ax = sns.countplot(x='Quartil_Idade', hue='Sobrevivente', data=df)

plt.title("Número de sobreviventes por quartil de idade")
plt.xlabel("Quartil de idade")
plt.ylabel("Total de passageiros") 
plt.legend(title=None, loc='lower right') #remove o título da legenda e posiciona no canto inferior direito

# Adicionar valores em cima das barras
for p in ax.patches:
    height = p.get_height()
    percent = (height / total_embarcados) * 100
    ax.annotate(f'{int(height)} ({percent:.1f}%)',
                (p.get_x() + p.get_width() / 2., height),
                ha='center', va='bottom')

plt.show()

#sns.histplot(df, x='Idade', hue='Status', multiple='stack')
#plt.show()



# Analise comparativa entre a população que sobreviveu e que não sobreviveu por classe

# In[27]:


#distribuição de frequências da coluna classe
print("Proporção de passageiros por classe:")
#print(df['Classe'].value_counts(normalize=True))


# por local de embarque

# In[28]:


"""
#distribuição de frequências da coluna embarked
print("Proporção de passageiros por porto de embarque:")
print(df['Porto_Embarque'].value_counts(normalize=True))

#POPULAÇÃO QUE SOBREVIVEU


sobreviventes['Classe'].value_counts(normalize=True)
sobreviventes['Porto_Embarque'].value_counts(normalize=True)



# Comparação por classe
pd.crosstab(df['Classe'], df['Sobrevivente'], normalize='index')

# Comparação por porto de embarque
pd.crosstab(df['Porto_Embarque'], df['Sobrevivente'], normalize='index')

#Isso mostra, por exemplo:
#- Qual proporção de homens/mulheres sobreviveu.
#- Qual proporção de passageiros de cada classe sobreviveu.
#- Diferenças entre portos de embarque.





sns.countplot(x='Classe', hue='Status', data=df)
plt.show()
"""

