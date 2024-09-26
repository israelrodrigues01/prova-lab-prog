import random

status = True
numerosGerados = []


def somarNumero(array):
    soma = 0
    for i in range(0, len(array)):
        soma += array[i]

    return soma


def media(array):
    soma = somarNumero(array)
    tamanho = len(array)
    return soma / tamanho


def maior(array):
    maior = 0
    for i in range(0, len(array)):
        if array[i] > maior:
            maior = array[i]

    return maior


while status:
    numero = random.randint(1, 10)
    numerosGerados.append(numero)
    somaNumeros = somarNumero(numerosGerados)

    if somaNumeros > 50:
        print("Soma de todos os número: ", somaNumeros)
        print("Número gerados:", numerosGerados)
        print("Quantidade de números gerados:", len(numerosGerados))
        print("Média dos números:", media(numerosGerados))
        print("Maior número:", maior(numerosGerados))
        status = False
