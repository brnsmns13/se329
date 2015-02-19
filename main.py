import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>Hello world</h1>');


application = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
