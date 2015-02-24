from google.appengine.ext import ndb

class Quiz(ndb.Model):
	questions = ndb.StructuredProperty(repeated=True)
	code=ndb.IntegerProperty(indexed=True)
	name=ndb.StringProperty(indexed=False)

class Question(ndb.Model):
	content=ndb.StringProperty(indexed=False)
	answers=ndb.StringProperty(repeated=True)
	correct_answer=ndb.StringProperty(indexed=False)