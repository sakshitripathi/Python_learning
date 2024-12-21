def JtoI(file):
    lines=file.readlines()
    #print(lines)
    correctedlines=[]
    for line in lines:
        corrected=''
        for char in line:   
            if char=='j':
                corrected+='i'
            else:
                corrected+=char
    correctedlines.append(corrected)  
    with open("/Users/sakshitripathi/python_Assignments/words.txt","w") as file:
              
        file.writelines(correctedlines)            
    return file
    
with open("/Users/sakshitripathi/python_Assignments/words.txt","r") as file:
    JtoI(file)
    

        
    