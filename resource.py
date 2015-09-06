import webapp2
import dbmodels
import logging
import datetime
import json
from generator import *
from google.appengine.api import users

def create_resource(params):
    resource = dbmodels.Resource()
    resource.title = params['title']
    resource.description = params['description']
    resource.ts_created = datetime.datetime.now()
    resource.ts_modified = datetime.datetime.now()
 #   resource.creator = users.get_current_user()
    resource.urls = params['urls'].split(",")
    resource.tags = [dbmodels.Tag(name=tag) for tag in params['tags'].split(",")]
    resource.put()
    logging.info("Created new resource: {}".format(resource.key.id()))

class Handler(webapp2.RequestHandler):

    def post(self):
        if self.request.params.has_key('generate'):
            logging.info("generating resources")
            num_resources = int(self.request.params['generate'])
            while num_resources > 0:
                params = { "title": sentence(),
                           "description": paragraph(),
                           "urls": ",".join([ "http://www.{}.com".format(word()) for _ in range(1,randint(3,6))]),
                           "tags": ",".join([ word() for _ in range(1, randint(2,5)) ]) }
                create_resource(params)
                num_resources -= 1
        else:
            params = self.request.params
            create_resource(params)
    
    def put(self, resource_id):
        resource = dbmodels.Resource.get_by_id(int(resource_id))
        params = self.request.params
        resource.title = params['title']
        resource.description = params['description']
        resource.ts_modified = datetime.datetime.now()
     #   resource.creator = users.get_current_user()
        resource.urls = params['urls'].split(",")
        logging.info("here")
     #   for tag in params['tags'].split(","):
          #  newTag = Tag(name=tag)
      #      logging.info(tag)
          #  resource.tags.append(newTag)
        resource.tags = [dbmodels.Tag(name=tag) for tag in params['tags'].split(",")]
        resource.put()
        logging.info("Modified resource: {}".format(resource_id))

    def delete(self, resource_id):
        resource = dbmodels.Resource.get_by_id(int(resource_id))
        resource.key.delete()
        logging.info("Deleted resource: {}".format(resource_id))

    def get(self, resource_id=None):
        is_admin = users.is_current_user_admin()
        if resource_id is None:
            data = dbmodels.Resource.all()
            logging.info(data)
            self.response.out.write(json.dumps([ is_admin, [resource.dict for resource in data]]))
        else:
            logging.info(resource_id)
            resource = dbmodels.Resource.get_by_id(int(resource_id))
            self.response.out.write(json.dumps([is_admin, resource.dict]))
