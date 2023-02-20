from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField
from wtforms.validators import InputRequired, ValidationError, Email, Regexp, Length
from wtforms.widgets import TextArea

class ContactForm(FlaskForm):
    PREFIX = "Please enter %s"
    INPUT_CLASS = "form-control input-field"
    title = "Contact Form"
    description = "Fill in this form to contact the site owners."
    name = StringField('Name', validators=[InputRequired()], description=PREFIX % "your full name.", render_kw={"class": INPUT_CLASS, "placeholder": "Marlon Lewis"})
    email = EmailField('Email', validators=[InputRequired(), Email(message="Don't forget to include the '@' sign in your email. i.e. 'user@domain.server'")], description=PREFIX % "your email address.", render_kw={"class": INPUT_CLASS, "placeholder": "example@email.com"})
    subject = StringField('Subject', validators=[InputRequired()], description=PREFIX % "the subject for your message.", render_kw={"class": INPUT_CLASS, "placeholder": "My Email Subject"})
    message = TextAreaField('Message', validators=[InputRequired()], description=PREFIX % "the message you would like to send.", render_kw={"class": INPUT_CLASS, "rows": 7}, widget=TextArea())
        
    def setEmail(self, email):
        self.email=email    
    
    def clean_String(self, string):
        if string is None:
            return ""
        return str(string).strip()
    
    def copy_field(self, name):
        for field in self:
            if field.label.lower() == name:
                return field