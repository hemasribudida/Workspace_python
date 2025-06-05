Bill =  int(input("Enter the Bill amount: "))
age = int(input("Enter the age of the customer : "))
if age > 50:
    discount = Bill *0.05
    Bill -= discount
    print("5% discount applied.")
else:
    print("No discount applied. ")
print("Final bill amount to be paid: Rs", round(Bill, 2))