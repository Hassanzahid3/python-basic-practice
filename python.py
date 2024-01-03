
print("Well come to an ATM")

correct_pin =4343 ;
balance = 5000;

pin = input("Enter the pin")
pin= int(pin)

if correct_pin == pin:
    print("Your password is correct")

    choice = int(input("Enter your choice (1-4): "))
    print("1: Balance inquriey")
    if choice == 1:
        print("your current balance is " + str(balance ))

    print("2: Cash withrdraw")
    if choice == 2:
      wamount = int(input("Enter the amount you want to withdraw" ))

    if wamount <= balance:
        print("Amount withdraw sucessfully")
    else:
        print("insifiicent amount ")
    print("4: Back")

else:
    print("Invalid pin")

