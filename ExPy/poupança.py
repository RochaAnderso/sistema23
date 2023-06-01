depósito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))

saldo = depósito
total_juros = 0

for mês in range(1, 25):
    saldo = saldo + (saldo * (taxa / 100))
    print(f"Saldo do mês {mês} é de R${saldo:5.2f}.")
    total_juros = saldo - depósito

print(f"O ganho obtido com os juros foi de R${total_juros:8.2f}.")