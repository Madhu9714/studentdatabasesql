USE student_db;

INSERT INTO student (id, name, age, grade) VALUES
(1, 'John', 20, 'A'),
(2, 'Mary', 21, 'B'),
(3, 'Sam', 19, 'A');

INSERT INTO course (id, course_name) VALUES
(101, 'Math'),
(102, 'Science'),
(103, 'History');

INSERT INTO enrollment (student_id, course_id) VALUES
(1, 101),
(2, 102),
(3, 103),
(1, 103);
