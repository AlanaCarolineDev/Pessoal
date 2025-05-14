# Ler o número inteiro
numero = int(input("Digite um número inteiro de até três dígitos: "))

# Garantir que o número esteja entre 0 e 999
if not (0 <= numero <= 999):
    print("Número fora do intervalo permitido.")
else:
    # Extrair centena, dezena e unidade
    centena = numero // 100
    resto = numero % 100
    dezena = resto // 10
    unidade = resto % 10

    # Imprimir os resultados sem f-string
    print("CENTENA =", centena)
    print("DEZENA =", dezena)
    print("UNIDADE =", unidade)