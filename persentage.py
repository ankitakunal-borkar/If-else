per=int(input("enter the marks"))
if per<=25:
    print("fail grade")
elif per>=25 and per<=45:
    print("e grade")
elif per>=45and per<=50:
    print("d grade")
elif per>=50 and per<=60:
    print("c grade")
elif per>=60 and per<=80:
    print("b grade")
elif per>=80:
    print("a grade")
else:
    print("fail")
        
# a=[1,2,3,4,5,6,7,8]
# print(a[::-5])