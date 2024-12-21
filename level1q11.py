num=int(input("Enter the number: "))
sum=0
rem=0
while len(str(num))!=1:
    while num!=0:
        rem=num%10
        sum+=rem
        num=num//10
    if len(str(sum))!=1:
        num=sum
        sum=0    
print("final sum",sum)    
    