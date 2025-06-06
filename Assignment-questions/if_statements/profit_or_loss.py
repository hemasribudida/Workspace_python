cp= int(input("Enter the Cost Price (CP): "))
sp = int(input("Enter the selling Price (SP): "))
if sp > cp:
    profit = sp-cp
    print("you made a Profit of Rs ", round(profit,2))
elif sp - cp:
    loss = cp - sp
    print("You made a loss of Rs ", round(loss,2))
else:
    print("No Profit, No Loss. ")
    
