from flask import Blueprint, request, render_template, flash, redirect
from flask.views import MethodView
from salebadger.models import Subscriber
from salebadger.forms import SubscriberForm
import pygeoip

defaults = Blueprint('defaults', __name__, template_folder='templates')

class IndexView(MethodView):

    def get(self):
        form = SubscriberForm()
        return render_template('index.html', form=form)

    def post(self):
        form = SubscriberForm(request.form)
        if form.validate():
            # add to database
            subscriber = Subscriber()
            subscriber.name = form.name.data
            subscriber.email = form.email.data
            subscriber.ip_address = request.remote_addr
            gi = pygeoip.GeoIP('salebadger/static/geolocation/GeoIP.dat')
            countryRecord = gi.country_name_by_addr(request.remote_addr)
            if countryRecord is not None:
                subscriber.country = countryRecord
            gic = pygeoip.GeoIP('salebadger/static/geolocation/GeoLiteCity.dat')
            cityRecord = gic.record_by_addr(request.remote_addr)
            if cityRecord is not None and cityRecord['city']:
                subscriber.city = cityRecord['city']
            
            subscriber.save()

            flash('Thank you for your subscription.')

        return render_template('index.html', form=form)


defaults.add_url_rule('/', view_func=IndexView.as_view('index'))