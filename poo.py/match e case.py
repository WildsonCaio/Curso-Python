def linha():
    print('-'*40)

raca = (input("Qual sua raça: "))
match raca:

    case "humano":
        linha()
        print(f"Classe = {raca} \nStrenght = 5 \nAgility = 5 \nIntelligence = 5 \nCharisma = 5")
        linha()
    case "guerreiro":
        print(f"Classe = {raca} \nStrenght = 10 \nAgility = 2 \nIntelligence = 0 \nCharisma = 0")
        linha()
    case "bruneca":
        print(f"Classe = {raca} \nStrenght = 10 \nAgility = 8 \nIntelligence = 9 \nCharisma = 8")
        linha()


# guerreiro força +10 agilidade +2 iinteligencia +0 carisma +0
# humano +5 em tudo)

# classe = ''
# strenght = 0
# agility = 0
# intelligence = 0
# charisma = 0
# guerreiro força +10 agilidade +2 iinteligencia +0 carisma +0
# humano +5 em tudo
