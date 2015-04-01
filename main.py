import jinja2
import json
import os
import random
import webapp2

from google.appengine.api import users

from models import *


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
            'login_url': users.create_login_url('/home'),
            'logout_url': users.create_logout_url('/'),
            'user': users.get_current_user()
        })

        self.response.write(template.render(self.template_values))

    def require_login(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
            return True


class AboutPage(BaseRequestHandler):
    def get(self):
        self.template_name = 'about.html'
        self.complete_request()


class DashboardPage(BaseRequestHandler):
    def get(self):
        if self.require_login():
            return

        self.template_name = 'dashboard.html'
        self.complete_request()


class UserPage(BaseRequestHandler):
    def get(self):
        if self.require_login():
            return

        self.template_name = 'user.html'
        self.complete_request()


class ResponsePage(BaseRequestHandler):
    def get(self):
        if self.require_login():
            return

        self.template_name = 'respond.html'
        self.template_values = {
            'pin_default': 0
        }

        self.complete_request()

    def post(self):
        if self.require_login():
            return

        pin = int(self.request.get('pin', -1))
        current_answer = self.request.get('answer')

        self.template_name = 'respond.html'
        self.template_values = {
            'pin_default': pin,
            'current_answer': current_answer
        }

        self.complete_request()


class CreatePage(BaseRequestHandler):
    def get(self):
        if self.require_login():
            return

        self.template_name = 'create.html'
        self.complete_request()

    def post(self):
        user = users.get_current_user()
        if not user:
            self.error(401)
            return

        data = json.loads(self.request.body)
        quiz = Quiz()
        for q in data['questions']:
            question = Question(
                question=q['question'],
                answers=q['answers'],
                correct_answer=q['correctAnswer'])

            quiz.questions.append(question)

        quiz.name = data['name']
        quiz.userid = user.user_id()
        quiz.put()


class QuizPage(BaseRequestHandler):
    def get(self):
        if self.require_login():
            return

        user = users.get_current_user()
        quizzes = Quiz.query(Quiz.userid == user.user_id()).fetch(10)

        self.template_name = 'quizzes.html'
        self.template_values = {
            'quizzes': quizzes
        }

        self.complete_request()


class StartPage(BaseRequestHandler):
    def post(self):
        if self.require_login():
            return
            
        self.template_name = 'start.html'
        quiz_id = int(self.request.get('quiz'))
        question_number = int(self.request.get('question', 0))
        quiz = Quiz.get_by_id(quiz_id, parent=None)

        try:
            question = quiz.questions[question_number]

        except IndexError:
            self.response.write('invalid question number')
            return
        
        if not quiz.code:
            quiz.code = random.randint(1000, 2000)
            quiz.put()

        self.template_values = {
            'name': quiz.name,
            'code': quiz.code,
            'quiz_id': quiz_id,
            'question': question.question,
            'answers': question.answers,
            'question_number': question_number + 1,
            'total_questions': len(quiz.questions)
        }

        self.complete_request()


application = webapp2.WSGIApplication([
    ('/', AboutPage),
    ('/home', DashboardPage),
    ('/respond', ResponsePage),
    ('/create', CreatePage),
    ('/quizzes', QuizPage),
    ('/start', StartPage),
    ('/user', UserPage)
], debug=True)
