
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('admin', 'Admin'), ('doctor', 'Doctor'), ('patient', 'Patient')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class InventoryForm(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired(), Length(min=2, max=120)])
    category = StringField('Category', validators=[DataRequired(), Length(min=2, max=50)])
    quantity = StringField('Quantity', validators=[DataRequired()])
    reorder_level = StringField('Reorder Level', validators=[DataRequired()])
    supplier = StringField('Supplier', validators=[DataRequired(), Length(min=2, max=120)])
    submit = SubmitField('Add Item')

# Outros formulários (BillingForm, ReportForm, etc.) seguem uma estrutura similar
