#Ex.58:Jogo de adivação v2.0
from random import randint
comp = randint(1,10)
player = int(input('tente adivinhar o numero que estou pensando de 1 à 10: '))
while player != comp:
  player = int(input('ERROU!! tente novamente (1 à 10)'))
  erro =+ 1
print(f'ACERTOU!! era o número {comp}, você errou {erro} vezes')