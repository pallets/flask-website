from __future__ import with_statement
from flask import Blueprint, render_template, redirect


mod = Blueprint('mailinglist', __name__, url_prefix='/mailinglist')


@mod.route('/')
def index():
    return render_template('mailinglist/index.html')


@mod.route('/archive/', defaults={'page': 1})
@mod.route('/archive/page/<int:page>/')
def archive(page):
    return redirect('http://librelist.com/browser/flask/')


@mod.route('/archive/<int:year>/<int:month>/<int:day>/<slug>/')
def show_thread(year, month, day, slug):
    return redirect('http://librelist.com/browser/flask/%s/%s/%s/%s'
                    % (year, month, day, slug))
