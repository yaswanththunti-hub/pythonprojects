import time
print("Welcome to pentagon ATM")
card =int(input("insert the card :"))
balance=1000
password=9876
if card==1:
    print("Select the language : English , Telugu ")
    language=int(input("Choose the language 1.English and 2.Telugu:"))
    if language==1:
        pin=int(input("Enter the pin :"))
        if pin==password:
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
                    if withdraw%100==0:
                        print("Your transaction being processing")
                        time.sleep(3)
                        print("please wait")
                        time.sleep(2)
                        print("Please take your amount")
                        time.sleep(1)
                        afterwithdraw=int(input("Do you want to check balance 1.yes 2.no :"))
                        if afterwithdraw==1:
                            print("Your balance is :",balance-withdraw)
                            print("Thank you visit again")
                        else:
                            print("Thank you visit again")
                    else:
                        print("Enter withdraw amount in 100's")
                else:
                    print("Insufficient balance")
            elif option==3 :
                print("Put the amount")
                deposit = int(input("Enter how much you deposited :"))
                if deposit%100==0:
                    print("Your transaction being processing")
                    print("Your transaction being processing")
                    time.sleep(3)
                    print("please wait")
                    time.sleep(2)
                    print("Successfully deposited your amount")
                    time.sleep(1)
                    afterdeposit=int(input("Do you want to check balance 1.yes 2.no :"))
                    if afterdeposit==1:
                        print("Your balance is :",balance+deposit)
                        print("Thank you visit again")
                    else:
                        print("Thank you visit again")
                else:
                    print("Put deposit amount in 100's")
            else:
                print("Enter the correct option")
        else:
            print("Entered wrong pin")
    else:
        print("Please select English option")
else:
    print("Please insert card again")
