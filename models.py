from google.appengine.ext import ndb


class Question(ndb.Model):
    question = ndb.StringProperty(indexed=False)
    answers = ndb.JsonProperty(indexed=False)
    correct_answer = ndb.StringProperty(indexed=False)

    @property
    def dict(self):
        return {
            'question': self.question,
            'answers': self.answers
        }


class Quiz(ndb.Model):
    questions = ndb.StructuredProperty(Question, repeated=True)
    code = ndb.IntegerProperty(indexed=True)
    name = ndb.StringProperty(indexed=False)
    userid = ndb.StringProperty(indexed=True)

    @property
    def dict(self):
        return {
            'questions': [q.dict for q in self.questions],
            'code': self.code,
            'name': self.name,
            'userid': self.userid
        }
