from flask import Blueprint, render_template, jsonify
from flask_website.utils import request_wants_json
from flask_website.listings.projects import projects

mod = Blueprint('community', __name__, url_prefix='/community')


@mod.route('/')
def index():
    return render_template('community/index.html')


@mod.route('/irc/')
def irc():
    return render_template('community/irc.html')


@mod.route('/badges/')
def badges():
    return render_template('community/badges.html')


@mod.route('/poweredby/')
def poweredby():
    if request_wants_json():
        return jsonify((k, [p.to_json() for p in v])
                       for k, v in projects.iteritems())
    return render_template('community/poweredby.html', projects=projects)


@mod.route('/logos/')
def logos():
    return render_template('community/logos.html')
