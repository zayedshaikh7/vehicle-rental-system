# Vehicle Rental System - Version 2.0
# Features: rent/return vehicles, rental cost calculation, online vehicle search

vehicles = ["Car", "Bike", "SUV"]

def rent_vehicle(vehicle_id, customer_id):
    print("Vehicle", vehicle_id, "rented to customer", customer_id)

def return_vehicle(vehicle_id):
    print("Vehicle", vehicle_id, "returned")

def calculate_rental_cost(days, rate=500):
    cost = days * rate
    print("Rental Cost = Rs.", cost)
    return cost

def search_vehicle(vehicle_type):
    if vehicle_type in vehicles:
        print(vehicle_type, "is available")
    else:
        print(vehicle_type, "not found")
