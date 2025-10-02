USE student_db;

CREATE TABLE student (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(10)
);

CREATE TABLE course (
    id INT PRIMARY KEY,
    course_name VARCHAR(50)
);

CREATE TABLE enrollment (
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES student(id),
    FOREIGN KEY (course_id) REFERENCES course(id)
);
