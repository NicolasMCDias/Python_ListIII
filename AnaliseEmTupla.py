#Ex 74: Analizando dados em um tupla
par = 0
num = (int(input("Digite um numero:")),int(input("digite outro numero")),int(input("mais um: ")), int(input("mais um: ")), int(input("mais um: ")), int(input("o ultimo: ")))
print(f"Você digitou ==> {num}")
print(f"O número 9 apareceu {num.count(9)} vezes")
print(f"a primeira aparição do 3 é na {num.index(3) + 1}º posição")
for i in num:
  if i % 2 == 0:
    par = par + 1
print(f"E apareceram {par} numeros pares")