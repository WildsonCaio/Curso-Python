preco = float(input("Quanto você ganha por hora? "))
hora =  float(input("Quantas horas você trabalhou no mes? "))

salario = float (preco*hora)
sind = float    (0.05*salario)
inss = float    (0.08* salario)
ir = float      (0.11* salario)
salarioliquido = float (((salario-ir)-inss)-sind)

print ("Seu salario bruto:R$" , (salario))
print ("Seu imposto de renda é:" , (ir))
print ("INSS R$:" , (inss))
print ("Sindicato R$:" , (sind))
print (("Salario liquido R$:") , (salarioliquido))