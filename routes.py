
from flask import render_template, url_for, flash, redirect, request, Response
from app import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from app.models import User, Patient, Doctor, Inventory, Billing, Payment, Appointment
from app.forms import RegistrationForm, LoginForm, PatientRegistrationForm, BillingForm, PaymentForm, ReportForm, InventoryForm

@app.route("/dashboard")
@login_required
def dashboard():
    if current_user.role == 'admin':
        return render_template('admin_dashboard.html')
    elif current_user.role == 'doctor':
        return render_template('doctor_dashboard.html')
    elif current_user.role == 'patient':
        return render_template('patient_dashboard.html')

# Exemplo de rota para autenticação
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

# Exemplo de rota para gerenciamento de inventário
@app.route("/inventory", methods=['GET', 'POST'])
@login_required
def manage_inventory():
    form = InventoryForm()
    low_stock_items = Inventory.query.filter(Inventory.quantity <= Inventory.reorder_level).all()
    if form.validate_on_submit():
        new_item = Inventory(item_name=form.item_name.data, category=form.category.data,
                             quantity=form.quantity.data, reorder_level=form.reorder_level.data,
                             supplier=form.supplier.data)
        db.session.add(new_item)
        db.session.commit()
        flash('New inventory item added!', 'success')
        return redirect(url_for('manage_inventory'))
    inventory = Inventory.query.all()
    return render_template('inventory.html', form=form, inventory=inventory, low_stock_items=low_stock_items)
