from flask import Flask
from flask.ext.mongoengine import MongoEngine

def register_blueprints(app):
    # Prevents circular imports
    from salebadger.views import defaults
    app.register_blueprint(defaults)

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': 'salebadger'}
app.config["SECRET_KEY"] = "Inc0rr3cT"

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()

register_blueprints(app)