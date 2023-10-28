#Ex.53:Detector de palindromo
frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)- 1, -1, -1):
  inverso += junto[letra]
print(inverso,':',junto, end=' ')
if inverso == junto:
  print('temos um palindromo')
else:
  print('Não temos um palindrômo')