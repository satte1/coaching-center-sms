from config.db_config import get_connection

def get_all_pending_fees():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT 
            s.full_name,
            s.course,
            f.total_amount,
            f.paid_amount,
            (f.total_amount - f.paid_amount) as pending_amount,
            f.payment_mode
        FROM students s
        JOIN fees f ON s.student_id = f.student_id
        WHERE (f.total_amount - f.paid_amount) > 0
    """)
    pending = cursor.fetchall()
    cursor.close()
    connection.close()
    return pending

def add_payment(student_id, amount, payment_mode):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE fees 
        SET paid_amount = paid_amount + %s,
            payment_date = CURDATE(),
            payment_mode = %s
        WHERE student_id = %s
    """, (amount, payment_mode, student_id))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"✅ Payment of {amount} added!")

def get_fee_by_student(student_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT 
            s.full_name,
            f.total_amount,
            f.paid_amount,
            (f.total_amount - f.paid_amount) as pending,
            f.payment_date,
            f.payment_mode
        FROM students s
        JOIN fees f ON s.student_id = f.student_id
        WHERE s.student_id = %s
    """, (student_id,))
    fee = cursor.fetchone()
    cursor.close()
    connection.close()
    return fee