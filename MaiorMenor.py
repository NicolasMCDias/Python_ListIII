#Ex.65:Maior e menor valores
resp = "S"
soma = quant = media = maior = menor = 0
while resp in "Ss":
  numero = int(input("Digite um número:"))
  soma = soma + numero
  quant = quant + 1
  if quant == 1:
    maior = menor = numero
  else:
    if numero > maior:
      maior = numero
    if numero < menor:
      menor = numero
  resp = input("Vai continuar ? [S] [N]").upper().strip()[0]
media = soma / quant
print(f"Você digitou {quant} numeros e teve uma media de {media:.2f}")
print(f"O maior valor foi {maior} e o menor valor é {menor}")