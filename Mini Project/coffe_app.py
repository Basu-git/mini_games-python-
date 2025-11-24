print("---Welcome to out cafe-----")
class coffeeapp:
    def __init__(self):
        self.menu={"cappucino":10,"filtercoffe":8,"coldcoffe":15,"bread":5}
        self.sales=0
        self.last_order=None #store last order of recepient
    
    #Show coffee menu
    def show_menu(self):
        print("\n--- Menu Items--- ")
        for coffee,price in self.menu.items():
            print(f"{coffee}:${price}")
    #Take order from the User
    def take_order(self):
        self.show_menu()
        choice=input("\n Enter Your choice: ").lower()
        
        if choice in self.menu:
            price=self.menu[choice]
            print(f"{choice} is served ")
            self.sales+=price
            self.last_order=(choice,price)
        else:
            print("Your order is not available ")
            
    #printing reciept for last order
    def printing_recipet(self):
        if not self.last_order:
            print("\n Not ordered anything order wht do u want")
        else:
            coffee,price=self.last_order
            print(f"Item : {coffee}")
            print(f"Price : ${price}")
            print("---------------------")
            
    #Total sales
    def total_sales(self):
        print(f"\n Total Sales : {self.sales}")
        
        
    def run(self):
        while True:
            print("---Choose Option----")
            print("\n1. Show Menu")
            print("\n2. Take Order")
            print("\n3.Print Reciept")
            print("\n4.Show Total sales")
            print("\n5. Exit")
            opt=input("Choose Your Option: ")
            if opt=="1":
                  self.show_menu()
            elif opt=="2":
                self.take_order()
            elif opt=="3":
                self.printing_recipet()
            elif opt=="4":
                self.total_sales()
            elif opt=="5":
                print("Than YOu Visit Agin")
                break
a=coffeeapp()
a.run()