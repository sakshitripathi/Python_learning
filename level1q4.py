num1=int(input("enter num1: "))
num2=int(input("enter num2 greater than num1: "))
sum=0
for num in range(num1,num2+1):
    if num%2!=0:
        sum+=num
print("the sum of all odd numbers between",num1, "and",num2,"is",sum)
        