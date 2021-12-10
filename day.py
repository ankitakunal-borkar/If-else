
# day = input("Aaj ka din kya hai? (monday/tuesday) > ")
# time = input("Kaunse samay ka khana banana hai? (lunch/dinner) > ")
# if day == "monday" and time =="lunch":
#     print ("Daal-Roti banegi aaj")
# elif day == "tuesday" and time == "dinner":
#     print ("Pav-Bhaji banegi aaj toh")

day=input("enter the day")
time=input("enter the time")
if day=="monday":
    if time=="breakfast":
        print("poha")
    elif time=="lunch":
        print("dal chaval")
    else:
        print("roti sabji")
elif day=="tuesday":
    if time=="breakfast":
        print("magi")
    elif time=="lunch":
        print("rajma")
    else:
        print("khichdi")
elif day=="wednesday":
    if time=="breakfast":
        print("khir puri")
    elif time=="lunch":
        print("upma")
    else:
        print("pulav")
elif day=="thursday":
    if time=="breakfast":
        print("ots")
    elif time=="lunch":
        print("chole roti")
    else:
        print("hamburger")
elif day=="friday":
    if time=="breakfast":
        print("pizza")
    elif time=="lunch":
        print("moong dal khichdi")
    else:
        print("masala poha")
elif day=="saturday":
    if time=="breakfast":
        print("pasta")
    elif time=="lunch":
        print("methi parantha")
    else:
        print("moong dal khichdi")
elif day=="sunday":
    if time=="breakfast":
        print("sandwich")
    elif time=="lunch":
        print("methi roti")
    else:
        print("chaval")

