list1=[]
n=int(input("enter the number of elements to take in list1: "))
for i in range(n):
    x=int(input("enter number: "))
    list1.append(x)
mp={}
for i in range(len(list1)):
    if list1[i] in mp:
        mp[list1[i]]+=1
    else:
        mp[list1[i]]=1       
print(mp)        