# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello! Coaching Center SMS chal raha hai! 🎉"

# @app.route('/students')
# def students():
#     return "Yahan students ki list aayegi!"

# @app.route('/fees')
# def fees():
#     return "Yahan fees ki report aayegi!"

# if __name__ == '__main__':
#     app.run(debug=True)
#real student  ka data dekhten hai 
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello! Coaching Center SMS chal raha hai! 🎉"

# @app.route('/students')
# def students():
#     return "Yahan students ki list aayegi!"

# @app.route('/fees')
# def fees():
#     return "Yahan fees ki report aayegi!"

# if __name__ == '__main__':
#     app.run(debug=True)
# real student dekhaten hain  
# from flask import Flask
# from students.student_operations import get_all_students

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello! Coaching Center SMS chal raha hai! 🎉"

# @app.route('/students')
# def students():
#     all_students = get_all_students()
    
#     # HTML table banate hain
#     html = """
#     <h1>Students List</h1>
#     <table border='1'>
#         <tr>
#             <th>ID</th>
#             <th>Name</th>
#             <th>Email</th>
#             <th>Course</th>
#         </tr>
#     """
    
#     for s in all_students:
#         html += f"""
#         <tr>
#             <td>{s[0]}</td>
#             <td>{s[1]}</td>
#             <td>{s[2]}</td>
#             <td>{s[4]}</td>
#         </tr>
#         """
    
#     html += "</table>"
#     return html

# if __name__ == '__main__':
#     app.run(debug=True)
# updating files with templates 
# from flask import Flask, render_template
# from students.student_operations import get_all_students

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello! Coaching Center SMS chal raha hai! 🎉"

# @app.route('/students')
# def students():
#     all_students = get_all_students()
#     return render_template('students.html', students=all_students)

# if __name__ == '__main__':
#     app.run(debug=True)
# with fees page 
from flask import Flask, render_template, request, redirect, url_for, flash
from students.student_operations import get_all_students, add_student
from fees.fee_operations import get_all_pending_fees, add_payment
from attendance.attendance_operations import get_attendance_by_date, mark_attendance

app = Flask(__name__)
app.secret_key = 'coaching123'  # flash ke liye zaroori hai

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/students')
def students():
    all_students = get_all_students()
    return render_template('students.html', students=all_students)

@app.route('/students/add', methods=['GET', 'POST'])
def add_student_page():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course']
        batch_name = request.form['batch_name']
        joining_date = request.form['joining_date']
        batch_id = request.form['batch_id']

        add_student(full_name, email, phone, course, batch_name, joining_date, batch_id)
        
        flash(f'✅ {full_name} successfully add ho gaya!', 'success')
        return redirect(url_for('students'))
    
    return render_template('add_student.html')

@app.route('/fees')
def fees():
    pending = get_all_pending_fees()
    return render_template('fees.html', pending_fees=pending)

@app.route('/attendance')
def attendance():
    date = request.args.get('date', '2025-04-01')
    records = get_attendance_by_date(date)
    return render_template('attendance.html', records=records, date=date)

@app.route('/fees/pay', methods=['POST'])
def pay_fees():
    student_id = request.form['student_id']
    amount = request.form['amount']
    payment_mode = request.form['payment_mode']
    
    add_payment(student_id, amount, payment_mode)
    
    flash(f'✅ ₹{amount} payment successfully add ho gayi!', 'success')
    return redirect(url_for('fees'))

@app.route('/attendance/mark', methods=['POST'])
def mark_attendance_page():
    student_id = request.form['student_id']
    batch_id = request.form['batch_id']
    date = request.form['date']
    status = request.form['status']
    
    mark_attendance(student_id, batch_id, date, status)
    
    flash(f'✅ Attendance marked — {status}!', 'success')
    return redirect(url_for('attendance'))

if __name__ == '__main__':
    app.run(debug=True)