usearname= input("what is the name")
password=int(input("enter the password"))
if usearname >="a" or usearname<="z":
    if password>=0:
        print("your login is succesfully")
    else:
        print("incorrect password")
elif usearname!="ankita" and password!=12:
    print("both conditions are wrong")
    print("create new account") 
    name=(input("entre the name"))
    pas=input("enter the password ")
    print("your new account(successfuli created")
else:
    print("incorrect userday name")

