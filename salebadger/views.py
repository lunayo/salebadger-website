from flask import Blueprint, request, render_template
from flask.views import MethodView
from salebadger.models import Subscriber

defaults = Blueprint('defaults', __name__, template_folder='templates')

class IndexView(MethodView):

    def get(self):
        return render_template('index.html')


defaults.add_url_rule('/', view_func=IndexView.as_view('index'))