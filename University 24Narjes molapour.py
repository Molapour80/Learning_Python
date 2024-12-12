import mysql.connector
##github.com/Molapour80/Learning_Python

con = mysql.connector.connect(
    host='localhost', 
    user='admin',  
    password='2001',  
    database='university'  
)

cursor = con.cursor()


cursor.execute("CREATE DATABASE university")
cursor.execute("USE university")


cursor.execute('''
CREATE TABLE  Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    Email VARCHAR(100)
)''')

cursor.execute('''
CREATE TABLE  Courses  (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    Instructor VARCHAR(100)
)''')

cursor.execute('''
CREATE TABLE  Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
)''')


students = """
    INSERT INTO Students(StudentID,FirstName,LastName,DateOfBirth,Email)
     values
    (1, 'narjes', 'go', '2000-01-15', 'narjes.doadse@example.com'),
    (2, 'fati', 'don', '1999-05-23', 'fati.smdaasith@example.com'),
    (3, 'moni', 'molapour', '2001-09-30', 'monie.johnsadsason@example.com'),
    (4, 'Bobds', 'Brown', '2002-02-10', 'bobds.browdadan@example.com')
"""

courses ="""
    INSERT INTO Courses (CourseID,CourseName ,Instructor)
    values
    (1, 'Introduction to Java', 'Dr. go'),
    (2, 'Advanced Java', 'Prof. dr.don'),
    (3, 'Data Structures', 'Dr. Brown'),
    (4, 'Database Systems', 'Prof. molapour')
"""

enrollments = """
    INSERT INTO Enrollments (EnrollmentID,StudentID ,CourseID , EnrollmentDate )
    values 
    (1, 1, 1, '2023-01-10'),
    (2, 1, 3, '2023-01-15'),
    (3, 2, 2, '2023-01-12'),
    (4, 3, 1, '2023-01-14'),
    (5, 3, 4, '2023-01-16'),
    (6, 4, 2, '2023-01-11')
"""


cursor.execute('''
SELECT 
    s.FirstName, 
    s.LastName, 
    COUNT(e.CourseID) AS CourseCount
FROM 
    Students s
LEFT JOIN 
    Enrollments e ON s.StudentID = e.StudentID
GROUP BY 
    s.StudentID
ORDER BY 
    s.LastName
''')

results = cursor.fetchall()
for row1 in results:
    print(row1)

# Delete 
cursor.execute('''
DELETE FROM Students 
WHERE StudentID IN (
    SELECT StudentID 
    FROM Enrollments 
    GROUP BY StudentID 
    HAVING COUNT(CourseID) < 2
)
''')

# Update
cursor.execute('''
UPDATE Courses 
SET CourseName = 'Python'
WHERE CourseName LIKE '%Java%'
''')

# accept update
cursor.execute('SELECT * FROM Courses')
updated_courses = cursor.fetchall()
for course in updated_courses:
    print(course)


con.commit()
cursor.close()
con.close()