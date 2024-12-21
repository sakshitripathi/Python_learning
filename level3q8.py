import re
coded=input("Enter a string for firstname,lastname and id all connected by 0s: ")
def encode(coded):
    mp={}
    list1=re.split('0+',coded)
    mp['firstname']=list1[0]
    mp['lastname']=list1[1]
    mp['id']=list1[2]
        
    return mp 
print("results: ",encode(coded))    
   
    