from config.db_config import get_connection

def mark_attendance(student_id, batch_id, date, status):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO attendance 
        (student_id, batch_id, date, status)
        VALUES (%s, %s, %s, %s)
    """, (student_id, batch_id, date, status))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"✅ Attendance marked - {status}")

def get_attendance_by_date(date):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT 
            s.full_name,
            s.course,
            a.date,
            a.status
        FROM students s
        JOIN attendance a ON s.student_id = a.student_id
        WHERE a.date = %s
        ORDER BY a.status
    """, (date,))
    attendance = cursor.fetchall()
    cursor.close()
    connection.close()
    return attendance

def get_student_attendance_report(student_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT 
            COUNT(*) as total_days,
            SUM(CASE WHEN status = 'Present' THEN 1 ELSE 0 END) as present_days,
            SUM(CASE WHEN status = 'Absent' THEN 1 ELSE 0 END) as absent_days
        FROM attendance
        WHERE student_id = %s
    """, (student_id,))
    report = cursor.fetchone()
    cursor.close()
    connection.close()
    return report