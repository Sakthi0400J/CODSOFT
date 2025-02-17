class task:
    def __init__(self,key,status):
        self.key=key
        self.status=None

class Task_manager:
    def __init__(self):
        self.tasks=[]
        
    def append(self,data):
        
        new_node=task(data,None)
        self.tasks.append(new_node)
        
    def completed(self,number):
        
        node=self.tasks[number]
        node.status="COMPLETED"
        print("UPDATED")
        
    def print_list(self):
        print(self.tasks)
        a=1
        for i in self.tasks:
            print(a,"value:",i.key,"\nStatus:",i.status)
            a+=1
            
            
print("\nTo-Do List Application")
print("1. Add Task")
print("2. List Tasks")
print("3. Completed Task")
print("4. Exit")
        
        

abd=Task_manager()            
while True :
    choice=int(input("Enter Your Choice:"))
    
    
    if choice == 1:
        data=input("Enter Task Name:")
        
        abd.append(data)
    elif choice == 2:
        
        abd.print_list()

    elif choice == 3:
        number=int(input("Enter the Task number"))
        
        abd.completed(number)    
    elif choice == 4:
        break   
