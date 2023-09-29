lista = ['abc']
"""
while True:
    try:
        i = int(input("Diga um número: "))
        print(lista[i])
        print("1" + 1)
        break
    except ValueError:
        print("Deve ser um número inteiro.")
    except IndexError:
        print(f"Além de inteiro, deve ser entre 0 e {len(lista)-1}")
    except Exception as e:
        print(e)

while True:
    try:
        i = int(input("Diga um número: "))
        print(lista[i])
    except ValueError:
        print("Deve ser um número inteiro.")
    except IndexError:
        print(f"Além de inteiro, deve ser entre 0 e {len(lista)-1}")
    except Exception as e:
        print(e)
    else:
        print("Operação realizada com sucesso!")
        break

while True:
    try:
        a = int(input("1 numero: "))
        b = int(input("2 numero"))
        print(b/a)
        break
    except ZeroDivisionError:
        print("Não posso dividir por zero!")
    except ValueError:
        print("Digite um número inteiro!")

dic = {
    'são paulo' : 'campeão',
    'palmeiras' : 'sem mundial',
    'corinthians' : 'sem libertadores não ganha mundial',
    'santos' : 'idoso rebaixado'
}
while True:
    try:
        time = input("Diga pra que time você torce: ")
        print(f"Você é {dic[time]}")
        break
    except KeyError:
        print("Digiet um time válido")

dic = {
    1 : 'um',
    2 : 'dois',
    3 : 'três'
}

while True:
    try:
        numero = int(input(f"Digite um dos números: {dic.keys()}: "))
        print(dic[numero])
        break
    except KeyError:
        print(f"Tem que ser um dos números: {dic.keys()}")
    except ValueError:
        print("Tem que ser um número inteiro")
"""
dic = {
    1 : ['um', 'uno', 'one'],
    2 : ['dois', 'dos', 'two'],
    3 : ['três', 'tres', 'three']
}
idiomas = ['1 - portugues', '2 - espanhol', '3 - ingles']

while True:
    try:
        numero = int(input(f"Digite um dos números: {list(dic.keys())}: "))
        print(f"Número escolhido: {dic[numero]}")
        idioma = int(input(f"Digite o idioma desejado: {idiomas}: "))
        print(dic[numero][idioma-1])
        break
    except KeyError:
        print(f"Tem que ser um dos números: {list(dic.keys())}")
    except IndexError:
        print(f"Tem que ser dos idiomas: {idiomas}")
    except ValueError:
        print("Tem que ser um número inteiro")
