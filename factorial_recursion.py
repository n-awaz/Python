def factorial(num):
    if num==0:
        return 1
    return num*factorial(num-1)

ans=factorial(5)
print(ans)