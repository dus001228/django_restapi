from django.db import models

class daejeonnews(models.Model):
    id = models.Index = models.AutoField(primary_key=True)
    title = models.TextField()
    news_url = models.TextField()

    def __str__(self):
        return self.title

class daejeonweather(models.Model):
    id = models.Index = models.AutoField(primary_key=True)
    tmp = models.TextField()
    img_url = models.TextField()

    def __str__(self):
        return self.title

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

class daejeontour(models.Model):
    id = models.Index = models.AutoField(primary_key=True)
    category = models.TextField()
    title = models.TextField()
    address = models.TextField()
    call = models.TextField()
    room = models.TextField()
    img_url = models.TextField()

    def __str__(self):
        return self.title

class daejeonrest(models.Model):
    id = models.Index = models.AutoField(primary_key=True)
    category = models.TextField()
    title = models.TextField()
    address = models.TextField()
    call = models.TextField()
    homepage = models.TextField()
    img_url = models.TextField()

    def __str__(self):
        return self.title
