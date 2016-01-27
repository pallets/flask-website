# -*- coding: utf-8 -*-
from urlparse import urlparse
from flask import Markup


class Project(object):
    def __init__(self, name, url, description, source=None):
        self.name = name
        self.url = url
        self.description = Markup(description)
        self.source = source

    @property
    def host(self):
        if self.url is not None:
            return urlparse(self.url)[1]

    @property
    def sourcehost(self):
        if self.source is not None:
            return urlparse(self.source)[1]

    def to_json(self):
        rv = vars(self).copy()
        rv['description'] = unicode(rv['description'])
        return rv


projects = {
    'websites': [
        Project('Flask Website', 'http://flask.pocoo.org/', '''
            <p>
              The website of the Flask microframework itself including the
              mailinglist interface, snippet archive and extension registry.
        '''),
        Project('Brightonpy', 'http://brightonpy.org/', '''
            <p>
              The website of the Brighton Python User Group
        ''', source='http://github.com/j4mie/brightonpy.org/'),
        Project(u's h o r e … software development', 'http://shore.be/', '''
            <p>Corporate website of Shore Software Development.
        '''),
        Project(u'ROCKYOU.fm', 'https://www.rockyou.fm/', '''
            <p>
              ROCKYOU.fm is a german internet radio station and webzine
              featuring mostly metal and hard rock. Since 2012 the DJs and
              reporters provide their listeners with news, reviews, feature
              shows and interviews.
        '''),
        Project('Steven Harms\' Website', 'http://www.sharms.org/', u'''
            <p>
              Personal website of Steven Harms.
        ''', source='http://github.com/sharms/HomePage'),
        Project('ThadeusB\'s Website', 'http://thadeusb.com/', u'''
            <p>
              Personal website of ThadeusB.
        '''),
        Project('Blueslug', 'http://blueslug.com/', u'''
            <p>
              A flask-powered anti-social delicious clone
        '''),
        Project('Planete GT LL', None, u'''
            <p>
              News aggregator for the open source workgroup of the Paris Region
              innovation cluster, Systematic.
        ''', source='https://github.com/sfermigier/Planet-GTLL'),
        Project('Battlefield3 Development News Aggregator', None, u'''
            <p>
              Development news aggregator for Battlefield3.  Tracks twitter
              accounts and forum posts by DICE developers.
        ''', source='https://github.com/mitsuhiko/bf3-aggregator'),
        Project('Get Python 3', None, u'''
            <p>
              A website to collect feedback of Python third party
              libraries about its compatibility with Python 3
        ''', source='https://github.com/baijum/getpython3'),
        Project('DotShare', 'http://dotshare.it/', u'''
            <p>
              Socially driven website for sharing Linux/Unix dot files.
        '''),
        Project('saallergy.info', 'http://saallergy.info/', u'''
            <p>
              San Antonio Allergy Data
        '''),
        Project(
            'sopython', 'http://sopython.com/',
            '<p>Site of the Python chat room on Stack Overflow. '
            'Includes OAuth authentication, a wiki, and a growing, '
            'searchable list of "canonical" answers to Python '
            'questions on SO.</p>',
            source='https://github.com/sopython/sopython-site'
        )
    ],
    'apps': [
        Project('hg-review', None, '''
            <p>
              hg-review is a code review system for Mercurial.  It is available
              GPL2 license.
        ''', source='http://bitbucket.org/sjl/hg-review/'),
        Project('Cockerel', None, '''
            <p>
              An Online Logic Assistent Based on Coq.
        ''', source='http://github.com/dcolish/Cockerel'),
        Project('Ryshcate', None, '''
            <p>
              Ryshcate is a Flask powered pastebin with sourcecode
              available.
        ''', source='http://bitbucket.org/leafstorm/ryshcate/'),
        Project(u'Übersuggest Keyword Suggestion Tool', None, u'''
            <p>
              Übersuggest is a free tool that exploit the Google
              suggest JSON API to get keyword ideas for your search marketing
              campaign (PPC or SEO).
        ''', source='http://bitbucket.org/esaurito/ubersuggest'),
        Project('Have they emailed me?', None, '''
            <p>
              A mini-site for checking Google's GMail feed with Oauth.
        ''', source='http://github.com/lincolnloop/emailed-me'),
        Project('Remar.kZ', None, '''
            <p>
               Sometimes you use someone else's computer and find something
               neat and interesting.  Store it on Remar.kZ without having
               to enter your credentials.
        ''', source='http://bitbucket.org/little_arhat/remarkz'),
        Project('Dominion', None, u'''
            <p>
              Domination is a clone of a well-known card game.
        ''', source='https://bitbucket.org/xoraxax/domination/'),
        Project('jitviewer', None, '''
            <p>
              web-based tool to inspect the output of PyPy JIT log
        ''', source='https://bitbucket.org/pypy/jitviewer'),
        Project('blohg', 'http://blohg.org/', '''
            <p>
              A mercurial based blog engine.
        ''', source='https://github.com/rafaelmartins/blohg'),
        Project('pidsim-web', None, '''
            <p>
              PID Controller simulator.
        ''', source='https://github.com/rafaelmartins/pidsim-web'),
        Project('HTTPBin', 'http://httpbin.org/', u'''
            <p>
              An HTTP request & response service.
        ''', source='https://github.com/kennethreitz/httpbin'),
        Project('Flask-Pastebin', None, u'''
            <p>
              Pastebin app with Flask and a few extensions that does Facebook
              connect as well as realtime push notifications with socket.io
              and juggernaut.
        ''', source='https://github.com/mitsuhiko/flask-pastebin'),
        Project('newsmeme', None, u'''
            <p>
              A hackernews/reddit clone written with Flask and
              various Flask extensions.
        ''', source='https://bitbucket.org/danjac/newsmeme'),
    ]

}

# order projects by name
for _category in projects.itervalues():
    _category.sort(key=lambda x: x.name.lower())
del _category
