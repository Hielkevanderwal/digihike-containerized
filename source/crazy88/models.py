import os

from django.db import models
from django.core.validators import FileExtensionValidator

from accounts.models import Team

# Create your models here.

class MissionList(models.Model):
    list_name = models.CharField(max_length=200, unique=True)
    missions = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.list_name
    
class MissionExecution(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    mission_list = models.ForeignKey(MissionList,on_delete=models.CASCADE)
    mission_number = models.IntegerField()
    
    upload_date = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    media = models.FileField(upload_to='uploads', validators = [FileExtensionValidator(allowed_extensions=['mp4','png', 'jpg', 'jpeg',"gif"])])
    
    validated = models.BooleanField(null=True, blank=True)

    def is_vid(self):
        name, extension = os.path.splitext(self.media.name)
        return extension in [".mp4"]
    