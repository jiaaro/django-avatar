from urllib2 import urlopen

from django.db.models import Manager
from django.core.files.base import ContentFile

class AvatarManager(Manager):
    def create_from_url(self, url, *args, **kwargs):
        img = ContentFile(urlopen(url).read())
        
        avatar = self.create(*args, **kwargs)
        
        filename = url.split('/')[-1]
        avatar.avatar.save(filename, img)
        
        #avatar.save()
        return avatar