from prac_08.taxi import Taxi


# name, fuel, price_per_km

def main():
    new_taxi = Taxi("Prius 1", 100)
    new_taxi.drive(40)
    print(new_taxi)
    print(new_taxi.get_fare())
    new_taxi.start_fare()
    new_taxi.drive(100)
    print(new_taxi)
    print(new_taxi.get_fare())


main()
