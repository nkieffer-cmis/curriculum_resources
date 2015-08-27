from google.appengine.ext import ndb
import json

class Tag(ndb.Model):
    name = ndb.StringProperty()

class ResourceReview(ndb.Model):
    submitter = ndb.UserProperty(required=True)
    ts_created = ndb.DateTimeProperty(required=True)
    text = ndb.TextProperty(required=True)
    @property
    def dict(self):
        return { "submitter": self.submitter.nickname(),
                 "ts_created" : self.ts_created,
                 "text" : self.text }
class Resource(ndb.Model):
    title = ndb.StringProperty(required=True)
    description = ndb.TextProperty(required=True)
    ts_created = ndb.DateTimeProperty(required=True)
    ts_modified = ndb.DateTimeProperty(required=True)
    creator = ndb.UserProperty(required=False)
    urls = ndb.StringProperty(repeated=True)
    tags = ndb.StructuredProperty(Tag, repeated=True)
    reviews = ndb.StructuredProperty(ResourceReview, repeated=True)
    
    @classmethod
    def all(cls):
        resources = []
        for resource in  cls.query():
            resources.append(resource)
        return resources

    @property
    def dict(self):
        data = { "id": self.key.id(), 
                 "title" : self.title,
                 "description" : self.description,
                 "ts_created" : self.ts_created.isoformat(),
                 "ts_modified" : self.ts_modified.isoformat(),
                 "creator" : self.creator,
                 "urls" : self.urls,
                 "reviews" : [ r.dict for r in self.reviews ] }
        return data

