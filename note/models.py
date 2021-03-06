from django.db import models

from fbuser.models import FBUser

# Create your models here.
class Note(models.Model):
    FBID = models.ForeignKey(FBUser, related_name='Notes', on_delete=models.CASCADE)
    NoteTitle = models.CharField(max_length=100, blank=True, default='')
    NoteContent = models.TextField()
    DateCreated = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=100, blank=True, default='1')

    class Meta:
        ordering = ('FBID','NoteTitle','NoteContent','DateCreated','Status')

    def __str__(self):
        return self.NoteTitle