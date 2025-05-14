# Este programa calcula o total economizado em reais com base nas moedas de Pedrinho.  

# Solicita a quantidade de cada tipo de moeda  
print("-" * 50)  
num_moedas_1_real = int(input("Digite a quantidade de moedas de 1 real: "))  
num_moedas_50_centavos = int(input("Digite a quantidade de moedas de 50 centavos: "))  
num_moedas_25_centavos = int(input("Digite a quantidade de moedas de 25 centavos: "))  
num_moedas_10_centavos = int(input("Digite a quantidade de moedas de 10 centavos: "))  
num_moedas_5_centavos = int(input("Digite a quantidade de moedas de 5 centavos: "))  
num_moedas_1_centavo = int(input("Digite a quantidade de moedas de 1 centavo: "))  

# Converte a quantidade de moedas para o valor total em reais  
total_reais = (num_moedas_1_real * 1) + \
              (num_moedas_50_centavos * 0.50) + \
              (num_moedas_25_centavos * 0.25) + \
              (num_moedas_10_centavos * 0.10) + \
              (num_moedas_5_centavos * 0.05) + \
              (num_moedas_1_centavo * 0.01)  

# Exibe o total economizado  
print("-" * 50)  
print("O total economizado em reais é: R$ {:.2f}".format(total_reais))  
print("-" * 50)  