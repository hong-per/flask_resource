from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class UserCreateForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(), Length(min=3, max=25)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=6), EqualTo('password_confirm', 'passwords do not match')])
    password_confirm = PasswordField(
        'Password Confirm', validators=[DataRequired()])


class UserLoginForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6)])


class ServerForm(FlaskForm):
    host = StringField('Host', validators=[DataRequired()])
    cpu = IntegerField('CPU', validators=[DataRequired()])
    memory = IntegerField('Memory', validators=[DataRequired()])
    storage = IntegerField('Storage', validators=[DataRequired()])


class DateForm(FlaskForm):
    date = DateField('Date', format='%Y%m%d', validators=[DataRequired()])


class UsageForm(FlaskForm):
    cpu_usage = IntegerField('CPU Usage', validators=[DataRequired()])
    memory_usage = IntegerField('Memory Usage', validators=[DataRequired()])
    storage_usage = IntegerField('Storage Usage', validators=[DataRequired()])
