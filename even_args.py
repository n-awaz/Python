#Define a function called myfunc that takes in an arbitrary number of arguments, and returns a list containing only those arguments that are even.
mylist=[]
def myfunc(*args):
    for num in args:
        if num%2==0:
            mylist.append(num)
        else:
            continue
    
    return mylist
    
myfunc(10,11,12,13)
print(mylist)