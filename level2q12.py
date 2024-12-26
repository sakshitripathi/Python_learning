def login_system():
    username=input("enter the username: ")
    password=input("enter the password: ")
    attempts=3
    while attempts>0:
        retype_password=input("enter passord again: ")
        if retype_password==password:
            print("successful login")
            return 
        else:
            attempts-=1
            if attempts>0:
                print(f"you have {attempts} remaining attempts")
    print("login failed")
login_system()                
            