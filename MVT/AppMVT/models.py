from django.db import models

class Contact(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.CharField(max_length=400)

    def __unicode__(self):
        return self.full_name



class Languages(models.Model):
     language=models.CharField(max_length=50)
     text=models.CharField(max_length=600)

     def __unicode__(self):
        return self.language