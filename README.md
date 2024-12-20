# Hospital Management System

This project is a hospital management system developed with Flask, enabling administrators, doctors, and patients to perform essential operations such as managing patients, appointments, inventory, billing, and report generation.

## System Structure

### Directories

- **app/**: Contains the core files of the Flask application.
  - **__init__.py**: Initializes the Flask app, database, and login functionality.
  - **models.py**: Defines models for users, patients, doctors, inventory, and billing.
  - **routes.py**: Defines routes for various functionalities.
  - **forms.py**: Contains forms used in the system.
  - **templates/**: Contains HTML templates for different pages.
  - **static/**: Contains the CSS file (`style.css`) and the JavaScript file (`main.js`).

- **schema.sql**: SQL script for creating database tables.

## Features

### 1. User Authentication
- **Functionality**: Administrators, doctors, and patients can register and log in. The system redirects users to an appropriate dashboard based on their role.
- **Technology**: Flask-Login, Bcrypt for encrypted passwords.

### 2. Patient Management
- **Functionality**: Administrators and doctors can manage patients, view and edit details, and schedule appointments.
- **Related Models**: User, Patient, Appointment.

### 3. Doctor Management
- **Functionality**: Administrators can manage doctor profiles. Doctors can view their appointments and manage patients.
- **Related Models**: User, Doctor, Appointment.

### 4. Inventory Management
- **Functionality**: Administrators can add, edit, and remove inventory items, with alerts for low stock levels.
- **Related Models**: Inventory.

### 5. Billing and Payments
- **Functionality**: Generate invoices for patients, process payments, and track pending and completed invoices.
- **Related Models**: Billing, Payment.

### 6. Reporting and Analytics
- **Functionality**: Administrators can generate financial, patient, and doctor performance reports.
- **Technology**: Dynamic report generation using Flask.

## How to Run

### 1. Clone the Repository
```bash
git clone <repository-URL>
cd hospital_management_system
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the Database
Initialize the database by running the SQL file:
```bash
sqlite3 hospital.db < schema.sql
```

### 5. Run the Server
```bash
python run.py
```

The application will be available at `http://127.0.0.1:5000/`.

## Dependencies
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Login
- Bcrypt

## Contribution
Feel free to submit pull requests or open issues for improvements.

## License

This project is free to use for educational purposes.
