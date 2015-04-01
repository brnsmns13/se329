import models
from test.utils import DatastoreBaseCase


class QuestionTestCase(DatastoreBaseCase):
    def test_question(self):
        test_question = models.Question(
            question='Test Question',
            answers={
                'A': 'First Answer',
                'B': 'Second Answer'
            },
            correct_answer='B')

        key = test_question.put()
        result = key.get()
        self.assertEqual(result.correct_answer, 'B')
        self.assertDictEqual(
            result.dict,
            {
                'question': 'Test Question',
                'answers': {
                    'A': 'First Answer',
                    'B': 'Second Answer'
                }
            }
        )


class QuizTestCase(DatastoreBaseCase):
    def test_quiz(self):
        q1 = models.Question(
            question='Test Question 1',
            answers={
                'A': 'First Answer',
                'B': 'Second Answer'
            },
            correct_answer='B')

        q2 = models.Question(
            question='Test Question 2',
            answers={
                'A': 'An Answer',
                'B': 'Another Answer'
            },
            correct_answer='A')

        test_quiz = models.Quiz(
            questions=[q1, q2],
            code=8675309,
            name='Test Quiz',
            userid='test.user-ID')

        key = test_quiz.put()
        result = key.get()
        self.assertDictEqual(
            result.dict,
            {
                'questions': [
                    {
                        'question': 'Test Question 1',
                        'answers': {
                            'A': 'First Answer',
                            'B': 'Second Answer'
                        }
                    },
                    {
                        'question': 'Test Question 2',
                        'answers': {
                            'A': 'An Answer',
                            'B': 'Another Answer'
                        }
                    }
                ],
                'code': 8675309,
                'name': 'Test Quiz',
                'userid': 'test.user-ID'
            }
        )
