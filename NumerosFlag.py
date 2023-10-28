#Ex.66: Varios números com flag
soma = cont = 0
while True:
  num = int(input("Digite um valor (999 para parar): "))
  if num == 999:
    break
  cont = cont + 1
  soma = soma + num
print(f"foram digitados {cont} valores e a soma deles deu {soma}")