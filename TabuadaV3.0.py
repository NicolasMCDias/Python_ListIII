 #Ex.67:Tabuada v3.0
while True:
  num = int(input("Ver tabuada de qual valor:"))
  if num < 0:
    print("Até a proxima !")
    break
  else: 
    print('==' * 30)
    for ta in range(1,11):
      print(f"{num} x {ta} = {num * ta}")
    print('==' * 30)