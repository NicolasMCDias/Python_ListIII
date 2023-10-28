#ex 73:Tuplas com times de futebol
times = ('Corinthians', 'Palmeiras','São Paulo', 'Atletico-MG', 'Botafogo', 'Santos', 'Fluminense', 'Coritiba', 'America-MG', 'Avaí', 'Internacional', 'Athetico-PR', 'Bragantino', 'Flamengo', 'Goiás', 'Cuiabá', 'Atletico-GO', 'Juventude', 'Ceará-SC', 'Fortaleza')
print(f"TUPLA: {times}")
print("=====" * 35)
print(f"Os 5 primeiros são : {times[0:5]}")
print("=====" * 35)
print(f"Os 4 ultimos são: {times[-4:]}")
print("=====" * 35)
print(f"Em ordem alfabetica: {sorted(times)}")
print("=====" * 35)
print(f"O time São Paulo esta na posição {times.index('São Paulo')}")

#ex 73: Maior e menor valores em tuplas
from random import randint
for h in range(0,6):
  valor = (randint(1,10),randint(0,10), randint(0,10), randint(0,10), randint(1,10))
print(f"valores sorteados foram ==>", end=" ")
for v in valor:
  print(f'{v}', end=" ")
print(f"\nO menor número é ==> {min(valor)}")
print(f"O maior número é ==> {max(valor)}")