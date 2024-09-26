produtos = []
precos = []
carrinho = []
indiponiveis = []

status = True


def listarProdutos(produtos, precos):
    for i in range(0, len(produtos)):
        print(f"Produto {i+1}: {produtos[i]} - R$ {precos[i]}")

    print(f"{len(produtos) + 1} - Sair da Compra")
    print("\n\n")


def listarCarrinho(carrinho):
    for i in range(0, len(carrinho)):
        print(f"Produto {i+1}: {carrinho[i][0]} - Quantidade: {carrinho[i][1]}")

    print("\n\n")


while status:
    print("Bem-vindo(a) ao SuperMercado, o que deseja:")
    print("1 - Adicionar produto")
    print("2 - Sair")

    opcao = int(input("O que deseja? "))
    print("\n\n")

    while opcao < 1 and opcao > 2:
        print("Por favor, adicione um menu existente, o que deseja:")
        print("1 - Adicionar produto")
        print("2 - Sair")

        opcao = int(input("O que deseja? "))
        print("\n\n")

    if opcao == 2:
        status = False
        break

    nome = input("Digite o nome do produto: ")
    valor = float(input(f"Digite o valor do produto {nome}: "))
    produtos.append(nome)
    precos.append(valor)

    print("\n\n")


status = True

while status:
    print("Bem-vindo(a) ao SuperMercado, o que deseja:")
    print("1 - Comprar produto")
    print("2 - Sair")

    opcao = int(input("O que deseja? "))
    print("\n\n")

    while opcao < 1 and opcao > 2:
        print("Por favor, adicione um menu existente, o que deseja:")
        print("1 - Comprar produto")
        print("2 - Sair")

        opcao = int(input("O que deseja? "))
        print("\n\n")

    if opcao == 2:
        status = False
        break

    compra = True
    while compra:
        print("=========== Lista dos Produtos e preços ===========")
        listarProdutos(produtos, precos)

        opcao = input("Qual deseja comprar ou sair? ")

        if opcao in "sair":
            status = False
            break

        escolhaProduto = -1
        if opcao in produtos:
            for i in range(0, len(produtos)):
                if opcao == produtos[i]:
                    escolhaProduto = i

        if escolhaProduto == -1:
            indiponiveis.append(opcao)
            print("Produto nao disponivel :(")
            print("\n\n")
        else:
            qtd = int(input(f"Quantos de {produtos[escolhaProduto]}? "))
            escolha = [produtos[escolhaProduto], qtd]

            carrinho.append(escolha)

        print("=========== Seu Carrinho ===========")
        listarCarrinho(carrinho)

        print("Continuar comprando? ")
        print("1 - Sim")
        print("2 - Não")

        continuar = int(input("Continuar comprando? "))
        print("\n\n")

        if continuar == 2:
            compra = False
            break


def total(carrinho, produtos, precos):
    soma = 0
    for i in range(0, len(carrinho)):
        for j in range(0, len(produtos)):
            if carrinho[i][0] == produtos[j]:
                valorProduto = precos[j] * carrinho[i][1]
                if carrinho[i][1] > 5:
                    desconto = valorProduto - ((10 / 100) * valorProduto)
                    valorProduto = desconto

                soma += valorProduto

    return soma


print("=========== Seu Carrinho ===========")
listarCarrinho(carrinho)
print("\n\n")

print(total(carrinho, produtos, precos))
print(f"Produtos nao disponiveis {indiponiveis}")
print(f"{len(indiponiveis)} Produtos nao disponiveis")
