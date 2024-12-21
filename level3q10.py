n=int(input("enter the number of computers:"))
seq=input("enter sequence (each letter twice):")
def noOfUser(seq,n):
    s=set()
    count=0
    unused=set()
    for i in seq:
        if n>0 and i not in s:
            s.add(i)
            n-=1
        elif i in s:
            s.remove(i)
            n+=1
        elif n==0 and i not in unused:
            count+=1
            unused.add(i)
    return count            
print("number of users returned",noOfUser(seq,n))                