def gerar_dicionario(frase):
    dicionario = {}
    for caractere in frase:
        if caractere in dicionario:
            dicionario[caractere] += 1
        else:
            dicionario[caractere] = 1
    return dicionario

frase = input("Digite uma frase: ")
dicionario = gerar_dicionario(frase)
print(dicionario)