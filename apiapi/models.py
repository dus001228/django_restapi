from django.db import models

class daejeonfood(models.Model):
    번호 = models.Index = models.AutoField(primary_key=True)
    업소명 = models.TextField()
    도로명주소 = models.TextField()
    소재지주소 = models.TextField()
    지정일자 = models.BigIntegerField()
    음식의유형 = models.TextField()
    주된음식종류 = models.TextField()
    전화번호 = models.TextField()
    

    def __str__(self):
        return self.title