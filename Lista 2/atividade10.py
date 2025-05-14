# Solicitar ao usuário o raio e a altura
raio = float(input("Digite o raio da caixa d'água (em metros): "))
altura = float(input("Digite a altura da caixa d'água (em metros): "))

print("-" * 50)

# Calcula o volume (usando pi aproximadamente 3,14159)
pi = 3.14159
volume = pi * (raio ** 2) * altura

# Exibir o resultado
print("O volume da caixa d'água cilíndrica é de", volume, "metros cúbicos.")

print("-" * 50)