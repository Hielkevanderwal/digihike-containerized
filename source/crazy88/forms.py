from django.forms import ModelForm

from .models import MissionExecution

class MissionUploadForm(ModelForm):
    class Meta:
        model = MissionExecution
        fields = ["media","description"]
