#Ex.62:Progressão aritmerica v3.0
p = int(input('primeiro termo:'))
r = int(input('razão da PA: '))
t = p
total = 0
mais = 10
cont = 1
while mais != 0:
  total = total + mais
  while cont <= 10:
    print(f'{t} ->', end=' ')
    t = t + r
    cont += 1
  print('PAUSA!')
  mais = int(input('deseja colocar mais quantos valores: '))
print(f'A sequencia teve um total de {total} termos')