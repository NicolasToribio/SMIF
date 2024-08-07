from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True) #only unique names allowed

    def __str__(self):
        return self.name
    

class Project(models.Model): #inheriting from the base model
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    link = models.URLField(max_length=200, blank=True) #Blank = True allows blank space inputs

    def __str__(self):
        return self.title
    
#Creating a model to store the images for our project 
class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
        ) #Specify the image that the project exists for. We only have a single project that the image exists for, so we use a foreign key. We CASCADE on delete to ensure that if the project were deleted, the images would be deleted along with them.
    image = models.ImageField(upload_to="project_images/")

    def __str__(self):
        return f"{self.project.title} Image" 
    


    
