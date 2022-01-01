#Greeting
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip = 1 + (tip_percentage / 100)
total_bill = bill * tip
split = "{:.2f}".format(total_bill / people, 2)

print(f"Each person should pay: ${split}")