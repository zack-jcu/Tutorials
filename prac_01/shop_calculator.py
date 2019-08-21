"""
A shop requires a small program that would allow them to quickly work out the total price for a number of items, each
with different prices.

The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is
displayed on the screen.
"""

total_items_cost = 0
number_of_items = int(input("How many item would you like to enter: "))
while number_of_items <= 0:
    print("*** Invalid selection ***")
    number_of_items = int(input("How many item would you like to enter: "))

for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_items_cost += price_of_item

if total_items_cost > 100:
    discount = total_items_cost * 0.1
    print("Total price for ", number_of_items, "items is ${:.2f}".format(total_items_cost - discount))
    print("A ${:.2f}".format(discount), "discount was included")
else:
    print("Total price for ", number_of_items, "items is ${:.2f}".format(total_items_cost))
