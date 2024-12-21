inputlist=list(map(int,input("enter list element space seperated: ").split()))
key=int(input("enter key value: "))
s=set()
count=0
for k in inputlist:
    if key-k in s:
        count+=1
    s.add(k)    
print("count of pairs: ",count)