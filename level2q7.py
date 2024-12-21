list1=list(map(int,input("enter numbers in the list space seperated: ").split()))

def findmedian(list1):
    list1=sorted(list1)
    print(list1)
    if len(list1)%2!=0:
        return list1[len(list1)//2]
    else:
        mid1=len(list1)//2
        mid2=(len(list1)//2)-1
        #print(list1[mid1],list1[mid2])
        return (list1[mid1]+list1[mid2])//2
       
print("median of list: ",findmedian(list1))