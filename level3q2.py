with open("/Users/sakshitripathi/python_Assignments/doc.txt","r") as file:
    lines=file.readlines()
    count=0
    for line in lines:
        count+=1
    print("count of lines are: ",count)    