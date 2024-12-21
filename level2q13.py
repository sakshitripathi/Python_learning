str=input("Enter a string: ")
ch=input("Enter a character: ")
call=lambda str, ch: print("True") if str[0]==ch else print("False")
call(str,ch)
