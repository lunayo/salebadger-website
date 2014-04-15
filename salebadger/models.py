import datetime
from salebadger import db

class Subscriber(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(max_length=255, required=True)
    email = db.StringField(max_length=255, required=True)
    country = db.StringField(max_length=255)
    city = db.StringField(max_length=255)
    ip_address = db.StringField(max_length=255)

    def __unicode__(self):
        return self.email

    meta = {
        'indexes': ['-created_at', 'email']
    }
