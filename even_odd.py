number=int(input("enter a nmber:"))
if number % 2 ==0:
    print("even")
else:
  print("odd")


while True:
  number=int(input("enter a nmber:"))
  if number % 2 == 0:
    print("even")
  else:
     print("odd")
  if input("quit? (y/n):").lower() == "y":
     break
  
  
  