#Ex.55:Maior e menor da sequencia
maior = 0
menor = 0
for p in range(1, 6):
  peso = float(input('peso da {}º pessoa: '.format(p)))
  if p == 1:
    maior = peso
    menor = peso
  else:
    if peso > maior:
      maior = peso
    if peso < maior:
      menor = peso
print(f'O maior peso é {maior}kg')
print(f'O menor peso é {menor}kg')
