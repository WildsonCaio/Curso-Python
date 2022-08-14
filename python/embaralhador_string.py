import random

letras =(input("Insira palavra para embaralhar: "))  #aqui inserir input
mixer = ''.join(random.sample(letras,len(letras)))
print(mixer)