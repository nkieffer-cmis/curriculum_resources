from google.appengine.ext import ndb
import json

class ResourceReview(ndb.Model):
    submitter = ndb.UserProperty(required=True)
    ts_created = ndb.DateTimeProperty(required=True)
    text = ndb.TextProperty(required=True)

class Resource(ndb.Model):
    title = ndb.StringProperty(required=True)
    description = ndb.TextProperty(required=True)
    ts_created = ndb.DateTimeProperty(required=True)
    ts_modified = ndb.DateTimeProperty(required=True)
    creator = ndb.UserProperty(required=True)
    urls = ndb.StringProperty(repeated=True)
    reviews = ndb.StructuredProperty(ResourceReview, repeated=True)
    
    @property
    def json(self):
        data = json.dump({ "title" : self.title,
                          "description" : self.description,
                          "ts_created" : self.ts_created,
                          "ts_modified" : self.ts_modified,
                          "creator" : self.creator,
                          "urls" : self.urls,
                          "reviews" : self.reviews })
        return data
