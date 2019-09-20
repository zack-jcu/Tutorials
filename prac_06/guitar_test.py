from prac_06.Guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2012, 16035.40)

print(gibson.get_age())
print(another_guitar.get_age())
print(gibson.is_vintage())
print(another_guitar.is_vintage())


