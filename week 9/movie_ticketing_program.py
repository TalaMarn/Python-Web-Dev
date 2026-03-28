# Movie Ticketing Program
import psycopg2

#-----------DB Connection-----------
def connect_db():
    return psycopg2.connect(
        dbname="movie_system",
        user="postgres",
        password="9102004",
        host="localhost",
        port="5432"
    )

#-----------Class--------------
class Movie:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats

class Theater:
    def add_movie(self, movie):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO movies(name, total_seats, available_seats) VALUES (%s, %s, %s)",
            (movie.name, movie.total_seats, movie.total_seats)
        )
        conn.commit()
        cursor.close()
        conn.close()
        print("Movie added!")

    def show_movie(self):
        conn = connect_db()
        cur = conn.cursor()

        cur.execute("SELECT * FROM movies")
        movies = cur.fetchall()

        print("\n Movies:")
        for m in movies:
            print(f"ID: {m[0]}, Name: {m[1]}, Total Seats: {m[2]}, Available Seats: {m[3]}")

        conn.close()

    #--------------Booking----------------

    def book_ticket(self, movie_id, seat_number):
        conn = connect_db()
        cur = conn.cursor()
        
        # Check seats
        cur.execute(
            "SELECT name, available_seats FROM movies WHERE movie_id = %s", (movie_id,)
        )
        movie = cur.fetchone()
        if not movie:
            print("Movie not found!")
            return
        if movie[1] <= 0:
            print("No seats available!")
            return
        
        # Check seat duplication
        cur.execute(
            "SELECT * FROM bookings WHERE movie_name = %s AND seat_number = %s ", (movie[0], seat_number)
        )
        if cur.fetchone():
            print("Seat already booked!")
            return
        # Insert booking
        cur.execute(
            "INSERT INTO bookings(movie_name, seat_number) VALUES (%s, %s)", 
            (movie[0], seat_number)
        )

        # Update seats
        cur.execute(
            "UPDATE movies SET available_seats = available_seats - 1 WHERE movie_id = %s",
            (movie_id,)
        )

        conn.commit()
        conn.close()
        print("Ticket booked!")

    def cancel_ticket(self, movie_name, seat_number):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM bookings WHERE movie_name = %s AND seat_number = %s",
            (movie_name, seat_number)
        )
        if cur.rowcount == 0:
            print("Booking not found!")
        
        else:
            cur.execute(
                "UPDATE movies SET available_seats = available_seats + 1 WHERE name = %s",
                (movie_name,)
            )
            print("Ticket canceled!")
        conn.commit()
        conn.close()

    #------------View-----------------
    def show_bookings(self):
        conn = connect_db()
        cur = conn.cursor()

        cur.execute("SELECT * FROM bookings")
        bookings = cur.fetchall()
        print("\n Bookings:")
        for b in bookings:
            print(f"Movie: {b[1]}, Seat: {b[2]}")

        conn.close()

#-----------Main Program-----------
def main():
    theater = Theater()

    while True:
        print("\n============ Movie Ticketing System ============")
        print("1. Add Movie")
        print("2. Show Movies")
        print("3. Book Ticket")
        print("4. Cancel Ticket")
        print("5. Show Bookings")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter movie name: ")
            seats = int(input("Enter total seats: "))
            movie = Movie(name, seats)
            theater.add_movie(movie)
        
        elif choice == '2':
            theater.show_movie()

        elif choice == '3':
            movie_id = int(input("Enter movie ID: "))
            seat_number = input("Enter seat number: ")
            theater.book_ticket(movie_id, seat_number)

        elif choice == '4':
            movie_name = input("Enter movie name: ")
            seat_number = input("Enter seat number: ")
            theater.cancel_ticket(movie_name, seat_number)

        elif choice == '5':
            theater.show_bookings()

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()