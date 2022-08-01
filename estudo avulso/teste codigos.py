from math import ceil

cobert = int(6)
vlrLataP = int(25)
vlrLataG = int(80)
rendGalaoP = float(3.6*cobert)
rendGalaoG = float(18*cobert)
tamanho = float(input("Informe o tamanho da parede me m²: "))
qtdLataP = ceil(tamanho/rendGalaoP)
qtdLataG = ceil(tamanho/rendGalaoG)

print(f"\nOpção 1: {qtdLataP} latas de 3,6 litros ao valor de R$ {qtdLataP * vlrLataP}")
print(f"Opção 2: {qtdLataG} latas de 18 litros ao valor de R$ {qtdLataG * vlrLataG}")
if qtdLataG*rendGalaoG > tamanho * 1.1:
    melhorRendG = qtdLataG - 1
    melhorRendP = 5
    for n in range(0,5):
        if melhorRendP * rendGalaoP + melhorRendG * rendGalaoG < 1.1*tamanho:
            print(f"Opção 3: {melhorRendG} latas de 18 litros e {melhorRendP} latas de 3.6 litros terá um disperdio menor que 10% e gastará R${melhorRendG*vlrLataG+melhorRendP*vlrLataP}")
            exit()
        melhorRendP -= 1
    melhorRendP = 1
    print(f"Opção 3: {melhorRendG} latas de 18 litros e {melhorRendP} latas de 3.6 litros terá um disperdio um pouco superior a 10% e gastará R${melhorRendG*vlrLataG+melhorRendP*vlrLataP}")
else:
    print(f"A melhor opção é a 2 que sairá mais barato e terá disperdico inferior a 10% ")
