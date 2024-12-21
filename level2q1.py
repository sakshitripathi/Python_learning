inputlist1=input("enter list1 of elements space separated: ").split()
inputlist2=input("enter list2 of elements space separated: ").split()
print(inputlist1,inputlist2)
s=set()
i=0
j=0
while i<len(inputlist1):
    if inputlist1[i] in inputlist2:
        s.add(inputlist1[i])
    i+=1    
print("common elements",s)        

