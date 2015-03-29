import jinja2
import json
import logging
import os
import random
import webapp2

from google.appengine.api import users
from google.appengine.ext import ndb

from models import *


USER = 'test_user@iastate.edu'


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class BaseRequestHandler(webapp2.RequestHandler):
    def __init__(self, request=None, response=None):
        super(BaseRequestHandler, self).__init__(request, response)
        self.template_name = None
        self.template_values = {}

    def complete_request(self):
        template = JINJA_ENVIRONMENT.get_template(self.template_name)
        self.template_values.update({
            'login_url': users.create_login_url(self.request.uri),
            'logout_url': users.create_logout_url(self.request.uri),
            'user': users.get_current_user()
        })
        self.response.write(template.render(self.template_values))



class MainPage(BaseRequestHandler):
    def get(self):
        self.template_name = 'index.html'
        self.complete_request()


class ResponsePage(BaseRequestHandler):
    def get(self):
        self.template_name = 'respond.html'
        self.template_values = {
            'pin_default': 0
        }
        self.complete_request()

    def post(self):
        self.template_name = 'respond.html'
        pin = int(self.request.get('pin', -1))
        current_answer = self.request.get('answer')

        self.template_values = {
            'username': USER,
            'pin_default': pin,
            'current_answer': current_answer
        }
        self.complete_request()


class CreatePage(BaseRequestHandler):
    def get(self):
        self.template_name = 'create.html'
        self.complete_request()

    def post(self):
        logging.info(self.request.body)
        data = json.loads(self.request.body)
        quiz = Quiz()
        for q in data['questions']:
            question = Question(
                question=q['question'],
                answers=q['answers'],
                correct_answer=q['correctAnswer'])

            quiz.questions.append(question)

        quiz.name = data['name']
        quiz.put()


class QuizPage(BaseRequestHandler):
    def get(self):
        self.template_name = 'quizzes.html'
        quizzes = Quiz.query().fetch(10)
        self.template_values = {
            'quizzes': quizzes
        }
        self.complete_request()


class StartPage(BaseRequestHandler):
    def get(self):
        self.template_name = 'start.html'
        quiz_key = self.request.get('key')
        quiz = Quiz.get_by_id(quiz_key)
        rand_code = random.randint(1000, 2000)
        quiz.code = rand_code
        quiz.put()
        self.complete_request()


class PresentAPI(webapp2.RequestHandler):
    def get(self):
        quiz_key = self.request.get('quiz')
        question_number = self.request.get('question')
        quiz = Quiz.get_by_id(quiz_key)
        try:
            question = quiz.questions[int(question_number)]

        except IndexError:
            self.response.write('invalid question number')
            return

        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(question.dict))


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/respond', ResponsePage),
    ('/create', CreatePage),
    ('/quizzes', QuizPage),
    ('/start', StartPage)
], debug=True)
