#to checks whether a number is positive or negative
num = int(input("enter an integer: "))
if num>0:
  if num % 2 == 0:
     print("the number is even and positive.")
  else:
     print("the number is odd and positive.")
elif num<0:
  if num % 2 == 0:
     print("the number is even and negative.")
  else:
     print("the number is odd and negative.")
else:
  print("the number is zero,which is even.")
