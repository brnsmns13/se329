import json

from google.appengine.api import users
from mock import patch
from webtest.app import TestApp

import main
from main import application, Question, Quiz
from test.utils import DatastoreBaseCase


class AboutPageTestCase(DatastoreBaseCase):
    def setUp(self):
        super(AboutPageTestCase, self).setUp()
        self.app = TestApp(application)

    def test_get(self):
        resp = self.app.get('/')

        resp.mustcontain(
            '<h1>Welcome to Clicker</h1>',
            '<li><a href="{url}">Login</a></li>'.format(
                url=users.create_login_url('/home')))


class DashboardPageTestCase(DatastoreBaseCase):
    def setUp(self):
        super(DashboardPageTestCase, self).setUp()
        self.app = TestApp(application)

    def test_get(self):
        self.login(**DatastoreBaseCase.DEFAULT_USER)

        resp = self.app.get('/home')

        resp.mustcontain(
            '<h1>Dashboard</h1>',
            '<h3>Welcome test.user@iastate.edu</h3>')

    def test_get_login_required(self):
        resp = self.app.get('/home', status=302)

        resp.mustcontain(no=[
            '<h1>Dashboard</h1>',
            '<h3>Welcome test.user@iastate.edu</h3>'])


class UserPageTestCase(DatastoreBaseCase):
    def setUp(self):
        super(UserPageTestCase, self).setUp()
        self.app = TestApp(application)

    def test_get(self):
        self.login(**DatastoreBaseCase.DEFAULT_USER)

        resp = self.app.get('/user')

        resp.mustcontain(
            '<h1>User Page</h1>')

    def test_get_login_required(self):
        resp = self.app.get('/user', status=302)

        resp.mustcontain(no=[
            '<h1>User Page</h1>'])


class ResponsePageTestCase(DatastoreBaseCase):
    def setUp(self):
        super(ResponsePageTestCase, self).setUp()
        self.app = TestApp(application)

    def test_get(self):
        self.login(**DatastoreBaseCase.DEFAULT_USER)

        resp = self.app.get('/respond')

        resp.mustcontain(
            '<h1>Respond to a Quiz</h1>',
            '<input name="pin" id="pin" class="form-control" type="number" '
            'value="0">',
            '<h4>Current User: test.user@iastate.edu</h4>',
            '<h4>Submitted Response: </h4>')

    def test_get_login_required(self):
        resp = self.app.get('/respond', status=302)

        resp.mustcontain(no=[
            '<h1>Respond to a Quiz</h1>',
            '<input name="pin" id="pin" class="form-control" type="number" '
            'value="0">',
            '<h4>Current User: test.user@iastate.edu</h4>',
            '<h4>Submitted Response: </h4>'])

    def test_post(self):
        self.login(**DatastoreBaseCase.DEFAULT_USER)

        resp = self.app.post('/respond?pin=7&answer=B')

        resp.mustcontain(
            '<h1>Respond to a Quiz</h1>',
            '<input name="pin" id="pin" class="form-control" type="number" '
            'value="7">',
            '<h4>Current User: test.user@iastate.edu</h4>',
            '<h4>Submitted Response: B</h4>')

    def test_post_no_pin(self):
        self.login(**DatastoreBaseCase.DEFAULT_USER)

        resp = self.app.post('/respond?answer=B')

        resp.mustcontain(
            '<h1>Respond to a Quiz</h1>',
            '<input name="pin" id="pin" class="form-control" type="number" '
            'value="-1">',
            '<h4>Current User: test.user@iastate.edu</h4>',
            '<h4>Submitted Response: B</h4>')

    def test_post_login_required(self):
        resp = self.app.post('/respond?pin=7&answer=B', status=302)

        resp.mustcontain(no=[
            '<h1>Respond to a Quiz</h1>',
            '<input name="pin" id="pin" class="form-control" type="number" '
            'value="7">',
            '<h4>Current User: test.user@iastate.edu</h4>',
            '<h4>Submitted Response: B</h4>'])


