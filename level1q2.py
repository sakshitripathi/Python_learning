st=input("enter a string")
numOfAlpha=0
numOfDig=0
for s in st:
    if s.isalpha():
        numOfAlpha+=1
    if s.isdigit():
        numOfDig+=1
print("num of alphabets:",numOfAlpha,"num of digits:",numOfDig)            