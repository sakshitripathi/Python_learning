def countVowels(str):
    count=0
    s={"a","e","i","o","u"}
    for st in str:
        if st in s:
            count+=1
    return count        
str=input("Enter a string: ")    
print("count of vowels is: ",countVowels(str))