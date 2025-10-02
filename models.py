from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Define the base class
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    age = Column(Integer)
    # Add more fields as per your database schema

# Define the Course model
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String, nullable=False)
    # Add more fields as per your database schema

# Define the Enrollment model (many-to-many relationship)
class Enrollment(Base):
    __tablename__ = 'enrollments'
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    grade = Column(String)
    # Add more fields as per your database schema

# Create an engine and a session
engine = create_engine('sqlite:///student_database.db')  # Use your actual database URI
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables
Base.metadata.create_all(engine)

# Example of adding a new student
new_student = Student(name='John Doe', email='john.doe@example.com', age=20)
session.add(new_student)
session.commit()

# Query all students
students = session.query(Student).all()
for student in students:
    print(student.name, student.email, student.age)

session.close()
