import webapp2
import dbmodels
import logging
import datetime
from google.appengine.api import users


class Create(webapp2.RequestHandler):
    def post(self):
        resource = dbmodels.Resource()
        params = self.request.params
        resource.title = params['title']
        resource.description = params['description']
        resource.ts_created = datetime.datetime.now()
        resource.ts_modified = datetime.datetime.now()
        resource.creator = users.get_current_user()
        resource.urls = params['urls'].split(",")
        resource.put()
        
        self.response.out.write(resource.to_dict())

class Retrieve(webapp2.RequestHandler):
    def get(self):
        pass