class CreatePageTestCase(DatastoreBaseCase):
    def setUp(self):
        super(CreatePageTestCase, self).setUp()
        self.app = TestApp(application)

    def test_get(self):
        self.login(**DatastoreBaseCase.DEFAULT_USER)

        resp = self.app.get('/create')

        resp.mustcontain(
            '<h1>Create a Quiz</h1>')

    def test_get_login_required(self):
        resp = self.app.get('/create', status=302)

        resp.mustcontain(no=[
            '<h1>Create a Quiz</h1>'])

    def test_post(self):
        self.login(**DatastoreBaseCase.DEFAULT_USER)

        self.app.post('/create', params=json.dumps({
            'name': 'Test Quiz',
            'questions': [
                {
                    'question': 'Test Question 1',
                    'answers': {
                        'A': 'First Answer',
                        'B': 'Second Answer'
                    },
                    'correctAnswer': 'B'
                },
                {
                    'question': 'Test Question 2',
                    'answers': {
                        'A': 'An Answer',
                        'B': 'Another Answer'
                    },
                    'correctAnswer': 'A'
                }
            ]
        }))

        user_id = DatastoreBaseCase.DEFAULT_USER['user_id']
        result = Quiz.query(Quiz.userid == user_id).fetch()[0]

        self.assertDictEqual(result.dict, {
            'questions': [
                {
                    'question': 'Test Question 1',
                    'answers': {
                        'A': 'First Answer',
                        'B': 'Second Answer'}
                },
                {
                    'question': 'Test Question 2',
                    'answers': {
                        'A': 'An Answer',
                        'B': 'Another Answer'},
                }
            ],
            'code': None,
            'name': 'Test Quiz',
            'userid': user_id
        })

    def test_post_login_required(self):
        self.app.post('/create', status=401)

        user_id = DatastoreBaseCase.DEFAULT_USER['user_id']
        quizes = Quiz.query(Quiz.userid == user_id).fetch()
        self.assertEqual(len(quizes), 0)


class QuizPageTestCase(DatastoreBaseCase):
    def setUp(self):
        super(QuizPageTestCase, self).setUp()
        q1 = Question(
            question='Test Question 1',
            answers={
                'A': 'First Answer',
                'B': 'Second Answer'
            },
            correct_answer='B')

        q2 = Question(
            question='Test Question 2',
            answers={
                'A': 'An Answer',
                'B': 'Another Answer'
            },
            correct_answer='A')

        q3 = Question(
            question='Test Question 3',
            answers={
                'A': 'Alpha',
                'B': 'Bravo',
                'C': 'Charlie'
            },
            correct_answer='C')

        q4 = Question(
            question='Test Question 4',
            answers={
                'A': 'Good Luck'
            },
            correct_answer='B')

        Quiz(
            questions=[q1, q2],
            code=8675309,
            name='Test Quiz 1',
            userid='test.user-ID').put()

        Quiz(
            questions=[q3],
            code=1234,
            name='Test Quiz 2',
            userid='test.user-ID').put()

        Quiz(
            questions=[q4],
            code=5678,
            name='Test Quiz 3',
            userid='another.user-ID').put()

        self.app = TestApp(application)

    def test_get(self):
        self.login(**DatastoreBaseCase.DEFAULT_USER)

        resp = self.app.get('/quizzes')

        resp.mustcontain(
            '<h1>Quizzes</h1>',
            'Test Quiz 1',
            'Test Quiz 2',
            no=[
                'Test Quiz 3'])

    def test_get_login_required(self):
        resp = self.app.get('/quizzes', status=302)

        resp.mustcontain(
            no=[
                '<h1>Quizzes</h1>',
                'Test Quiz 1',
                'Test Quiz 2',
                'Test Quiz 3'])


class StartPageTestCase(DatastoreBaseCase):
    def setUp(self):
        super(StartPageTestCase, self).setUp()
        self.mock_randint = patch.object(
            main.random, 'randint', autospec=True).start()

        self.mock_randint.return_value = 8675309

        q1 = Question(
            question='Test Question 1',
            answers={
                'A': 'First Answer',
                'B': 'Second Answer'
            },
            correct_answer='B')

        q2 = Question(
            question='Test Question 2',
            answers={
                'A': 'An Answer',
                'B': 'Another Answer'
            },
            correct_answer='A')

        self.quiz_key = Quiz(
            questions=[q1, q2],
            code=None,
            name='Test Quiz',
            userid='test.user-ID').put()

        self.app = TestApp(application)

    def test_get(self):
        self.login(**DatastoreBaseCase.DEFAULT_USER)

        self.app.get('/start?key=' + str(self.quiz_key.id()))

    def test_get_login_required(self):
        self.app.get('/start?key=' + str(self.quiz_key.id()), status=302)
