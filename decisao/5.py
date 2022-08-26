nota1 = float(input ("Digite nota 1: "))
nota2 = float(input ("Digite nota 2: "))
media = float((nota1+nota2)/2)

if media > 7.0 and media <10:
    print ("Aprovado")
elif media < 7.0:
    print ("Reprovado")
elif media == 10.0:
    print ("Aprovado com Distinção")
