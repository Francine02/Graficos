#Configurações iniciais para fazer o trabalho
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/content/archive_stores.zip', sep = ',', encoding= 'ISO 8859-1')

#Descobrindo o nome das colunas e renomeando elas
dfColunas = ['ï»¿Store ID ', 'Store_Area', 'Items_Available',
       'Daily_Customer_Count', 'Store_Sales']
dfNovo = df.filter (items = dfColunas)
dfNovo = dfNovo.rename (columns={
    'ï»¿Store ID ': 'ID',
    'Store_Area' : 'Área da Loja',
    'Items_Available' : 'Itens Disponíveis',
    'Daily_Customer_Count' : 'Visitantes',
    'Store_Sales' :'Vendas (US$)'})

#Função que aborda as questões de máximo, mínimo, médio e desvio padrão sobre os itens disponíveis.
def item():
 print('\n Itens Disponíveis')
 disponível = dfNovo['Itens Disponíveis']
 print(f'Máximo:{disponível.values.max()}')
 print(f'Mínimo:{disponível.values.min()}')
 print(f'Média:{disponível.values.mean()}')
 print(f'Desvio Padrão:{disponível.values.std()}')
#Configurações do gráfico sobre esse assunto, definindo a legenda, os eixos e a cor
 plt.xlabel("ID da Loja")
 plt.ylabel("Quantidade")
 plt.rcParams['figure.figsize'] = (5,5) #O tamanho da figura
 plt.plot(disponível, 'ro', label = 'Itens Disponíveis', markerfacecolor = 'blue')
 plt.legend()
 plt.show() #Mostrando o gráfico

#Função sobre os visitantes, parecida com a função de item.
def visit():
 print('\n Visitantes')
 visita = dfNovo['Visitantes']
 print(f'Máximo:{visita.values.max()}')
 print(f'Mínimo:{visita.values.min()}')
 print(f'Média:{visita.values.mean()}')
 print(f'Desvio Padrão:{visita.values.std()}')
 plt.xlabel("ID da Loja")
 plt.ylabel("Quantidade")
 plt.rcParams['figure.figsize'] = (5,5)
 plt.plot(visita, 'ro', label = 'Visitantes', markerfacecolor = 'red')
 plt.legend()
 plt.show()

#Mesma coisa que as anteriores, só muda o assunto que é de vendas
def vend():
 print('\n Vendas (US$)')
 venda = dfNovo['Vendas (US$)']
 print(f'Máximo:{venda.values.max()}')
 print(f'Mínimo:{venda.values.min()}')
 print(f'Média:{venda.values.mean()}')
 print(f'Desvio Padrão:{venda.values.std()}')
 plt.xlabel("ID da Loja")
 plt.ylabel("Quantidade")
 plt.rcParams['figure.figsize'] = (5,5)
 plt.plot(venda, 'ro', label = 'Vendas (US$)', markerfacecolor = 'orange')
 plt.legend()
 plt.show()

#Chamando as funções para mostrar para o usuário
item ()
visit()
vend()
dfNovo.head() #Mostrando a tabela com os nomes das colunas atualizadas