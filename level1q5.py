num=int(input("enter a number to find factorial"))
factorial=1
for i in range(num,0,-1):
    factorial*=i
print(f"the factorial of {num} is {factorial}")    
  
        