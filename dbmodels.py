from google.appengine.ext import ndb
import json

class Tag(ndb.Model):
    name = ndb.StringProperty()
    @property
    def dict(self):
        return { "name": self.name }

class ResourceReview(ndb.Model):
    submitter = ndb.UserProperty(required=True)
    ts_created = ndb.DateTimeProperty(required=True, auto_now_add=True)
    text = ndb.TextProperty(required=True)

    @classmethod
    def query_resource(cls, ancestor_key):
        return cls.query(ancestor=ancestor_key).order(-cls.ts_created)

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
    category = ndb.StringProperty()
    
    @classmethod
    def all(cls):
        resources = []
        for resource in  cls.query():
            resources.append(resource)
        return resources

    @property
    def dict(self):
        data = { "key": self.key.id(), 
                 "title" : self.title,
                 "description" : self.description,
                 "ts_created" : self.ts_created.isoformat(),
                 "ts_modified" : self.ts_modified.isoformat(),
                 "creator" : self.creator,
                 "urls" : self.urls,
                 "tags" : [ tag.name for tag in self.tags ],
                 "reviews" : [ r.dict for r in ResourceReview.query_resource(self.key) ] }
        return data

class Star(ndb.Model):
    resource = ndb.KeyProperty(kind=Resource)
    user = ndb.UserProperty()
