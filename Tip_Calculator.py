print("Welcome to Tip Calculator")
Bill = float(input("What was the total bill ? $"))
tip_per = float(input("what percentage tip would you like to give ? 10, 12, or 15 ? "))
split = int(input ("How many people to split the bill ? "))
Bill_with_tip = (Bill+(Bill*tip_per/100))/split
print(f'Total Bill : ${round(Bill_with_tip,2)}')

# adding two decimal pt
Total_bill = "{:.2f}".format(Bill_with_tip)
print('Totall_bill : $' + Total_bill)
