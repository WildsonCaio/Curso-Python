# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.


inc1 = 20/100
inc2 = 15/100
inc3 = 10/100
inc4 = 5/100
salario = float (input("Insira seu usuario "))



if salario <= 280:
    print ("o salário antes do reajuste:" , (salario))
    print ("o percentual de aumento aplicado:" , (inc1*100),"%")
    print ("o valor do aumento:", (salario*inc1))
    print ("o novo salário, após o aumento:" , ((inc1*salario)+salario))

elif salario > 280 and salario < 700:
    print ("o salário antes do reajuste:" , (salario))
    print ("o percentual de aumento aplicado:" , (inc2*100),"%")
    print ("o valor do aumento:", (salario*inc2))
    print ("o novo salário, após o aumento:" , ((inc2*salario)+salario))

elif salario > 700 and salario <= 1500:
    print ("o salário antes do reajuste:" , (salario))
    print ("o percentual de aumento aplicado:" , (inc3*100),"%")
    print ("o valor do aumento:", (salario*inc3))
    print ("o novo salário, após o aumento:" , ((inc3*salario)+salario))

elif salario > 1500 :
    print ("o salário antes do reajuste:" , (salario))
    print ("o percentual de aumento aplicado:" , (inc4*100),"%")
    print ("o valor do aumento:", (salario*inc4))
    print ("o novo salário, após o aumento:" , ((inc4*salario)+salario))