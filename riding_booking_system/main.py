import psycopg2
from random import randint

def connect_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="ride_booking_db",
            user="postgres",
            password="9102004"
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
    
class User:
    def __int__(self, name, gender, phone):
        self.__name = name
        self.__gender = gender
        self.__phone = phone
        self.__id = randint(000000, 999999)

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_phone(self):
        return self.__phone
    
    def get_id(self):
        return self.__id
    
class Driver(User):
    def __init__(self, name, gender, phone, car_model, license_plate):
        super().__init__(name, gender, phone)
        self.__car_model = car_model
        self.__license_plate = license_plate
        self.__isAvailable = True

    def get_car_model(self):
        return self.__car_model

    def get_license_plate(self):
        return self.__license_plate
    
    def is_available(self):
        return self.__isAvailable
    
    def set_availability(self, availability):
        self.__isAvailable = availability
    
    

class DriverManager:

    def addDriver(self, name, phone, car_model, license_plate):
        driver = Driver(name, phone, car_model, license_plate)
        conn = connect_db()
        cursor = conn.cursor()
        name = input("Enter driver name: ")
        gender = input("Enter driver gender: ")
        phone = input("Enter driver phone: ")
        car_model = input("Enter car model: ")
        license_plate = input("Enter license plate: ")

        # Insert driver into the database
        cursor.execute(
            "INSERT INTO drivers (name, gender, phone, car_model, license_plate) VALUES (%s, %s, %s, %s, %s)",
            (name, gender, phone, car_model, license_plate)
        )
        conn.commit()
        conn.close()
        print("Driver added successfully!")

    def checkBookingFromUser(self):
        conn = connect_db()
        cursor = conn.cursor()
        conn.excute("SELECT * FROM bookings")
        bookings = cursor.fetchall()
        for booking in bookings:
            print(f"Booking ID: {booking[0]}, \nUser ID: {booking[1]}, \nDriver ID: {booking[2]}, \nPickup: {booking[3]}, \nDropoff: {booking[4]}, \nFare: {booking[5]}, \nStatus: {booking[6]}")



class Ride:
    def __init__(self, user, driver, pickup_location, dropoff_location, fare, distance):
        self.__user = user
        self.__driver = driver
        self.__pickup_location = pickup_location
        self.__dropoff_location = dropoff_location
        self.__fare = fare
        self.__distance = distance
        self.__status = "Scheduled"

    def get_user(self):
        return self.__user

    def get_fare(self):
        return self.__fare

    def get_driver(self):
        return self.__driver
    
    def get_pickup_location(self):
        return self.__pickup_location
    
    def get_dropoff_location(self):
        return self.__dropoff_location
    
    def get_status(self):
        return self.__status
    
    def set_status(self, status):
        self.__status = status
        
    def get_distance(self):
        return self.__distance

    def calculate_fare(self):
        # Placeholder for fare calculation logic
        distance = self.__distance
        base_fare = 5000.0
        per_km_rate = 2000.0
        fare = base_fare + (distance * per_km_rate)
        return fare
    
class RideBooking:
    def book_ride(self):
        user_name = input("Enter your name: ")

        

def main():
    connection = connect_db()
    if connection:
        print("Connected to the database successfully!")
        connection.close()
    else:
        print("Failed to connect to the database.")

    print("Welcome to the Ride Booking System!")
    print("Are you a Driver or a User?")
    print("1. Driver")
    print("2. User")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        