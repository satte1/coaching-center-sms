# from config.db_config import get_connection

# # Connection test karte hain
# connection = get_connection()

# if connection.is_connected():
#     print("✅ Database se connection successful!")
# else:
#     print("❌ Connection failed!")

# connection.close()


# connection = get_connection()

# if connection.is_connected():
#     print("✅ Database se connection successful!\n")
    
#     # Data fetch karte hain
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM students")
    
#     students = cursor.fetchall()
    
#     print("--- Saare Students ---")
#     for student in students:
#         print(student)
    
#     cursor.close()

# connection.close()
## refresh code to display output in better way 
# from config.db_config import get_connection

# connection = get_connection()
# cursor = connection.cursor()

# cursor.execute("SELECT * FROM students")
# students = cursor.fetchall()

# print("=" * 50)
# print("      COACHING CENTER - STUDENTS LIST")
# print("=" * 50)

# for student in students:
#     print(f"ID    : {student[0]}")
#     print(f"Name  : {student[1]}")
#     print(f"Email : {student[2]}")
#     print(f"Course: {student[4]}")
#     print("-" * 50)

# cursor.close()
# connection.close()
## python se data insert karna 
# from config.db_config import get_connection

# connection = get_connection()
# cursor = connection.cursor()

# # Naya student add karna
# new_student = (
#     "Sana Khan",
#     "sana@gmail.com", 
#     "9876543215",
#     "Data Science",
#     "DS-Jan-2025",
#     "2025-01-10",
#     1
# )

# cursor.execute("""
#     INSERT INTO students 
#     (full_name, email, phone, course, batch_name, joining_date, batch_id)
#     VALUES (%s, %s, %s, %s, %s, %s, %s)
# """, new_student)

# connection.commit()  # yeh zaroori hai!

# print(f"✅ Student added! ID: {cursor.lastrowid}")

# cursor.close()
# connection.close()
## isko   test karten hain 
# from students.student_operations import get_all_students, add_student

# # Saare students dekho
# students = get_all_students()
# for student in students:
#     print(f"{student[0]} - {student[1]} - {student[4]}")

# print("---")

# # Naya student add karo
# new_id = add_student(
#     "Rahul Verma",
#     "rahulv@gmail.com",
#     "9876543216",
#     "Fullstack",
#     "FS-Mar-2025",
#     "2025-03-01",
#     2
# )
# print(f"✅ Naya student add hua! ID: {new_id}")
from students.student_operations import (
    get_student_by_id, 
    update_student_phone, 
    search_by_course
)

# Test 1 - ek student dhundo
# student = get_student_by_id(1)
# print(f"Student: {student[1]} - {student[4]}")

# print("---")

# # Test 2 - phone update karo
# update_student_phone(1, "9999999999")

# # confirm karo
# student = get_student_by_id(1)
# print(f"Updated Phone: {student[3]}")

# print("---")

# # Test 3 - course wise search
# print("Data Science Students:")
# ds_students = search_by_course("Data Science")
# for s in ds_students:
#     print(f"  {s[1]} - {s[2]}")
# from students.student_operations import delete_student

# # Student 7 ko deactivate karo
# delete_student(7)

# # Confirm karo - sirf active students dekho
# from students.student_operations import get_all_students
# students = get_all_students()
# print(f"Active students: {len(students)}") 
### testing fee operation 
from fees.fee_operations import (
    get_all_pending_fees,
    add_payment,
    get_fee_by_student
)

# Test 1 - pending fees dekho
# print("=" * 50)
# print("PENDING FEES REPORT")
# print("=" * 50)
# pending = get_all_pending_fees()
# for p in pending:
#     print(f"Name    : {p[0]}")
#     print(f"Course  : {p[1]}")
#     print(f"Total   : {p[2]}")
#     print(f"Paid    : {p[3]}")
#     print(f"Pending : {p[4]}")
#     print("-" * 50)

# # Test 2 - payment add karo
# print("\nAdding payment for Priya Singh...")
# add_payment(2, 5000, "Online")

# # Test 3 - confirm karo
# fee = get_fee_by_student(2)
# print(f"\nUpdated Fee Status:")
# print(f"Name    : {fee[0]}")
# print(f"Total   : {fee[1]}")
# print(f"Paid    : {fee[2]}")
# print(f"Pending : {fee[3]}") 
### attendence report check karna 
from attendance.attendance_operations import (
    mark_attendance,
    get_attendance_by_date,
    get_student_attendance_report
)

# Test 1 - aaj ki attendance mark karo
print("Marking attendance...")
mark_attendance(1, 1, "2025-04-27", "Present")
mark_attendance(2, 2, "2025-04-27", "Absent")
mark_attendance(3, 3, "2025-04-27", "Present")

# Test 2 - aaj ki report dekho
print("\n" + "=" * 50)
print("ATTENDANCE REPORT - 2025-04-27")
print("=" * 50)
attendance = get_attendance_by_date("2025-04-27")
for a in attendance:
    print(f"{a[0]} - {a[2]} - {a[3]}")

# Test 3 - ek student ki poori report
print("\n" + "=" * 50)
print("RAHUL SHARMA - ATTENDANCE SUMMARY")
print("=" * 50)
report = get_student_attendance_report(1)
print(f"Total Days  : {report[0]}")
print(f"Present     : {report[1]}")
print(f"Absent      : {report[2]}")