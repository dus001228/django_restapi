from django.db import models

class daejeonfood(models.Model):
    id = models.Index = models.AutoField(primary_key=True)
    title = models.TextField()
    new_add = models.TextField()
    소재지주소 = models.TextField()
    지정일자 = models.BigIntegerField()
    음식의유형 = models.TextField()
    주된음식종류 = models.TextField()
    call = models.TextField()
    img_url = models.TextField()

    

    def __str__(self):
        return self.title
