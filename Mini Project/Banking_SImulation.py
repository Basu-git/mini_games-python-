class acc:
    def __init__(self,acc_no,user_name):
        self.acc_no=acc_no
        self.user_name=user_name
        self._balance=0
    
    def check_balance(self):
        print(f"\n Balance is {self._balance}")
    def deposit(self,amt):
        if amt>=0:
            self._balance+=amt
            print(f"\n{amt} depostied succesfully,Updated balance {self._balance}")
        else:
            print("Negative and zero's amt is not allowed ")
    def withdraw(self,amt):
        if amt>=0 or amt<=self._balance:
            self._balance-=amt
            print(f"\nWithdrawal Succesful,Updated balance is {self._balance}")
        else:
            print("Negative or insufficient balance")
        
            
class savings_acc(acc):
    def calculate_intrest(self):
        intt=0.05 #5%
        intrest=self._balance*intt
        print(f"Intrest added balance {intrest}")

class current_acc(acc):
    def withdraw(self, amt):
        over_amt=1000
        if self._balance+over_amt>=amt:
             self._balance-=amt
             print(f"\nWithdrawal Succesful,Updated balance is {self._balance}")
        else:
            print("Limit is over")

class bank:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.__acc={}
    
    def create_acc(self,acc_no,user_name,type):
        if type=="savings":
            new_acc=savings_acc(acc_no,user_name)
        elif type=="current":
            new_acc=current_acc(acc_no,user_name)
        self.__acc[acc_no]=new_acc
        print("\n Account created succesfully")
        return new_acc
    def get_acc(self,acc_no):
        if acc_no not in self.__acc:
            print("\n Account not found!!")
            return None
        else:
            account = self.__acc[acc_no]
            print(f"\n ID : {account.acc_no} \t Holder Name: {account.user_name}")
            return account

a=bank("SBI","Banglore")
b=a.create_acc("1234","John","savings")
b=a.get_acc("1234")
c=a.create_acc("4321","Bobby","current")
c=a.get_acc("4321")
b.deposit(1000)
b.withdraw(500)
b.check_balance()
c.deposit(5000)
c.withdraw(2500)
c.check_balance()
c.withdraw(3500) # It allows to withdraw more than our balance with overdriven amt 1000 only
c.withdraw(4200) # It shows limit is over because the withdrawwing amt is overdrived limit 
