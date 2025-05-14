soma = 0 
n = 3 
for i in range(1, n + 1):
    numero = float(input(f"Digite o número {i} número:"))
    soma += numero
    multiplicacao = soma / n 
    print("A média dos numeros digitado é:", multiplicacao)
    