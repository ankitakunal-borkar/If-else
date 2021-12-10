ammount=60000
print("wellcome to bank of india")
card=input("enter your card:-")
if card=="atm":
    language = input("enter the language:-")
    if language =="hindi" or language =="english":
        account=input("enter the type account:-")
        if account =="current" and "saving":
            pin = int (input("enter the pin:-"))
            if pin == 1234:
                    transaction=input("enter the transaction:-")
                    if transaction == "withdrawal":
                        cash =int(input("enter the cash:-"))
                        if cash>=100 and cash<=10000:
                            # print(ammount-cash,"are remaining")
                            receipt=input("do you want to reciept your ammount:-")
                            if receipt == "yes":
                                print("take a printed reciept,if needed")
                                print("your withdrawal successful thank you so much")
                            else:
                                print("no")
                        else:
                            print("something went to wrong")
                    else:
                        print("incorrect")      
            else:
                print("not ammount")
        else:
            print("pin is correct")   
    else:
        print("break")
else:
    print("out process") 