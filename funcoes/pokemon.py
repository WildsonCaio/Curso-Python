#https://pokeapi.co/api/v2/pokemon/{id or name}/
#passar nome ou id do pokemon
#nome do pokemon ou mensagem de erro
#imagem ou gif ou sprit geração 5
#tipo do pokemon
#tamanho 
#peso

from pip._vendor import requests

def linha():
    return('-'*40)

nome=(input("Insira nome ou ID do pokemon: "))
response=requests.get(f'https://pokeapi.co/api/v2/pokemon/{nome}/').json()

name = response['name']
linha()


image = (response['sprites']['versions']['generation-v']['black-white']['animated']['back_default'])

tipo = (response['types'][0]['type']['name'])

tamanho = (response['height'])

peso = (response['weight'])

print(f"Nome: {name}\n{linha()}\nImagem: {image} \n{linha()}\nTipo: {tipo}\n{linha()} \nTamanho: {tamanho} centímetros\n{linha()} \nPeso: {peso} gramas\n{linha()}")
