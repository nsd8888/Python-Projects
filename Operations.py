
from appexcept import DepositError,WithDrawError,NegativityError

acc_bal=500.00
def Deposit():
    n=float(input("Enter The Amount To Deposit: "))
    if n<=0:
        raise DepositError
    else:
        global acc_bal
        acc_bal=acc_bal+n
        print("Your Account is Credited with Amount {}".format(n))
        print("You Account Balance is {}".format(acc_bal))

def withdraw():
    global acc_bal
    n=float(input("Enter the Amount to withdraw: "))
    if n>=acc_bal:
        raise WithDrawError
    else:
        if n<=0:
            raise NegativityError
        else:
            acc_bal = acc_bal - n
            print("Your account is Debited with an amount {}".format(n))
            print("Your account balance is {}".format(acc_bal))

def BalanceEq():
    print("Your Account Balance is {}".format(acc_bal))