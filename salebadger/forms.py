from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required, Email, ValidationError
from salebadger.models import Subscriber

def unique_email(form, field):
    if Subscriber.objects(email=field.data).count() >= 1:
        raise ValidationError('You have already subscribed.')
    

class SubscriberForm(Form):
    name = TextField('Name', validators=[Required()])
    email = TextField('Email', validators=[Required(), Email(message='Invalid email address.'), unique_email])

