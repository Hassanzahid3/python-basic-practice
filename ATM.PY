
print("Well come to an ATM")

correct_pin =4343 ;
balance = 5000;

pin = int(input("Enter the pin")) 

if correct_pin == pin:
    print("Your password is correct")

    print("choice 1 :  Balance inquriey ")
    print("choice 2 :  Cash withrdraw ")
    print("choice 3 :  Cash Deposite ")
    print("choice 4 :   Back  ")

    choice = int(input("Enter your choice (1-4): "))
    # print("1: Balance inquriey")
    if choice == 1:
        print("your current balance is " + str(balance ))

    elif choice == 2:
     w_amount= float(input("Enter amount to widraw"))
     if w_amount >balance:
        print("Insufiicent amount")
     elif w_amount <= balance:
        print("your transcation is being process")
        print("Transcation sucesfull")
    elif choice == 3:
        d_amount=int(input("Enter amount to Deposite"))
        new_amount=balance+d_amount
        print("your current amount is " + str(new_amount))
    elif choice == 4:
        print("Thank u for using ATM")
else:
    print("Invalid pin")

