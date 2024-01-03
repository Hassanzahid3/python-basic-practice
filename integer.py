#write a program to take the user input and generate prime number

lower = int(input("Enter the lower limit"))
uper = int(input("Enter the uper limit"))

for i in range ( lower,  uper+1 ):
    if i>1:
     for j in range (2, i):
        if i % j == 0:
         break
     else:
        print(j)


    