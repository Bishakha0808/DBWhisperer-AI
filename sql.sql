CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    department VARCHAR(50),
    marks INT
);

INSERT INTO students (name, department, marks) VALUES
('Rahul', 'CSE', 85),
('Ananya', 'IT', 90),
('Rohit', 'CSE', 78),
('Priya', 'ECE', 88),
('Arjun', 'CSE', 92);
