# Dicionários

import pandas as pd

carros = {
            "modelo":["up", "ka", "celtinha", "gol"],
            "preço":[10,20,1000,50]
}

carros["potencia (cv)"] = [500, 50, 200, "+8000"]

print(pd.DataFrame(carros))

def encontra_maior(lista):
    indice_maior = 0
    maior = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indice_maior = i
    return indice_maior

local_maior = encontra_maior(carros["preço"])

for key in carros.keys():
    print(f"{key} : {carros[key][local_maior]}")

def adiciona_carro(dic):
    while True:
        resposta = input("Você quer cadastrar um novo carro? (sim/ nao): ")
        while resposta not in ["sim","nao"]:
            resposta = input("Você quer cadastrar um novo carro? (sim/ nao): ")
        if resposta == "sim":
            for key in dic.keys():
                dic[key].append(input(f"{key}: "))
        else:
            print("Finalizado")
            break
    return dic

print(adiciona_carro(carros))

frase = "A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha."

def conta_palavras(frase):
    frase = frase.lower()
    for char in ",.!?:;*":
        frase = frase.replace(char,"")
    frase = frase.split(" ")
    palavras = {}
    for palavra in frase:
        if palavra not in palavras.keys():
            palavras[palavra] = 1
        else:
            palavras[palavra] += 1
    return palavras

print(conta_palavras(frase))


carros1 = {"modelos":["ka", "celta", "corsa"], "preco": [10,20,30], "potencia": [2,201,301]}
carros2 = {"modelos":["ka", "celta", "corsa"], "cor":["prata","preto","vermelho"],"km":[1000,2000,3000]}

uniao = {}

for key in carros1.keys():
    uniao[key] = carros1[key]

for key in carros2.keys():
    if key not in uniao.keys():
        uniao[key] = carros2[key]

print(pd.DataFrame(uniao))
