#Ex.68:Par ou Impar
from random import randint
n=0
while True:
  player = int(input("Digite o valor: "))
  comp = randint(0, 10)
  tot = player + comp
  tipo = ' '
  while tipo not in 'PI':
    tipo = str(input("Par ou Impar ? [P/I]")).strip().upper()[0]
  print(f"Vc jogou {player} e o PC jogou {comp} Total de {tot}")
  if tipo == "P":
    if tot % 2 == 0:
      print("Você VENCEU!")
      n = n + 1
    else:
      print("Você PERDEU!")
      break
  elif tipo == "I":
    if tot % 2 == 1:
      print("Você VENCEU!")
      n = n + 1
    else:
      print("Você PERDEU!")
      break
print(f"GAME OVER ! Você venceu {n} vezes")