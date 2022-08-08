from pip._vendor import requests

response=requests.get('https://servicodados.ibge.gov.br/api/v2/censos/nomes/Joao').json()
print (response[0]['res'][3])