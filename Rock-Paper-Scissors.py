import random



sample=['rock','paper','scissor']
print(sample)
user_points=0
comp_points =0


while True:
    if comp_points==3:
        print("computer won the match",comp_points,"-",user_points)
        break
    if user_points==3:
        print("user won the match",comp_points,"-",user_points)
        break
    user=input("Enter your choice in lowercase:")
    comp=random.choice(sample)
    print(f"user={user} computer= {comp}")
    
    
    if user == comp:
        print("DRAW")
        
    elif user=="rock" and comp=="paper":
        print("Computer wins!")
        comp_points+=1
    
    elif user=="rock" and comp=="scissor":
        print("User wins!")
        user_points+=1
    
    elif user=="paper" and comp=="rock":
        print("user wins!")
        user_points+=1
    
    elif user=="paper" and comp=="scissor":
        print("Computer wins!")
        comp_points+=1
    
    elif user=="scissor" and comp=="paper":
        print("user wins!")
        
    elif user=="scissor" and comp=="rock":
        print("Computer wins!")
        comp_points+=1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
