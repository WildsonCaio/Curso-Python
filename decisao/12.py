salario = float (input("Insira seu usuario "))

ir1 = salario*0.05
ir2 = salario*0.10
ir3 =salario*0.20

sind =salario*0.03
fgts =salario*0.11
inss =salario*0.10


if salario <= 900:
    print (f"o salário bruto: {salario}")
    print ("INSS:" , (inss))
    print ("FGTS:", (fgts))
    print ("Total de desconto:" , (inss+fgts))
    print ("Salário liquido:" , (salario-inss))


elif salario > 900 and salario <=1500:
    print (f"o salário bruto: {salario}")
    print ("INSS:" , (inss))
    print (f"FGTS:, {(fgts):.2f}")
    print ("IR:", (ir1))
    print ("Total de desconto:" , (inss+fgts+ir1))
    print ("Salário liquido:" , (salario-inss))


elif salario > 1500 and salario <=2500:
    print (f"o salário bruto: {salario}")
    print ("INSS:" , (inss))
    print (f"FGTS: {(fgts):.2f}")
    print ("IR:", (ir2))
    print ("Total de desconto:" , (inss+fgts+ir2))
    print ("Salário liquido:" , (salario-inss))


elif salario > 2500:
    print (f"o salário bruto: {salario}")
    print ("INSS:" , (inss))
    print ("FGTS:", (fgts))
    print ("IR:", (ir3))
    print ("Total de desconto:" , (inss+fgts+ir3))
    print ("Salário liquido:" , (salario-inss))
