#Numeros Primos:
from time import sleep
numero = int(input("Valor Limite:"))
tot = 0
for n in range(1, numero + 1):
    if numero % n == 0:
        print(f'\033[30m{n}', end='')
        tot += 1
    else:
        print(f'\033[33m{n}', end='')
print(f"\nO número {numero} foi divisivel {tot} vezes por isso..")
sleep(2)
if tot == 2:
    print("Ele é primo")
else:
    print("Ele não é primo") 