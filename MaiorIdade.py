#Ex.54:grupo de maior idade
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for n in range(1,8):
  ano = int(input(f'Ano de nacimento da {n}º pessoa:'))
  idade = atual - ano
  if idade >= 18:
    totmaior += 1
  else:
    totmenor += 1
print(f'{totmenor} ainda estão na menor idade')
print(f'{totmaior} pessoas atingiram a maior idade')