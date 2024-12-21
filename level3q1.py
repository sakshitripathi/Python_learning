with open("/Users/sakshitripathi/python_Assignments/doc.txt","r") as file:
    lines=file.readlines()
    content=''
    for line in  lines:
        words=line.split(' ')
        print(words)
        for word in words:
            if len(word)%2==0:
                content=content+ ' ' +word
    with open("/Users/sakshitripathi/python_Assignments/doc.txt","a") as file:
        file.write("\n"+content)
        print("content updated")
           
                
            
        
    