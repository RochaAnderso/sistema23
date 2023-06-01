estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50]  
}

total = 0
print("Vendas:\n")

while True:
    produto = input("Nome do produto (fim para sair): ")

    if produto == "fim":
        break

    produto = produto.lower()  # Converter para letras minúsculas

    if produto in estoque:
        quantidade = int(input("Quantidade: "))

        estoque_disponivel = estoque[produto][0]

        if quantidade <= estoque_disponivel:
            preco = estoque[produto][1]
            custo = preco * quantidade
            print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print("Quantidade solicitada não disponível")
    else:
        print("Nome de produto inválido")

print("\nTotal: R$ {:.2f}".format(total))