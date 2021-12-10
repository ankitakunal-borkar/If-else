letter=input("enter the letter")
if letter>="a" or letter<="z":
    special_char=input("enter the special_char")
    if special_char=="@"or "$" or "#":
        numeric=int(input("enter the number"))
        if numeric>=1:
            print(letter+special_char+str(numeric))   
        else:
            print("invalied")
    else:
        print("it is not special character")
else:
    print("it is not letter")
