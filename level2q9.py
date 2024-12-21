list1=list(map(int,input("enter the numbers in a list").split()))
indx=int(input("enter a index"))
def accessOperation(list1,indx):
    try:
       print(f"element at index {indx} is {list1[indx]} ")
    except IndexError:
        print("index out of range")            
accessOperation(list1,indx)
