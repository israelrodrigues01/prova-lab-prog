numeros = []

qtdNumero = int(input("Digite a quantidade de números da lista: "))

for i in range(0, qtdNumero):
    numero = int(input(f"Número {i+1}: "))
    if numero > 10 and numero % 2 == 0:
        numeros.append(numero)


def somarNumero(array):
    soma = 0
    for i in range(0, len(array)):
        soma += array[i]

    return soma


print("\nNúmeros", numeros)
print("Soma", somarNumero(numeros))
