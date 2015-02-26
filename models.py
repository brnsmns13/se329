from google.appengine.ext import ndb


class Question(ndb.Model):
    content=ndb.StringProperty(indexed=False)
    answers=ndb.JsonProperty(indexed=False)
    correct_answer=ndb.StringProperty(indexed=False)


class Quiz(ndb.Model):
    questions = ndb.StructuredProperty(Question, repeated=True)
    code = ndb.IntegerProperty(indexed=True)
    name = ndb.StringProperty(indexed=False)
