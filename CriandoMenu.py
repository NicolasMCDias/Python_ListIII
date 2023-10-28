#Ex.59:Criando um menu de opçoes
n1 = float(input('primeiro valor: '))
n2 = float(input('Segundo valor: '))
opçoes = 0
while opçoes != 5:
  print('escolha:\n[1]Somar\n[2]Multiplicar\n[3]Media\n[4]Novos valores\n[5]Sair do programa')
  opçoes = int(input('Qual será de sua escolha: '))
  if opçoes == 1:
    print(f'{n1}+{n2} = {n1 + n2}')
  elif opçoes == 2:
    print(f'{n1}x{n2}={n1 * n2}')
  elif opçoes == 3:
    print(f'sua media é de {n1 + n2 / 2}')
  elif opçoes == 4:
    n1 = float(input('Primeiro valor: '))
    n2 = float(input('Segundo valor: '))
  elif opçoes == 5:
    print('Finalizando programa...')