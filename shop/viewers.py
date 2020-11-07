import redis
from django.conf import settings
from .models import Product


# connect to redis
r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)
            

class Viewer:
    '''
    Viewer is the object that update/retrieve the articles views.
    '''

    @staticmethod
    def addViewer(id):
        '''Add 1 to the article views'''
        
        i = Viewer.getViewers(id) + 1
        r.set(id, i)
        return i

    @staticmethod
    def getViewers(id):
        '''Return the article views stored in the redis db'''

        if r.get(id):
            return int(r.get(id))
        else:
            r.set(id, 0)
            return 0
    @staticmethod
    def clearViewers(id):
        '''Reset the article views'''

        r.set(id, 0)
        return 0