from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.name
    
    
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    link = models.URLField(max_length=200, blank=True)
    
    def __str__(self) -> str:
        return self.title
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE) # 1 project have 1 images 
    image = models.ImageField(upload_to="project_images/")
    
    def __str__(self) -> str:
        return f"{self.project.title} Image"
    
    