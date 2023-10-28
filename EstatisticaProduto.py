#Ex.70: Estatísticas em produtos
maismil = 0
barato = 0
while True:
  produnome = input("Nome do produto: ")
  preço = float(input("Preço do produto: "))
  barato = preço
  nobarato = produnome
  tot = tot + preço
  if preço >= 1000:
    maismil = maismil + 1
  if preço < barato:
    barato = preço 
    nobarato = produnome
  cont = input("continua [S/N]: ").strip().lower()
  if cont == "n":
    break
print(f"Total gasto:R${tot:.2f}")
print(f"teve {maismil} produtos que custavam de 1000 pra cima")  
print(f"o mais barato foi o [{nobarato}] com um preço de R${barato:.2f}")