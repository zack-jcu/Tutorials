"""
Create an electricity bill estimator
Inputs should be:

price per kWh in cents,
daily use in kWh, and
number of days in the billing period.

print("User's Bonus: ${:.2f}".format(bonus))
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff = input("Please enter your tariff? 11 or 31: ")
daily_use_kWh = float(input("Please enter the number of hours used per day: "))
billing_period = int(input("Please enter the number of days in billing period: "))

if tariff == "11":
    selected_tariff = TARIFF_11
else:
    selected_tariff = TARIFF_31
total = (selected_tariff * daily_use_kWh) * billing_period
print("Bill Estimate: ${:.2f}".format(total), sep='')
