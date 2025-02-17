class node:
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
    

class contact_book:
    def __init__(self):
        self.list=[]
        
    def add(self,name,phone,email,address):
        new_node=node(name,phone,email,address)
        self.list.append(new_node)
        print("ADDED")
        
    def print_list(self):
        for i in self.list:
            print(i.name,"\n",i.phone)
            
    def search(self,name):
        for i in self.list:
            if i.name ==name:
                print("FOUND")
                print(i)
    
    def update(self,name,new_phone,new_email,new_address):
        for i in self.list:
            if i.name==name:
                if new_phone:
                    i.phone=new_phone
                if new_email:
                    i.phone=new_email
                if new_address:
                    i.phone=new_address
            print("UPDATED")
    
    def delete(self,name):
        for i in self.list:
            if i.name ==name:
                self.list.remove(i)
                print("REMOVED")



print("\nContact Management System")
print("1. Add Contact")
print("2. View Contacts")
print("3. search Contacts")
print("4. update Contact")
print("5. delete Contacts")
print("6. exit")




abd=contact_book()


    
while True:
    choice=int(input("Enter your choice:"))
    
    if choice == 1:
        a=input("name:")
        b=int(input("number:"))
        c=input("email:")
        d=input("address:")
        abd.add(a,b,c,d)
       
    
    if choice ==2:
        abd.print_list()
        
    if choice == 3:
        ele=input("Enter name to be searched")
        abd.search(ele)
        
    if choice == 4:
        a=input("Enter name")
        b=input("Enter new number to be changed:")
        c=input("Enter new email to be changed:")
        d=input("Enter new address to be changed:")
        abd.update(a,b,c,d)

        
    if choice ==5  :
        ele=input("enter name to delete:")
        abd.delete(ele)
        
    if choice==6:
        break
        
        
        
        
        
        
        
        
        
        
        
        
