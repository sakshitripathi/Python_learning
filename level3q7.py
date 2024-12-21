names=list(input("Enter the names of students space seperated: ").split())
subjects=list(input("Enter the subjects: ").split())
print(names,subjects)
names_sub={}
for i in range(len(names)):
    names_sub[names[i]]=subjects[i]
print(names_sub)    
    
    