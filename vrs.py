# Vehicle Rental System - Version 1.1
# Features: rent and return vehicles, rental cost calculation

def rent_vehicle(vehicle_id, customer_id):
    print("Vehicle", vehicle_id, "rented to customer", customer_id)

def return_vehicle(vehicle_id):
    print("Vehicle", vehicle_id, "returned")

def calculate_rental_cost(days, rate=500):
    cost = days * rate
    print("Rental Cost = Rs.", cost)
    return cost
