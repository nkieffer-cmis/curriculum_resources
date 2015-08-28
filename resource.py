import webapp2
import dbmodels
import logging
import datetime
import json
from google.appengine.api import users


class Handler(webapp2.RequestHandler):
    def post(self):
        resource = dbmodels.Resource()
        params = self.request.params
        resource.title = params['title']
        resource.description = params['description']
        resource.ts_created = datetime.datetime.now()
        resource.ts_modified = datetime.datetime.now()
     #   resource.creator = users.get_current_user()
        resource.urls = params['urls'].split(",")
        resource.tags = [dbmodels.Tag(name=tag) for tag in params['tags'].split(",")]
        resource.put()
        logging.info("Created new resource: {}".format(resource.key.id()))
    
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
        if resource_id is None:
            data = dbmodels.Resource.all()
            logging.info(data)
            self.response.out.write(json.dumps([ resource.dict for resource in data]))
        else:
            logging.info(resource_id)
            resource = dbmodels.Resource.get_by_id(int(resource_id))
            self.response.out.write(json.dumps(resource.dict))
