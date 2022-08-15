contador=0
vel=0
des=(-5)
nome_piloto=str("piloto")
hora_rodada=0
inf=(nome_piloto, vel, hora_rodada)
dirigindo=False

def acelerar():
    global vel
    vel+=5
    return vel

def desacelerar():
    vel-=5

def informacoes():
    print(f"Informações: {inf}")

def parar():
    global dirigindo
    dirigindo=True
    
while True:
    acelerar()
    if acelerar>100:
        print(vel)
        
    contador+=1