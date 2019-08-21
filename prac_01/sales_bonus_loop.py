"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.


Add a loop to the sales bonus exercise you did above, so that the program repeatedly asks for the user's sales and
prints the bonus until they enter a negative number.
Remember that until is the opposite of while.
"""

sales_value = float(input("Please enter the value of the Sales: $"))
while sales_value >= 0:
    if sales_value < 1000:
        bonus = sales_value * 0.1
    else:
        bonus = sales_value * 0.15
    print("User's Bonus: ${:.2f}".format(bonus))
    sales_value = float(input("Please enter the value of the Sales: $"))
