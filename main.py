#!/usr/bin/python3

# Import the carFactory class from the backend.carFactory module
from backend.carFactory import carFactory

if __name__ == "__main__":
    """
    Example usage


    args: 
        current_date: Replace with the actual current date
        last_service_date: Replace with the actual last service date
        current_mileage: Replace with the actual current mileage
        last_service_mileage: Replace with the actual last service mileage
        warning_light_is_on: Replace with the actual warning light status
    
    """
    # Example usage
    current_date = 16/11/2023
    last_service_date = 1/14/2019
    current_mileage = 45000
    last_service_mileage = 35000
    warning_light_is_on = True

    # Create different car models using the carFactory

    calliope_car = carFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)

    models = calliope_car
    
    def std_output(models):
        for items in calliope_car:
            print(items, end=" ")
    
    print("\nCar model created: {}")
    glissade_car = carFactory.create_glissade(
        current_date, last_service_date, current_mileage, last_service_mileage)
    palindrome_car = carFactory.create_palindrome(
        current_date, last_service_date, warning_light_is_on)
    rorschach_car = carFactory.create_rorschach(
        current_date, last_service_date, current_mileage, last_service_mileage)
    thovex_car = carFactory.create_thovex(
        current_date, last_service_date, current_mileage, last_service_mileage)

    # Now you have created instances of different car models and can use them as needed.
