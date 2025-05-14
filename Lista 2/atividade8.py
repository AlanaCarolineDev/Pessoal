# Este programa calcula a altura de um prédio utilizando a proporção das sombras.  

# Solicita que o usuário insira sua altura em metros  
sua_altura = float(input("Digite sua altura em metros: "))  

# Solicita que o usuário insira o comprimento da sua sombra em metros  
sua_sombra = float(input("Digite o comprimento da sua sombra em metros: "))  

# Solicita que o usuário insira o comprimento da sombra do prédio em metros  
sombra_predio = float(input("Digite o comprimento da sombra do prédio em metros: "))  

# Calcula a altura do prédio com base nas sombras  
altura_predio = (sua_altura * sombra_predio) / sua_sombra  

# Exibe uma linha de separação  
print("-" * 50)  

# Exibe a altura do prédio  
print("A altura do prédio é:", round(altura_predio, 2), "metros")  

# Exibe outra linha de separação  
print("-" * 50)  