#Ex.56:Analisador completo
from math import trunc
for p in range(1,5):
  print(f'----{p}º Pessoa----')
  nome = input('NOME: ').strip()
  idade = int(input('IDADE: '))
  sexo = input('sexo [M]/[F]: ').strip()[0]
  somatoria =+ idade
  if p == 1 and sexo in 'Mm':
    maioridade = idade
    nomevelho = nome
  if sexo in 'Mm' and idade > maioridade:
    maioridade = idade
    nomevelho = nome
  if sexo in 'Ff' and idade < 20:
    fidade20 =+ 1
media = somatoria / 4
print(f'a media da idade do grupo é de {trunc(media)}')
print(f'O homem mais velho tem {maioridade} anos e se chama {nomevelho}')
print(f'E à {fidade20} mulheres com menos de 20 anos')
