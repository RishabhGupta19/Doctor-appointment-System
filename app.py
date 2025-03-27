from flask import Flask, render_template, request, redirect, url_for # type: ignore
from flask_mysqldb import MySQL # type: ignore

app = Flask(__name__)
app.secret_key = "988d803aa58abffdd1bc2f2708336017"

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Rish@134'
app.config['MYSQL_DB'] = 'new_appointment'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    cursor.close()
    return render_template('index.html', doctors=doctors)

@app.route('/admin')
def admin():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    cursor.close()
    return render_template('admin.html', doctors=doctors)

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    name = request.form['name']
    specialization = request.form['specialization']
    availability = request.form['availability']
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO doctors (name, specialization, availability) VALUES (%s, %s, %s)", (name, specialization, availability))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('admin'))

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    patient_name = request.form['patient_name']
    patient_age = request.form['patient_age']
    patient_contact = request.form['patient_contact']
    doctor_id = request.form['doctor_id']
    appointment_date = request.form['appointment_date']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO patients (name, age, contact) VALUES (%s, %s, %s)", (patient_name, patient_age, patient_contact))
    patient_id = cursor.lastrowid
    cursor.execute("INSERT INTO appointments (patient_id, doctor_id, appointment_date) VALUES (%s, %s, %s)", (patient_id, doctor_id, appointment_date))
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for('appointment_booked', patient_id=patient_id, doctor_id=doctor_id, appointment_date=appointment_date))

@app.route('/appointment_booked')
def appointment_booked():
    patient_id = request.args.get('patient_id')
    doctor_id = request.args.get('doctor_id')
    appointment_date = request.args.get('appointment_date')

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM patients WHERE id = %s", [patient_id])
    patient = cursor.fetchone()
    cursor.execute("SELECT * FROM doctors WHERE id = %s", [doctor_id])
    doctor = cursor.fetchone()
    cursor.close()

    return render_template('appointment_booked.html', patient=patient, doctor=doctor, appointment_date=appointment_date)

if __name__ == '__main__':
    app.run(debug=True)
