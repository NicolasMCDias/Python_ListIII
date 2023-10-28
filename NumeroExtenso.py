#Ex 72: Número por extenso
extenso = ('zero', 'um', 'dois','três', 'quatro', 'cinco','seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quize', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
valor = int(input("Digíte um número entre 0 e 20:"))
while valor > 20 or valor < 0:
  valor = int(input("Tente Novamente ==> Digite um numero entre 0 e 20:"))
print(f"Por extenso ==> {extenso[valor]}")