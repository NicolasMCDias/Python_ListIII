#Ex.60:Calculo de fatorial
num = int(input('Valor p/ calculo fatorial: '))
c = num
f = 1
print(f'CALCULANDO {num}!:')
while c > 0:
  print(f'{c}', end=' ')
  print(' x 'if c > 1 else ' = ', end=' ')
  f *= c
  c -= 1
print(f'{f}')