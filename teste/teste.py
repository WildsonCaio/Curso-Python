from pip._vendor import requests
nome=str (input("Insira um nome: "))

response=requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}').json()


for i in (response[0]['res']):
    print(i)    