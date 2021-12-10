print("Please insert your ATM card")       
print("-:WELCOME TO SBI ATM:-")
language=input("Enter the language:-")
if language=="english":
    print("Next")
    pin=int(input("Enter the card pin"))
    pin=len(str(pin))==4
    if pin==1000 or 9999:
        print("Choose your account")
        print("""
            1==current account
            2==Saving account
            3==credit
              """)
        account=input("write your account")
        if account=="current account" and "saving account" and "credit":
            print("Next")
            print("Please select your transaction")
            print("""
                1==balace enquiry
                2==cash withrowal
                3==deposite amount
                4==exit        
                """
                )
            option=int(input("Please enter your choice"))
            balance=5000
            if option==1:
                print("your current balance is",balance)
            elif option==2:
                case_withrowal=int(input("Please enter your withdrawal amount"))
                balance=balance-case_withrowal
                print(case_withrowal,"is withrowal to your account")
                print("Your current balance is",balance)
                b=input("you take your recipt ")
                if b=="yes":
                    print("Ok, Thanks for using me")
                else:
                        print("Take your recipt")
            elif option==3:
                deposite_ammount=int(input("Please enter your deposite amount"))
                balance=balance+deposite_ammount
                print(deposite_ammount,"is credited to your account")
                print("Your updated balance is",balance)
                c=input("You take your deposite recipt")
                if c=="yes":
                    print("Ok")
                else:
                    print("your deposite recipt")
            elif option==4:
                print("Exit")
        else:
            ("Something is wrong,try again")        
    else:
        print("Try again")
        
        
        
        
elif language=="hindi":
    print("Aage badiye")
    pin=int(input("Aapna pin number dale"))
    pin=len(str(pin))==4
    if pin==1000 or 9999:
        print("Aapna khata chune")
        print("""
            1==current acconut
            2==Saving account
            3==credit
              """)
        account=input("yha khata nam likhe ")
        if account=="current account" and "saving account":
            print("Next")
            print("Aap kis chij se transaction kern achahte hy")
            print("""
                1==balace enquiry
                2==case withrowal
                3==deposite amount
                4==bahar nikle        
                """
                )
            try:
                option=int(input("Aapni pasand likhe"))
            except:
                print("yah glt hy")
            balance=5000
            if option==1:
                print("aapka vertman balance yah hy",balance)
            if option==2:
                case_withrowal=int(input("aapko kitne paise nikalne hai"))
                balance=balance-case_withrowal
                print(case_withrowal,"rupees aapke khate se nikale gye hy")
                print("aapka vertma balance yah hy",balance)
                b=input("aapne parchi li")
                if b=="ha":
                    print("Thik hy,")
                else:
                        print("Aapni parchi le")
            if option==3:
                deposite_ammount=int(input("Aapko kitne paise dalne hy"))
                balance=balance+deposite_ammount
                print(deposite_ammount,"aapke khate me itne paise dal diye gye hy")
                print("Aapka balance bda diya gya hy",balance)
                c=input("aapne kitne paise dale hy uski parchi li")
                if c=="ha":
                    print("Thik hy")
                else:
                    print("aapki paise dalne wali parchi le")
            if option==4:
                print("bahar nikle")
        else:
            ("kuch galt hy,kripya fir se ")        
    else:
        print("fir prayas kare")         
else:
    print("tumahri bhasha glt hy, kripya sahi bhasha likh")
      
        
        






