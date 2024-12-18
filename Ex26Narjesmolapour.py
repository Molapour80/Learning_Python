from pymongo import MongoClient

###github.com/Molapour80/Learning_Python
client = MongoClient('mongodb://localhost:27017/')
db = client['school']
students_collection = db['students']

def add_student(student_id, name, age):
    student = {
        "student_id": student_id,
        "name": name,
        "age": age
    }
    result = students_collection.insert_one(student)
    print(f'Student added: {result.inserted_id}')

def remove_student(student_id):
    result = students_collection.delete_one({"student_id": student_id})
    return result.deleted_count > 0

def search_student(student_id):
    student = students_collection.find_one({"student_id": student_id})
    return student if student else None

def display_students():
    students = list(students_collection.find())
    return students

#### MAIN ####
def main():
    while True:
        print("\n*** Student Records Management ***")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            add_student(student_id, name, age)

        elif choice == "2":
            student_id = input("Enter student ID to remove: ")
            if remove_student(student_id):
                print("Student removed successfully.")
            else:
                print("Student not found.")

        elif choice == "3":
            student_id = input("Enter student ID to search: ")
            stu = search_student(student_id)
            if stu:
                print(f'Student found: {stu}')
            else:
                print("Student not found.")

        elif choice == '4':
            students = display_students()
            if students:
                print("All Students:")
                for student in students:
                    print(student)
            else:
                print("No students found.")

        elif choice == '5':
            print("Goodbye! See you later.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()