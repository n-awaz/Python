marks=float(input("Enter Your percantage in numbers: "))
if marks>90 and marks<=100:
    print("A Grade")
elif marks>80 and marks<=90:
    print("B Grade")
elif marks>70 and marks<=80:
    print("C Grade")
elif marks>60 and marks<=70:
    print("D Grade")
elif marks>=40 and marks<=60:
    print("E Grade")
elif marks<40:
    print("FAILED")
else:
    print("Enter Valid Number")