from config.db_config import get_connection

def get_all_students():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(''' SELECT * FROM students  
                   WHERE is_active = TRUE''')
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return students

def add_student(full_name, email, phone, course, batch_name, joining_date, batch_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO students 
        (full_name, email, phone, course, batch_name, joining_date, batch_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (full_name, email, phone, course, batch_name, joining_date, batch_id))
    connection.commit()
    new_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return new_id
# three more function 
def get_student_by_id(student_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    student = cursor.fetchone()
    cursor.close()
    connection.close()
    return student

def update_student_phone(student_id, new_phone):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE students 
        SET phone = %s 
        WHERE student_id = %s
    """, (new_phone, student_id))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"✅ Phone updated!")

def search_by_course(course):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE course = %s", (course,))
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return students 
# adding soft delete function 
def delete_student(student_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE students 
        SET is_active = FALSE 
        WHERE student_id = %s
    """, (student_id,))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"✅ Student deactivated!")