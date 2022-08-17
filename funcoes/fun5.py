def is_prime(number):
    for i in range(2,number):
        if(number%i)==0:
            return False
    return True

numero_primo = int (input('Insira numero para saber se é primo: '))
print(is_prime(numero_primo))