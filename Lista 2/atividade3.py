  
print("Seja Bem-vindo!")  
  
print("-" * 20)   
valor_hora_normal = 10.00 
valor_hora_extra = 15.00    

horas_normais = float(input("Digite o número de horas normais trabalhadas: "))  
horas_extras = float(input("Digite o número de horas extras trabalhadas: "))    
 
print("-" * 20)  


salario_bruto = (horas_normais * valor_hora_normal) + (horas_extras * valor_hora_extra)  
  
desconto_impostos = salario_bruto * 0.10  


  
salario_liquido = salario_bruto - desconto_impostos  

  
print(f"\nSalário Bruto: R${salario_bruto:.2f}")  
 
print(f"Salário Líquido: R${salario_liquido:.2f}") 