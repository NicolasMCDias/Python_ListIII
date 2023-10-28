#Ex.61:Progressão aritmerica v2.0
p = int(input('primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = p
cont = 1
while cont <= 10:
  print(f'{termo} ->', end=' ')
  termo += razao
  cont += 1
print('FIM!')
