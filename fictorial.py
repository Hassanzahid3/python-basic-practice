#program to generate the factorial of the number:
factorial=1;
number = int (input ("Enter the number"))

if number==0:
  print("Factorial of 0 is   1")

elif number< 0 :
  print("Factorial of given number does not exist")

else:

  for i in range(1, number+1 ):
     factorial= factorial*i
     
  print("The Factorial of give number is"  ,factorial)
    
    #4
    #1, 4
    #1,1
    #1,2
   # 1,3
   # 1,4
    #