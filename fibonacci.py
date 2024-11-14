def fibonacci(a=2):
    if (a<=2):
        return 1
    elif (a>2):
        return fibonacci(a-1)+fibonacci(a-2)
    else:
        return "Invalid input."
a=int(input())
print(fibonacci(a))