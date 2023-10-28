#Ex.57:Validação de dados
s = str(input('Insirá seu sexo[M/F]: ')).strip().upper()[0]
while s not in 'MmFf':
  s = str(input('Valor invalido, coloque novamento seu sexo[M/F]')).strip().upper()
print('Guardando informação...')