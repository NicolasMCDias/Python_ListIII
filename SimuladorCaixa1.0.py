#Ex.71: Simulador de Caixa Eletrônico 
valor_busca = int(input("Valor à sacar: "))
nota50 = valor_busca // 50
valor = valor_busca % 50
nota20 = valor // 20
valor = valor % 20
nota10 = valor // 10
valor = valor % 10
nota1 = valor // 1 
if nota50 > 0:
  print(f"{nota50} notas de 50")
if nota20 > 0:
  print(f"{nota20} notas de 20")
if nota10 > 0:
  print(f"{nota10} notas de 10")
if nota1 > 0:
  print(f"{nota1} de 1 real")