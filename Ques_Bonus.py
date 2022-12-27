a=int(input("Number of Years you Served: "))
b=int(input("Enter Your Salary: "))
if a>5:
    print("Congratulations for Rs.1000 Bonus \nYour Salary is:")
    print(b+1000)
else:
    print("Not Eligible for Bonus\nYour Salary is:")
    print(b)