"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales_value = float(input("Please enter the value of the Sales: $"))
if sales_value < 1000:
    bonus = sales_value * 0.1
    print("User's Bonus: ${:.2f}".format(bonus))
else:
    bonus = sales_value * 0.15
    print("User's Bonus: ${:.2f}".format(bonus))
