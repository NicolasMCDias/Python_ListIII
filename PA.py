#Progressão Aritmetica:
primeiro = int(input("a1: "))
num = int(input("Tamanho da P.A.:"))
razao = int(input("Valor da razão:"))
for n in range(primeiro,num + razao,razao):
    print(n,end=' ')