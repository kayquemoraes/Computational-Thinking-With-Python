'''
lista = [4,2,6,1,7,0,3]
for i in range(len(lista)):
    n_trocas = 0
    for j in range(len(lista) - i - 1):
        if lista[j] > lista[j+1]:
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux
            n_trocas += 1
    if n_trocas == 0:
        break

print(lista)



def acha_raiz(valor, precisao):
        inicio = 0
        fim = valor
        chute = (inicio + fim)/2
        qtd = 0
        if abs(chute**2 - valor) > precisao:
            if chute**2 > valor:
                fim = chute
            else:
                inicio = chute
            chute = (inicio + fim)/2
            qtd += 1

        return chute

print(acha_raiz(25, 0.01))

def acha_raiz_recursao(valor, precisao, inicio, fim):
        chute = (inicio + fim)/2
        if abs(chute**2 - valor) > precisao:
            if chute**2 > valor:
                fim = chute
                return acha_raiz_recursao(valor, precisao, inicio, fim)
            else:
                inicio = chute
                return acha_raiz_recursao(valor, precisao, inicio, fim)

        return chute


print(acha_raiz_recursao(25, 0.01))

lista_od = [0,1,2,3,4,5,6,7]

def acha_num(lista, num, inicio, fim):
    chute = (inicio + fim)//2
    if lista[chute] == num:
        return chute
    elif lista[chute] > num:
        fim = chute
        return acha_num(lista, num, inicio, fim)
    elif lista[chute] < num:
        inicio = chute
        return acha_num(lista, num, inicio, fim)

print(acha_num(lista_od, 6, 0, len(lista_od)))


def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        lista_menor = [elem for elem in lista if elem < pivo]
        lista_maior = [elem for elem in lista if elem > pivo]
        menor_ordenada = quicksort(lista_menor)
        maior_ordenada = quicksort(lista_maior)
        ordenada = menor_ordenada + [pivo] + maior_ordenada
        print(lista_menor,pivo,lista_maior)
    return ordenada

print(quicksort([4,2,6,1,7,0,3]))

'''

