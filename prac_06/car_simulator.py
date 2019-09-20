from prac_06.car import Car


def main():
    # add_fuel(self, amount)
    # drive(self, distance)
    # Fuel 0 and odo 0

    print("Let's drive!")
    name = input("Enter your car name: ")
    print(Car(name))





main()

#
#     cars = []
#     cars.append(Car("Rover", 100))
#     cars.append(Car("Toyota", 50))
#
#     for car in cars:
#         print("Name: {}, Fuel: {}L".format(car.name, car.fuel))
#         car.fuel = refuel()
#
#
# def refuel():
#     fuel_to_add = 100
#     car.fuel += fuel_to_add
