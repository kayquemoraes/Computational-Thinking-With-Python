#Matrizes

#Matriz 3x3
matriz = [[1,2,3],[4,5,6],[7,8,9]]

#Função para printar cada elemento da matriz
def printa_elementos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"matriz[{i}][{j}] = {matriz[i][j]}")
    return

#Função para printar matriz    
def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

#Função para criar matriz
def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(0)
    return matriz

matriz = cria_matriz(10,10)

#Preenche colunas pares com 1, e ímpares com 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if j%2 == 0:
            matriz[i][j] = 1
        else:
            matriz[i][j] = 0

print("Matriz colunas pares com 1, e ímpares com 0:")
mostra_matriz(matriz)

print()

#Preenche linhas pares com 1, e ímpares com 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i%2 == 0:
            matriz[i][j] = 1
        else:
            matriz[i][j] = 0

print("Matriz linhas pares com 1, e ímpares com 0:")
mostra_matriz(matriz)

#Preenche colunas pares com 1, e ímpares com 0 (sem usar condições)
for i in range(len(matriz)):
    for j in range(0, len(matriz), 2):
        matriz[i][j] = 1

print()

jogo = cria_matriz(10,10)

#Preenche matriz triangular superior com 2
for i in range(len(jogo)):
    for j in range(i, len(jogo)):
        jogo[i][j] = 2

print("Matriz triangular superior com 2:")
mostra_matriz(jogo)

print()

#Preenche matriz triangular inferior com 1
for i in range(len(jogo)):
    for j in range(0, i + 1):
        jogo[i][j] = 1

print("Matriz triangular inferior com 1:")
mostra_matriz(jogo)

print()

#Função para tranpor matriz
def transpor_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(i, len(matriz)):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    return matriz

print("Matriz transposta:")
mostra_matriz(transpor_matriz(jogo))

print()

dama = cria_matriz(10,10)

#Matriz dama
for i in range(len(dama)):
    for j in range(len(dama)):
        #par + par, ou ímpar + ímpar resultam em um número par, par + ímpar, resultam em um número ímpar
        if (i+j)%2==0: #Outro jeito: (i%2)==(j%2) -> ímpar com ímpar, ou par com par, dama[i][j] = 1
            dama[i][j] = 1

print("Matriz dama:")
mostra_matriz(dama)

print()
print("<------------------------------------------------>")
print()

##Dicionários

#Para multiplicar uma matriz ixj por mxn, j deve ser igual a m, e resultará numa matriz ixn

#Matriz 1x5
pesos = [1,2,3,2,1]
soma_pesos = 9

#Matriz 5xn
notas = [[9,8],[7,6],[4,5],[10,10],[8,7]]
alunos = len(notas[0])

media = []

for j in range(alunos):
    soma = 0
    for i in range(len(pesos)):
        soma += pesos[i]*notas[i][j]
    soma /= soma_pesos
    media.append(soma)

print(media)

dic = {"chave_1" : "valor1",
       "chave_2" : "valor_2"}

dic["chave_3"] = "valor_3"
print(dic)
print(dic["chave_1"])

jogo = {"são paulo" : "venceu",
        "corinthians" : "looser"}
resposta = input("Pra que time você torce: ")

print(jogo[resposta])

import random
saudacoes = {"oi": ["olá","salve","iae","hello"],
            "tchau": ["vaza","flw","some","picopé"]}

resposta = input("Oi!! oi/ tchau: ")

print(saudacoes[resposta][random.randint(0,len(saudacoes["oi"])-1)])

carros = {"modelo" : ["corsinha","up","celta","ka","gol","uno"],
          "preco" : [10,20,2000,30,6555,10000],
          "potencia(cv)" : [100,200,500,250,10,512]}

import pandas as pd

print(pd.DataFrame(carros))


dic_numeros = {"par" : [],
             "ímpar" : []}

numeros = [1,2,3,4,5,6,7,8,9,10]

for i in numeros:
    if i%2 == 0:
        dic_numeros["par"].append(i)
    else:
        dic_numeros["ímpar"].append(i)

print(dic_numeros)