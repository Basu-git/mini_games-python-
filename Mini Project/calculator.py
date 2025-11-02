#Create Simple calculator
def Sum(num1,num2):
    result=num1+num2
    print(f"The Result is:{result}")
def sub(num1,num2):
    result=num1-num2
    print(f"The Result is:{result}")
def mul(num1,num2):
    result=num1*num2
    print(f"The Result is:{result}")
def div(num1,num2):
    result=num1*num2
    print(f"The Result is:{result}")
def menu():
    print("1.Addition of two numbers: ")
    print("2.Substraction of two numbers: ")
    print("3.Multiplication of two numbers: ")
    print("4.Division of two numbers: ")
    print("5.Exit")
menu()

while True:
    choice=input("Enter your choice: ")
    if choice=="1":
         num1,num2=map(int,input("Enter Two numbers: ").split())
         Sum(num1,num2)
    elif choice=="2":
         num1,num2=map(int,input("Enter Two numbers: ").split())
         sub(num1,num2)
    elif choice=="3":
         num1,num2=map(int,input("Enter Two numbers: ").split())
         mul(num1,num2)
    elif choice=="4":
         num1,num2=map(int,input("Enter Two numbers: ").split())
         div(num1,num2)
    elif choice=="5":
        break
    else:
        print("Invalid Choice!!!")
    menu()

        
    