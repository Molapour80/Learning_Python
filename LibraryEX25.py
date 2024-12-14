import mysql.connector


class LibrarySystem:
    def __init__(self):
        self.connection = self.create_connection()
        self.create_database_and_tables()

    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='your_username',  
                password='your_password'  
            )
            if connection.is_connected():
                print("Connected to MySQL server")
                return connection
        except :
            print("ERRor")
            return None

    def create_database_and_tables(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS LibrarySystem")
            cursor.execute("USE LibrarySystem")

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                UserID INT AUTO_INCREMENT PRIMARY KEY,
                Username VARCHAR(50) NOT NULL,
                Email VARCHAR(100) NOT NULL,
                RegistrationDate DATE NOT NULL
            )
            ''')

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Employees (
                EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(50) NOT NULL,
                Position VARCHAR(50) NOT NULL,
                HireDate DATE NOT NULL
            )
            ''')

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Books (
                BookID INT AUTO_INCREMENT PRIMARY KEY,
                Title VARCHAR(100) NOT NULL,
                Author VARCHAR(100) NOT NULL,
                PublicationYear INT NOT NULL,
                Genre VARCHAR(50) NOT NULL
            )
            ''')
            print("Database and tables created successfully.")
        except :
            print("Error")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Connection closed")

    def register_user(self, username, email):
        self.execute_query("INSERT INTO Users (Username, Email, RegistrationDate) VALUES (%s, %s, CURDATE())", (username, email))

    def delete_user(self, user_id):
        self.execute_query("DELETE FROM Users WHERE UserID = %s", (user_id,))

    def display_user(self, user_id):
        user = self.fetch_one("SELECT * FROM Users WHERE UserID = %s", (user_id,))
        print("User Details:", user if user else "User not found.")

    def add_employee(self, name, position):
        self.execute_query("INSERT INTO Employees (Name, Position, HireDate) VALUES (%s, %s, CURDATE())", (name, position))

    def display_employee(self, employee_id):
        employee = self.fetch_one("SELECT * FROM Employees WHERE EmployeeID = %s", (employee_id,))
        print("Employee Details:", employee if employee else "Employee not found.")

    def add_book(self, title, author, publication_year, genre):
        self.execute_query("INSERT INTO Books (Title, Author, PublicationYear, Genre) VALUES (%s, %s, %s, %s)", (title, author, publication_year, genre))

    def update_book(self, book_id, author=None, publication_year=None, genre=None):
        query = "UPDATE Books SET Author = %s, PublicationYear = %s, Genre = %s WHERE BookID = %s"
        self.execute_query(query, (author, publication_year, genre, book_id))

    def search_books(self, title):
        books = self.fetch_all("SELECT * FROM Books WHERE Title LIKE %s", ('%' + title + '%',))
        if books:
            for book in books:
                print("Book Found:", book)
        else:
            print("No books found with that title.")

    def execute_query(self, query, params):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        print("Operation successful.")

    def fetch_one(self, query, params):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

    def fetch_all(self, query, params):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

def main():
    library = LibrarySystem()

   
    library.register_user("Alice", "alice@example.com")
    library.register_user("Bob", "bob@example.com")

   
    library.display_user(1) 
    library.display_user(2)  

    library.add_employee("Charlie", "Librarian")

   
    library.display_employee(1) 

   
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
    library.add_book("1984", "George Orwell", 1949, "Dystopian")

    
    library.search_books("The Great Gatsby")

   
    library.update_book(1, author="Fitzgerald", genre="Classic")


    library.search_books("1984")

  
    library.delete_user(1)  

  
    library.display_user(1)

 
    library.close_connection()

if __name__ == "__main__":
    main()