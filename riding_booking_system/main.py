import psycopg2
import subprocess
import os

def clear_screen():
    subprocess.run('cls' if os.name == 'nt' else ['clear'], shell=True)

def connect_to_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="riding_booking_db",
            user="postgres",
            password="9102004"
        )
        return connection
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None

def create_tables():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS passengers (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(50) NOT NULL,
                role VARCHAR(20) NOT NULL,
                phone_number VARCHAR(20)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS drivers (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(50) NOT NULL,
                role VARCHAR(20) NOT NULL,
                phone_number VARCHAR(20),
                license_number VARCHAR(50),
                car_model VARCHAR(50),
                per_km_fee DECIMAL(10, 2)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id SERIAL PRIMARY KEY,
                passenger_id INTEGER REFERENCES passengers(id),
                driver_id INTEGER REFERENCES drivers(id),
                pickup_location VARCHAR(100),
                dropoff_location VARCHAR(100),
                distance DECIMAL(10, 2),
                fare DECIMAL(10, 2),
                status VARCHAR(20) DEFAULT 'Pending'
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("Tables created successfully!")
    else:
        print("Failed to connect to the database to create tables.")
    
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.__password = password
        self._role = role

    def register(self):
        clear_screen()
        print("Which type of user do you want to register?")
        print("1. Passenger")
        print("2. Driver")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            self._role = "Passenger"
        elif choice == "2":
            self._role = "Driver"
        else:
            print("Invalid choice. Please enter 1 or 2.")
            return
        
        self.username = input("Enter your username: ")
        self.__password = input("Enter your password: ")

        if self._role == "Passenger":
            phone_number = input("Enter your phone number: ")
        elif self._role == "Driver":
            phone_number = input("Enter your phone number: ")
            license_number = input("Enter your license number: ")
            car_model = input("Enter your car model: ")
            per_km_fee = input("Enter your per km fee: ")

        #    == Database Insertion ==
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            if self._role == "Passenger":
                cursor.execute("INSERT INTO passengers (username, password, role, phone_number) VALUES (%s, %s, %s, %s)", (self.username, self.__password, self._role, phone_number))
            elif self._role == "Driver":
                cursor.execute("INSERT INTO drivers (username, password, role, phone_number, license_number, car_model, per_km_fee) VALUES (%s, %s, %s, %s, %s, %s, %s)", (self.username, self.__password, self._role, phone_number, license_number, car_model, per_km_fee))
            conn.commit()
            cursor.close()
            conn.close()
            print("Registration successful!")

    def Login(self, username, password, role):
        clear_screen()
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            if role == "Passenger":
                cursor.execute("SELECT * FROM passengers WHERE username = %s AND password = %s", (username, password))
            elif role == "Driver":
                cursor.execute("SELECT * FROM drivers WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            cursor.close()
            conn.close()
            if user:
                print(f"Login successful! Welcome, {username}!")
                return role
            else:
                print("Invalid username or password. Please try again.")
                return None
        else:
            print("Failed to connect to the database. Please try again.")
            return None

#========================= Driver Class ========================

class Driver(User):
    def __init__(self, username, password):
        super().__init__(username, password, "Driver")
        self.driver_id = None
    
    def set_driver_id(self):
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM drivers WHERE username = %s", (self.username,))
            driver = cursor.fetchone()
            if driver:
                self.driver_id = driver[0]
            cursor.close()
            conn.close()


    def show_order(self):
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            self.set_driver_id()
            cursor.execute("SELECT * FROM orders WHERE driver_id = %s", (self.driver_id,))
            orders = cursor.fetchall()
            cursor.close()
            conn.close()
            if orders:
                print("=========================================")
                print("Your Orders:")
                for order in orders:
                    print(f"Order ID: {order[0]}, Passenger: {order[1]}, Pickup: {order[2]}, Dropoff: {order[3]}, Distance: {order[4]}, Fare: {order[5]}")
            else:
                print("You have no orders at the moment.")
            input("Press Enter to continue...")
            clear_screen()
        else:
            print("Failed to connect to the database. Please try again.")

    def update_order_status(self, new_status):
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            self.show_order()
            order_id = input("Enter the Order ID of the ride you want to update: ")
            cursor.execute("UPDATE orders SET status = %s WHERE id = %s AND driver_id = %s", (new_status, order_id, self.driver_id))
            conn.commit()
            cursor.close()
            conn.close()


    def edit_fee(self, new_fee):
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE drivers SET per_km_fee = %s WHERE id = %s", (new_fee, self.driver_id))
            conn.commit()
            cursor.close()
            conn.close()
            print("Per km fee updated successfully!")
        else:
            print("Failed to connect to the database. Please try again.")

#========================= Passenger Class ========================

class Passenger(User):
    def __init__(self, username, password):
        super().__init__(username, password, "Passenger")
        self.passenger_id = self.get_passenger_id()

    def show_available_drivers(self): # Show available drivers with their car model and per km fee
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, username, car_model, per_km_fee FROM drivers")
            drivers = cursor.fetchall()
            cursor.close()
            conn.close()
            if drivers:
                print("=========================================")
                print("Available Drivers:")
                for driver in drivers:
                    print(f"Driver ID: {driver[0]}, Username: {driver[1]}, Car Model: {driver[2]}, Per Km Fee: {driver[3]}")
            else:
                print("No drivers available at the moment.")
        else:
            print("Failed to connect to the database. Please try again.")

    def fare_calculator(self, distance, per_km_fee):
        return distance * per_km_fee
    
    def get_passenger_id(self):
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM passengers WHERE username = %s", (self.username,))
            passenger = cursor.fetchone()
            if passenger:
                return passenger[0]
            cursor.close()
            conn.close()
        return None

    def book_ride(self, pickup_location, dropoff_location, distance, driver_id):
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT per_km_fee FROM drivers WHERE id = %s", (driver_id,))
            driver = cursor.fetchone()
            if driver:
                per_km_fee = driver[0]
                fare = self.fare_calculator(distance, per_km_fee)
                cursor.execute("INSERT INTO orders (passenger_id, pickup_location, dropoff_location, distance, driver_id, fare, status) VALUES (%s, %s, %s, %s, %s, %s, 'Pending')", (self.passenger_id, pickup_location, dropoff_location, distance, driver_id, fare))
                conn.commit()
                print("Ride booked successfully!")
                input("Press Enter to continue...")
                clear_screen()
            else:
                print("Driver not found.")
            cursor.close()
            conn.close()
        else:
            print("Failed to connect to the database. Please try again.")

    def cancel_ride(self):
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            self.get_passenger_id()
            cursor.execute("SELECT * FROM orders WHERE passenger_id = %s AND status = 'Pending'", (self.passenger_id,))
            orders = cursor.fetchall()
            if orders:
                print("Your Orders:")
                for order in orders:
                    print(f"Order ID: {order[0]}, Pickup: {order[2]}, Dropoff: {order[3]}, Distance: {order[4]}, Driver: {order[5]}, Fare: {order[6]}, Status: {order[7]}")
                order_id = input("Enter the Order ID of the ride you want to cancel: ")
                cursor.execute("UPDATE orders SET status = 'Cancelled' WHERE id = %s AND passenger_id = %s", (order_id, self.passenger_id))
                conn.commit()
                print("Ride canceled successfully!")
                input("Press Enter to continue...")
                clear_screen()
            else:
                print("You have no pending orders.")
            cursor.close()
            conn.close()

    def view_bookings(self):
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM orders WHERE passenger_id = %s", (self.passenger_id,))
            orders = cursor.fetchall()
            
            if orders:
                print("=========================================")
                print("Your Bookings:")
                for order in orders:
                    cursor.execute("SELECT username FROM drivers WHERE id = %s", (order[2],))
                    driver = cursor.fetchone()
                    print(f"Order ID: {order[0]}, Driver: {driver[0]}, Pickup: {order[3]}, Dropoff: {order[4]}, Distance: {order[5]}, Fare: {order[6]} MMK, Status: {order[7]}")
            else:
                print("You have no bookings.")
            cursor.close()
            conn.close()
            
            input("Press Enter to continue...")
            clear_screen()


#========================= Main Function ========================
        
def main():
    create_tables()
    while True:
        print("Welcome to the Riding Booking System!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == "1":
            user = User("", "", "")
            user.register()
        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            print("Select your role:")
            print("1. Passenger")
            print("2. Driver")
            role_choice = input("Enter your choice (1 or 2): ")
            if role_choice == "1":
                role = "Passenger"
            elif role_choice == "2":
                role = "Driver"
            else:
                print("Invalid role choice.")
                continue

            # Determine user_role based on login credentials and show appropriate dashboard
            user_role = User("", "", "").Login(username, password, role)
            if user_role == "Driver":
                driver = Driver(username, password)
                while True:
                    print("=========================================")
                    print("Welcome to the Driver Dashboard!")
                    print("1. Show Orders")
                    print("2. Update Order Status")
                    print("3. Edit Fee")
                    print("4. Exit")
                    driver_choice = input("Enter your choice (1, 2, 3, or 4): ")

                    if driver_choice == "1":
                        driver.show_order()
                    elif driver_choice == "2":
                        print("Select new status:")
                        print("1. Accepted")
                        print("2. Completed")
                        print("3. Cancelled")
                        status_choice = input("Enter your choice (1, 2, or 3): ")
                        if status_choice == "1":
                            new_status = "Accepted"
                        elif status_choice == "2":
                            new_status = "Completed"
                        elif status_choice == "3":
                            new_status = "Cancelled"
                        else:
                            print("Invalid status choice.")
                            continue
                        driver.update_order_status(new_status)

                    elif driver_choice == "3":
                        new_fee = input("Enter new per km fee: ")
                        driver.edit_fee(new_fee)

                    elif driver_choice == "4":
                        print("Exiting Driver Dashboard. Goodbye!")
                        break

                    else:
                        print("Invalid choice. Please enter 1, 2, 3, or 4.")

            elif user_role == "Passenger":
                while True:
                    passenger = Passenger(username, password)
                    passenger.show_available_drivers()
                    print("=========================================")
                    print("Welcome to the Passenger Dashboard!")
                    print("1. Book a Ride")
                    print("2. Cancel a Ride")
                    print("3. View Bookings")
                    print("4. Exit")
                    passenger_choice = input("Enter your choice (1, 2, 3, or 4): ")
                    if passenger_choice == "1":
                        pickup_location = input("Enter pickup location: ")
                        dropoff_location = input("Enter dropoff location: ")
                        distance = int(input("Enter distance in km: "))
                        driver_id = input("Enter the driver's id you want to book: ")
                        passenger.book_ride(pickup_location, dropoff_location, distance, driver_id)
                    elif passenger_choice == "2":
                        passenger.cancel_ride()
                    elif passenger_choice == "3":
                        passenger.view_bookings()
                    elif passenger_choice == "4":
                        print("Exiting Passenger Dashboard. Goodbye!")
                        break
                    else:
                        print("Invalid choice. Please enter 1, 2, 3, or 4.")
            else:
                print("Invalid role choice.")
                continue
            break
        elif choice == "3":
            print("Thank you for using the Riding Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()