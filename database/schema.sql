-- creating database
CREATE DATABASE IF NOT EXISTS coaching_center;
USE coaching_center;
-- pheli table student bana raha hun 
CREATE TABLE IF NOT EXISTS students (
    student_id    INT AUTO_INCREMENT PRIMARY KEY,
    full_name     VARCHAR(100) NOT NULL,
    email         VARCHAR(100) UNIQUE,
    phone         VARCHAR(15),
    course        ENUM('Data Science', 'Fullstack', 'Salesforce'),
    batch_name    VARCHAR(50),
    joining_date  DATE,
    is_active     BOOLEAN DEFAULT TRUE
);
-- ab doosari table banate hai Batches 
CREATE TABLE IF NOT EXISTS batches (
    batch_id      INT AUTO_INCREMENT PRIMARY KEY,
    batch_name    VARCHAR(50) NOT NULL,
    course        ENUM('Data Science', 'Fullstack', 'Salesforce'),
    start_date    DATE,
    end_date      DATE,
    timing        VARCHAR(50),
    total_seats   INT DEFAULT 30
);
-- creating foregin key batch id 
ALTER TABLE students 
ADD COLUMN batch_id INT,
ADD FOREIGN KEY (batch_id) REFERENCES batches(batch_id);
-- fee table ab banana hai 
CREATE TABLE IF NOT EXISTS fees (
    fee_id          INT AUTO_INCREMENT PRIMARY KEY,
    student_id      INT NOT NULL,
    total_amount    DECIMAL(10,2) NOT NULL,
    paid_amount     DECIMAL(10,2) DEFAULT 0,
    payment_date    DATE,
    payment_mode    ENUM('Cash', 'Online', 'Cheque'),
    remarks         VARCHAR(200),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
); 
-- attendence table
CREATE TABLE IF NOT EXISTS attendance (
    attendance_id   INT AUTO_INCREMENT PRIMARY KEY,
    student_id      INT NOT NULL,
    batch_id        INT NOT NULL,
    date            DATE NOT NULL,
    status          ENUM('Present', 'Absent', 'Late'),
    remarks         VARCHAR(100),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (batch_id) REFERENCES batches(batch_id)
);
--  making test result table  
CREATE TABLE IF NOT EXISTS test_results (
    result_id       INT AUTO_INCREMENT PRIMARY KEY,
    student_id      INT NOT NULL,
    batch_id        INT NOT NULL,
    test_name       VARCHAR(100) NOT NULL,
    test_date       DATE,
    marks_obtained  DECIMAL(5,2),
    total_marks     DECIMAL(5,2),
    remarks         VARCHAR(200),
    source          ENUM('Manual', 'Google Sheets') DEFAULT 'Manual',
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (batch_id) REFERENCES batches(batch_id)
);
-- insertin quesry 
-- inserting data in table 
INSERT INTO batches (batch_name, course, start_date, end_date, timing, total_seats)
VALUES 
('DS-Jan-2025', 'Data Science', '2025-01-10', '2025-06-10', '10:00 AM - 12:00 PM', 30),
('FS-Mar-2025', 'Fullstack', '2025-03-01', '2025-08-01', '2:00 PM - 4:00 PM', 25),
('SF-Feb-2025', 'Salesforce', '2025-02-15', '2025-07-15', '6:00 PM - 8:00 PM', 20);
-- inserting data in student 
INSERT INTO students (full_name, email, phone, course, batch_name, joining_date, batch_id)
VALUES
('Rahul Sharma', 'rahul@gmail.com', '9876543210', 'Data Science', 'DS-Jan-2025', '2025-01-10', 1),
('Priya Singh', 'priya@gmail.com', '9876543211', 'Fullstack', 'FS-Mar-2025', '2025-03-01', 2),
('Amit Kumar', 'amit@gmail.com', '9876543212', 'Salesforce', 'SF-Feb-2025', '2025-02-15', 3),
('Neha Gupta', 'neha@gmail.com', '9876543213', 'Data Science', 'DS-Jan-2025', '2025-01-10', 1),
('Ravi Verma', 'ravi@gmail.com', '9876543214', 'Fullstack', 'FS-Mar-2025', '2025-03-01', 2); 
-- inserting data in fee table 
INSERT INTO fees (student_id, total_amount, paid_amount, payment_date, payment_mode, remarks)
VALUES
(1, 15000.00, 15000.00, '2025-01-10', 'Online', 'Full payment'),
(2, 18000.00, 10000.00, '2025-03-01', 'Cash', 'Partial payment'),
(3, 12000.00, 12000.00, '2025-02-15', 'Online', 'Full payment'),
(4, 15000.00, 5000.00, '2025-01-10', 'Cash', 'Partial payment'),
(5, 18000.00, 18000.00, '2025-03-01', 'Cheque', 'Full payment');
-- inserting some data in attendence 
INSERT INTO attendance (student_id, batch_id, date, status)
VALUES
(1, 1, '2025-04-01', 'Present'),
(2, 2, '2025-04-01', 'Absent'),
(3, 3, '2025-04-01', 'Present'),
(4, 1, '2025-04-01', 'Late'),
(5, 2, '2025-04-01', 'Present'),
(1, 1, '2025-04-02', 'Present'),
(2, 2, '2025-04-02', 'Present'),
(3, 3, '2025-04-02', 'Absent'); 
-- testing query 
-- Saare students dekho
SELECT * FROM students;
-- Sirf Data Science wale students
SELECT full_name, email, course 
FROM students 
WHERE course = 'Data Science';
-- Student aur uski batch detail saath mein dekho
SELECT 
    s.full_name,
    s.course,
    b.batch_name,
    b.timing
FROM students s
JOIN batches b ON s.batch_id = b.batch_id;
-- student with pending fees 
SELECT 
    s.full_name,
    f.total_amount,
    f.paid_amount,
    (f.total_amount - f.paid_amount) as pending_amount,
    f.payment_mode
FROM students s
JOIN fees f ON s.student_id = f.student_id
WHERE (f.total_amount - f.paid_amount) > 0; 
-- attendence check 
SELECT 
    s.full_name,
    s.course,
    a.date,
    a.status
FROM students s
JOIN attendance a ON s.student_id = a.student_id
WHERE a.date = '2025-04-01'
ORDER BY a.status;
-- Student, uski batch aur fee status ek saath
SELECT 
    s.full_name,
    s.course,
    b.timing,
    f.total_amount,
    f.paid_amount,
    (f.total_amount - f.paid_amount) as pending_amount
FROM students s
JOIN batches b ON s.batch_id = b.batch_id
JOIN fees f ON s.student_id = f.student_id
ORDER BY pending_amount DESC;