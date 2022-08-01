
matutino = str ("M")
vespertino = str ("V")
noturno = str ("N")

turno = str (input("Qual turno você estuda? Digite M-Matutino, V-Vespertino ou N- Noturno."))

if turno == matutino:
    print ("Bom Dia!")
    
elif turno == vespertino:
    print ("Boa Tarde!")
    
elif turno == noturno:
    print ("Boa Noite!")
    
elif turno != matutino and turno != vespertino and turno != noturno:
    print ("Esse é um turno inválido")

