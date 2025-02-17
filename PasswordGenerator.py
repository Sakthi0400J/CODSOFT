import random




lowercase= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase= ['A','B','C','D', 'E', 'F', 'G', 'H','I','J','K','L','M', 'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=["1","2","3","4","5","6","7","8","9","0"]


length=int(input("Enter the length of the password"))
temp_choice=[1,2,3]
password=""

for i in range(length):
    temp=random.choice(temp_choice)
    if temp==1:
        ans=random.choice(lowercase)
        password+=ans
    elif temp==2:
        ans=random.choice(uppercase)
        password+=ans
    elif temp==3:
        ans=random.choice(numbers)
        password+=ans



print("GENERATED PASSWORD",password)

