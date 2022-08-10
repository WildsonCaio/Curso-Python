from pip._vendor import requests

cidade=(input("Insira cidade para verificar condições climáticas: "))
response=requests.get(f'https://weather.contrateumdev.com.br/api/weather/city/?city={cidade}').json()
temp_atu = (response['main']['temp'])
temp_min = (response['main']['temp_min'])
temp_max = (response['main']['temp_max'])
descr_ceu = (response['weather'][0]['description'])
vel_ven = (response['wind']['speed'])
print(f"Na cidade de {cidade}, {descr_ceu}. \nVentos de {vel_ven} km/h. \nTemperatura atual: {temp_atu}. \nTemperatura mínima: {temp_min}. \nTemperatura máxima: {temp_max}.\n")

#salva dados 
data=open('clima.txt','a')
data.write(f"{cidade},{temp_atu},{descr_ceu}\n")




