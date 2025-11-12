#Write a Python program using a while loop to find the sum of first n natural numbers.
num = int(input("Enter a number:"))
if num < 0:
  print("Enter a number")
else:
  sum_numbers = 0
  counter = 1
  while counter <= num:
    sum_numbers += counter
    counter += 1
  print("the sum of natural number is: ",sum_numbers)
