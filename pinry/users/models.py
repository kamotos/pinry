import hashlib

from django.contrib.auth.models import User as BaseUser


class User(BaseUser):
    @property
    def gravatar(self):
        return hashlib.md5(self.email).hexdigest()

    def facebook_picture(self):
        try:
       	   fid = self.social_auth.filter(provider="facebook")[0].uid
        except:
	   return
	return "https://graph.facebook.com/" + fid + "/picture?type=large"

    class Meta:
        proxy = True
