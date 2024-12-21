def power(num):
    print(num)
    if num==1:
        return True
    if num<=0 or num%2!=0:
        return False
    
    
    else:
        return power(num//2)  
print(power(17))   