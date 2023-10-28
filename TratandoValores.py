#Ex.64:Tratando varios valores v1.0
num = cont = soma = 0
while num != 999:
  num = int(input('digite valores [999 para parar]: '))
  soma += num
  cont += 1
print(f'Você digitou {cont - 1} números e a soma destes valores é de {soma - 999}')