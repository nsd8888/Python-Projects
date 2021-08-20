import sys
from appexcept import DepositError,WithDrawError,NegativityError
from Operations import Deposit,withdraw,BalanceEq
while(True):
    print("1. Deposite")
    print("2. WithDraw")
    print("3. Balance Enquiry")
    print("4. Exit")
    try:
        ch = int(input("Enter Your choice For The operation: "))
        if ch == 1:
            try:
                Deposit()
            except ValueError:
                print("Dont Enter the Alphabets/Special Symbol/Alpha-Numeric")
            except DepositError:
                print("Dont Enter the Negative or Zero Amount")
        elif ch == 2:
            try:
                withdraw()
            except ValueError:
                print("Dont Enter the Alphabets/Special Symbol/Alpha-Numeric")
            except WithDrawError:
                print("Insuffient Balance.")
            except NegativityError:
                print("Dont Enter Negative/zero Amount")

        elif ch == 3:
            BalanceEq()
        elif ch == 4:
            print("Thank You For Using This App")
            sys.exit()
        else:
            print("You Entered Wrong Choice")

    except ValueError:
        print(" Dont Enter The Alphabets/ Special Symbol/Alpha-Numerics")
    finally:
        print(" The Programme is executed successfully.")

