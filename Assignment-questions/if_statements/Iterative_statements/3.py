num = int(input("Enter a number: "))

even_sum = 0
odd_sum = 0
for i in range(0,num+1):
    if i % 2 ==0:
        even_sum += i
    else:
        odd_sum += i
print("sum of even number =", even_sum)
print("sum of odd numbers =", odd_sum)