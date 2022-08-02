#SEXO
f = "f"
m = "m"

#tamanho nome
name = "123"

#estado civil
solteiro = "s"
casado  = "c"
viuvo   =  "v"
divorciado  = "d"


nome = str (input("Qual seu nome?"))
while len(nome) <3:
    nome = str input ("Insira nome valido")


idade = int (input("Qual sua idade?"))
if idade > 0 and idade < 150:
    print ("Idade valida")

salario = float (input("Qual seu salario?"))
if salario > 0:
    print ("Salario válido")


sexo = str (input("Qual seu sexo?"))
if sexo == "m":
    print("é masculino")
elif sexo == "f":
    print("é feminino")

estado_civil = str (input("Qual estado civil?"))
