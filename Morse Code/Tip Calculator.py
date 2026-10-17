# Tip Calculator in Python

#Input the bill amount and tip percentage
Bill_Amount = float(input("What is the total of the bill:"))
Tip_Amount = float(input("What is the tip to give in percents:"))

# Calculate the tip and total amounts
Tip_Percentage = float(round(Tip_Amount * .01, 2))
Tip_Total = float(round(Bill_Amount * Tip_Percentage, 2))
Total_Amount = float(Bill_Amount + Tip_Total)

#Output the tip and total amounts
print("The tip total is:", Tip_Total)
print("The total to pay is:", Total_Amount)