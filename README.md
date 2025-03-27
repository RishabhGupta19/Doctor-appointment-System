# Doctor Appointment System

![Doctor Appointment System](https://img.shields.io/badge/Doctor-Appointment%20System-blue)

## 🏥 About the Project
The **Doctor Appointment System** is a web-based application that allows patients to book appointments with doctors, manage their schedules, and keep track of medical records. The system is built using **Python (Flask)** and **MySQL**.

## 📌 Features
- 🏥 **Doctor Management**: Add, update, and delete doctor details.
- 📅 **Appointment Scheduling**: Patients can book and cancel appointments.
- 🔐 **User Authentication**: Secure login for doctors and patients.
- 📊 **Dashboard**: Admin and users can track appointments and activity.
- 💾 **Database Integration**: Uses MySQL to store appointment and user data.

---

## 🚀 Installation & Setup

### 🔧 Prerequisites
Make sure you have the following installed:
- Python 3.9+
- Flask
- MySQL
- Virtual Environment (Recommended)

### 📥 Clone the Repository
```sh
git clone https://github.com/RishabhGupta19/Doctor-appointment-System.git
cd Doctor-appointment-System
```

### ⚙️ Setting Up the Virtual Environment
```sh
python -m venv env
source env/bin/activate   # On macOS/Linux
env\Scripts\activate     # On Windows
```

### 📦 Install Dependencies
```sh
pip install -r requirements.txt
```

### 📂 Configure Database
1. Import `mynewsqul.sql` into your MySQL database.
2. Update `secret.py` with your database credentials:
   ```python
   DB_HOST = "your_host"
   DB_USER = "your_username"
   DB_PASSWORD = "your_password"
   DB_NAME = "your_database"
   ```

### ▶️ Run the Application
```sh
python app.py
```

The application will run on `http://127.0.0.1:5000/`

---



---

## 💡 Future Enhancements
- 📱 Mobile-responsive design
- 📧 Email notifications for appointment reminders
- 🏥 Multi-clinic support



## 📩 Contact
📧 Email: `rishabh134we@gmail.com`
GitHub: [RishabhGupta19](https://github.com/RishabhGupta19)

