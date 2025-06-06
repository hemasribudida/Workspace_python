def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
num = int(input("Enter a number to find factorial: "))

if num < 0:
    print("Factorial is not defined to find factorial.")
else:
    result = factorial(num)
    print("The factorial of "+ str(num) + " is " + str(result))
    