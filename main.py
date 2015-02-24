import os

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

ANSWERS = ['A', 'B', 'C', 'D']
USER = 'test_user@iastate.edu'


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render());


class ResponsePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('respond.html')
        template_values = {
            'username': USER,
            'pin_default': 0
        }
        self.response.write(template.render(template_values));

    def post(self):
        pin = int(self.request.get('pin', -1))
        current_answer = int(self.request.get('answer', -1))

        template_values = {
            'username': USER,
            'pin_default': pin,
            'current_answer': ANSWERS[current_answer]
        }
        template = JINJA_ENVIRONMENT.get_template('respond.html')
        self.response.write(template.render(template_values));


class CreatePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('create.html')
        self.response.write(template.render())


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/respond', ResponsePage),
    ('/create', CreatePage)
], debug=True)
