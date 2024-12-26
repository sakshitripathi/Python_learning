num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
lcm=max(num1,num2)
while True:
    if lcm%num1==0 and lcm%num2==0:
        print(f"lcm of {num1} and {num2} is {lcm}")
        break
    lcm+=1
    
    
