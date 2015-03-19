import jinja2
import json
import logging
import os
import random
import webapp2

from google.appengine.api import users
from google.appengine.ext import ndb

from models import *


ANSWERS = [None, 'A', 'B', 'C', 'D']
USER = 'test_user@iastate.edu'


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        template_values = {
            'login_url': users.create_login_url(self.request.uri),
            'logout_url': users.create_logout_url(self.request.uri),
            'user': users.get_current_user()
        }
        self.response.write(template.render(template_values))


class ResponsePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('respond.html')
        template_values = {
            'username': USER,
            'pin_default': 0
        }
        self.response.write(template.render(template_values))

    def post(self):
        pin = int(self.request.get('pin', -1))
        current_answer = int(self.request.get('answer', -1))

        template_values = {
            'username': USER,
            'pin_default': pin,
            'current_answer': ANSWERS[current_answer]
        }
        template = JINJA_ENVIRONMENT.get_template('respond.html')
        self.response.write(template.render(template_values))


class CreatePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('create.html')
        self.response.write(template.render())

    def post(self):
        logging.info(self.request.body)
        data = json.loads(self.request.body)
        quiz = Quiz()
        for question in data['questions']:
            question = Question(
                content=question['question'],
                answers=[question['a'], question['b'],
                         question['c'], question['d']],
                correct_answer=question['correctAnswer'])

            quiz.questions.append(question)

        quiz.name = data['name']
        quiz.put()


class QuizPage(webapp2.RequestHandler):
    def get(self):
        quizzes = Quiz.query().fetch(10)
        template_values = {
            'quizzes': quizzes
        }
        
        template = JINJA_ENVIRONMENT.get_template('quizzes.html')
        self.response.write(template.render(template_values))


class StartPage(webapp2.RequestHandler):
    def get(self):
        quiz_key = self.request.get('key')
        quiz = Quiz.get_by_id(quiz_key)
        rand_code = random.randint(1000, 2000)
        quiz.code = rand_code
        quiz.put()
        template_values = {
        }
        
        template = JINJA_ENVIRONMENT.get_template('start.html')
        self.response.write(template.render(template_values))


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
        self.response.write(question.as_json())


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/respond', ResponsePage),
    ('/create', CreatePage),
    ('/quizzes', QuizPage),
    ('/start', StartPage)
], debug=True)
