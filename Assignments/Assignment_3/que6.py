#6.Write a program to calculate profit or loss.

# Profit = Profit / CP * 100 [Profit = Selling price - cost price]
# Loss = Loss / CP * 100 [Loss = cost price - selling price]

cp = float(input('Enter cost price (CP):'))
sp = float(input('Enter selling price (SP):'))

if (sp > cp):
    profit = sp - cp
    profit_percent = profit / cp * 100
    print(f'Profit is {profit:.2f}')
    print(f'Profit percent is {profit_percent:.2f}%')
elif (cp > sp):
    loss = cp - sp
    loss_percent = loss / cp * 100
    print(f'Loss is {loss:.2f}')
    print(f'Loss percent is {loss_percent:.2f}%')
else:
    print(f'No profit, no loss.')