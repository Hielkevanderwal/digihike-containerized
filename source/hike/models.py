from django.db import models 
from accounts.models import Team

# Create your models here.

class RouteSection(models.Model):
    section_name = models.CharField(max_length=150)
    section_html = models.TextField(null=True, blank=True)
    additional_form = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    hint = models.TextField(null=True, blank=True)
    ordering = models.IntegerField(default=-1)

    def __str__(self):
        return self.section_name

class Route(models.Model):
    route_name = models.CharField(max_length=150)
    route_sections = models.ManyToManyField(RouteSection)

    def __str__(self):
        return self.route_name

class RouteProgress(models.Model):
    team = models.ForeignKey(Team, on_delete = models.CASCADE)
    route = models.ForeignKey(Route, on_delete= models.CASCADE)
    progress = models.IntegerField(default=1)

class HintUsed(models.Model):
    class Meta:
        unique_together = ["team", "route_section"]
    
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    route_section = models.ForeignKey(RouteSection, on_delete=models.CASCADE)
    