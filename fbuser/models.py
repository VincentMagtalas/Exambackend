from django.db import models

# Create your models here.
class FBUser(models.Model):
    FBID = models.CharField(max_length=100, blank=True, default='')
    Name = models.CharField(max_length=250,blank=True, default='')
    Email = models.CharField(max_length=250,blank=True, default='')
    DateRegistered = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('FBID','Name','Email','DateRegistered',)

    def __str__(self):
        return self.Name