#Importando as bibliotecas que serão necessárias
import matplotlib.pyplot as plt
import numpy as np

#Função com a equação
def equacao(a, b, c, x):
  y = a * x + b * x - c
  return y

#Valores presentes na equação com o RU
a = 7
b = 8
c = 1

#Vetor com os valores de X
x = [x1 := 2, x2 := 3, x3 := 4, x4 := 5, x5 := 6, x6 := 7, x7 := 8, x8 := 9, x9 := 10, x10 := 11]

#Configurando o visual e legenda do gráfico
plt.grid()
plt.title("Equação y = ax + bx - c")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

#Definindo o jeito de cada ponto e a cor.
plt.plot(x1, equacao(a, b, c, x1), marker ="o", markersize = 14, markerfacecolor = 'gray')
plt.plot(x2, equacao(a, b, c, x2), marker ="o", markersize = 14, markerfacecolor = 'black')
plt.plot(x3, equacao(a, b, c, x3), marker ="o", markersize = 14, markerfacecolor = 'brown')
plt.plot(x4, equacao(a, b, c, x4), marker ="o", markersize = 14, markerfacecolor = 'red')
plt.plot(x5, equacao(a, b, c, x5), marker ="o", markersize = 14, markerfacecolor = 'salmon')
plt.plot(x6, equacao(a, b, c, x6), marker ="o", markersize = 14, markerfacecolor = 'chocolate')
plt.plot(x7, equacao(a, b, c, x7), marker ="o", markersize = 14, markerfacecolor = 'yellow')
plt.plot(x8, equacao(a, b, c, x8), marker ="o", markersize = 14, markerfacecolor = 'lightgreen')
plt.plot(x9, equacao(a, b, c, x9), marker ="o", markersize = 14, markerfacecolor = 'aqua')
plt.plot(x10, equacao(a, b, c, x10), marker ="o", markersize = 14, markerfacecolor = 'fuchsia')

#Acrescentando a legenda sobre cada ponto do gráfico
plt.legend([f'x1={x1}, y1 ={equacao(a, b, c, x1)}',
            f'x2={x2}, y2 ={equacao(a, b, c, x2)}',
            f'x3={x3}, y3 ={equacao(a, b, c, x3)}',
            f'x4={x4}, y4 ={equacao(a, b, c, x4)}',
            f'x5={x5}, y5 ={equacao(a, b, c, x5)}',
            f'x6={x6}, y6 ={equacao(a, b, c, x6)}',
            f'x7={x7}, y7 ={equacao(a, b, c, x7)}',
            f'x8={x8}, y8 ={equacao(a, b, c, x8)}',
            f'x9={x9}, y9 ={equacao(a, b, c, x9)}',
            f'x10={x10}, y10 ={equacao(a, b, c, x10)}'])
