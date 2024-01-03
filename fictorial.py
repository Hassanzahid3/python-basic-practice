#program to generate the factorial of the number:

number = int (input ("Enter the number"))
factorial=1;
if number==0:
  print("Factorial of 0 is   1")

elif number< 0 :
  print("Factorial of given number does not exist")

else:

    for i in range(1, number+1 ):
     factorial= factorial*i
    print("Factorial")

# n * factorial(n - 1)

