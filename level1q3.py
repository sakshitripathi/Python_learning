phy=int(input("enter marks for physics:"))
chem=int(input("enter marks for chem:"))
maths=int(input("enter marks for maths:"))
computer=int(input("enter marks for computer:"))
bio=int(input("enter marks for bio:"))
percent= (phy+chem+maths+computer+bio)/5
if percent>=90:
    print("grade A")
elif percent>=80:
    print("grade B")
elif percent>=70:
    print("grade C")
elif percent>=60:
    print("grade D")
elif percent >=40:
    print("grade E")  
elif percent<40:
    print("grade F")                
