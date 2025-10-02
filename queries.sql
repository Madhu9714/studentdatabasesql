USE student_db;

-- List all students
SELECT * FROM student;

-- Find students enrolled in Math
SELECT s.name
FROM student s
JOIN enrollment e ON s.id = e.student_id
JOIN course c ON e.course_id = c.id
WHERE c.course_name = 'Math';

-- Update a student grade
UPDATE student SET grade = 'A+' WHERE id = 2;

-- Delete a student
DELETE FROM student WHERE id = 3;
