"""
Create an electricity bill estimator
Inputs should be:

price per kWh in cents,
daily use in kWh, and
number of days in the billing period.

print("User's Bonus: ${:.2f}".format(bonus))
"""
print("Electricity bill estimator")
price_per_kWh = int(input("Please enter the price (cents) per kWh: "))
daily_use_kWh = float(input("Please enter the number of hours used per day: "))
billing_period = int(input("Please enter the number of days in billing period: "))

total = (price_per_kWh * daily_use_kWh) * billing_period
print("Bill Estimate: $", total / 100, sep='')
