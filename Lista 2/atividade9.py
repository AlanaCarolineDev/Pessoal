# Solicita ao usuário a quantidade de litros de refresco desejada
X = float(input("Digite a quantidade de litros de refresco que deseja fazer: "))

# Proporções
partes_agua = 8
partes_suco = 2
total_partes = partes_agua + partes_suco

# Calcula litros de água e suco
litros_agua = (partes_agua / total_partes) * X
litros_suco = (partes_suco / total_partes) * X

# Exibe os resultados com uma linha separadora
print("_"*50)
print(f"\nPara fazer {X} litros de refresco, você precisa de:")
print(f"{litros_agua:.2f} litros de água mineral")
print(f"{litros_suco:.2f} litros de suco de maracujá")
print("_"*50)