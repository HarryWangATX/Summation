def summation(x):
  output_number = float((x * (x + 1))/2)
  print(str(output_number))
    
while (True):
  output_number = 0
  x = float(input("Enter a number: "))

  summation(x)

  y = input("Would you like to keep using this? ")

  if (y == "Yes") or (y == "yes"):
    a = 0
  else:
    break

print("Have a nice day!")
