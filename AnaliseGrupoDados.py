#Ex.69: Análise de dados do grupo
idadet = 0
masculino = 0
feminino = 0
while True:
  sexo = input("Qual é o sexo : Masculino [M] / Feminino [F]:").strip().upper()[0]
  idade = int(input("Idade: "))
  if sexo == "M":
    masculino = masculino + 1
  if sexo == "F" and idade < 20:
    feminino = feminino + 1
  if idade >= 18:
    idadet = idadet + 1
  cont = str(input("Vai continuar? [S/N]: ")).strip().upper()[0]
  if cont == "N":
    break
print(f"Têm {idadet} pessoas com mais de 18 anos")
print(f"A {masculino} Homens cadastrados")
print(f"A {feminino} Mulheres com menos de 20 anos")