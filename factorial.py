def factorial(a=0):
    if (a==0):
        return 1
    elif (a>=1):
        return a*factorial(a-1)
    else:
        return "Invalid input."
a=int(input())
print(factorial(a))