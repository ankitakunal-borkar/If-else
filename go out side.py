day=input("enter the day:-")
if day=="monday":
    print("ok")
    disco_per=input("take discopermission:-")
    if disco_per=="yes":
        print("imform the teme member")
        teme_member=input("take teme member permission:-")
        if teme_member=="yes":
            print("ok")
            place=input("enter the place")
            if place=="hospital":
                print("you can go")
                going_time=int(input("enter thegoing time"))
                if going_time>=6:
                    print("ok")
                    coming_time=int(input("enter the coming time"))
                    if coming_time<=5.30:
                        print("ok")
                        prefertion=input("enter the prefertion")
                        if prefertion=="mask" and "sanitizer":
                            print("yes you can go")
                        else:
                            print("you cant go") 
                    else:
                        print("no")  
                else:
                    print("not ok") 
            else:
                print("is cant go")
        else:
            print("is not ok")
    else:
        print("dont ask")
else:
    (" invalid")
            
            
            
