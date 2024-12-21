str1=input("enter string1")
str2=input("enter string2")
if len(str1)!=len(str2):
    print("not an anagram")
if sorted(str1)==sorted(str2):
    print("its an anagram")   
else:
    print("not an anagram")    