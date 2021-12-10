per=int(input("enter the marks"))
if per>80:
    print("A grade")
elif per>60 and per<=80:
    print("B grade")
elif per>=50 and per<=60:
    print("C grade")
elif per>=45 and per<=50:
    print("D grade")
elif per>=25 and per<=45:
    print("E grade")
else:
    print("fail")