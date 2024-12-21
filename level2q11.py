list1=list(map(str,input("enter strings space separated: ").split()))
print(list1)
mainlist=[]
for st in list1:
    l=list(map(str,st))
    mainlist.append(l)
print(mainlist)    