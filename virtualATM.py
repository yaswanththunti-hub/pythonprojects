print("Welcome to Bank ATM")
card =int(input("Please insert the card :"))
balance=10000
if card==1:
    print("Select the language : English , Telugu ")
    language=int(input("Choose the language 1.english & 2.Telugu:"))
    if language==1 or language==2:
        pin=int(input("Enter the pin :"))
        if pin==1234:
            print("Select the option")
            print("1.Balance enquiry ")
            print("2.Withdraw")
            print("3.Deposit")
            option=int(input("Enter the option:"))
            if option==1:
                print("Your balance is :",balance)
                print("Thank you visit again")
            elif option==2 :
                print("Enter the amount")
                withdraw=int(input())
                if balance>=withdraw:
                    print("Please take your amount")
                    afterwithdraw=int(input("Do you want to check balance 1.yes 2.no :"))
                    if afterwithdraw==1:
                        print("Your balance is :",balance-withdraw)
                        print("Thank you visit again")
                    else:
                        print("Thank you visit again")
                else:
                    print("Insufficiant balance
            else :
                print("Put the amount")
                deposit=int(input())
                print("Successfully deposited your amount")
                afterdeposit=int(input("Do you want to check balance 1.yes 2.no :"))
                if afterdeposit==1:
                    print("Your balance is :",balance+deposit)
                    print("Thank you visit again")
                else:
                    print("Thank you visit again")
        else:
            print("Entered wrong pin")
    else:
        print("Enter correct option")

else:
    print("Please insert card again")
