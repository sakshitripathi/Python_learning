string1=input("Enter a string: ")
def runlength(string1):
    ans=''
    i=0
    while i<len(string1):
        curr=string1[i]
        count=0
        while i<len(string1) and curr==string1[i]:
            count+=1
            i+=1   
        ans+=curr+str(count)
        
    return ans    
print("run length ",runlength(string1))            
            