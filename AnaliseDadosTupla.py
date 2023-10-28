#Analise de dados em uma tupla
listagem = ("Lapis",1.78,
            "Borracha",2.55,
            "Caderno",5.89,
            "Cola bastao",8.99)
print('---'*15)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('---'*15)

for pos in range(0,len(listagem)):
  if pos % 2 == 0:
    print(f"{listagem[pos]:.<30}" , end='')
  else:
    print(f"{listagem[pos]:>7.2f}")