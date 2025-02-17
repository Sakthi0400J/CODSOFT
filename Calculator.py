class calculator:
    def __init__(self,data,ele):
        self.data=data
        self.ele=ele
        
    def add(self):
        print(self.data+self.ele)
        
    def sub(self):
        print(self.data-self.ele)
    
    def mul(self):
        print(self.data*self.ele)
        
    def div(self):
        print(float(self.data/self.ele))
        
    






a=int(input("Enter First number:"))
b=int(input("Enter Second number:"))

abd=calculator(a,b)

print("\nCALCULATOR")
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")



while True:
    choice=int(input("enter your choice:"))
    
    if choice == 1:
        abd.add()
    elif choice == 2:
        abd.sub()
    elif choice == 3:
        abd.mul()
    elif choice == 4:
        abd.div()
    else:
        break







