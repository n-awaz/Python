time_year=int(input("Enter the number you served the company:"))
salary=int(input("Your Salary is:"))
if time_year>=10:
    print(salary+salary*0.1)
elif time_year>=6:
    print(salary+salary*0.08)
else:
    print(salary+salary*0.05)