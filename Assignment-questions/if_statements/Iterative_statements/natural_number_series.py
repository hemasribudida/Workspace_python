num = int(input("Enter a number: "))
sum_series = 0
if num <0:
    print("Please enter a natural number greater than 0.")
else:
    
    for i in range(1,num+1):
        print(i, end=" ")
        sum_series += i
    print(" sum of the series is =", sum_series)