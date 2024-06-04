from django.db import models

# Create your models here.

#region movie display -----------------------------------------------------------



class MovieDisplay(models.Model):
    display_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=25, blank=True, null=True)
    image = models.FileField(upload_to="images/", blank=False, null=False)

    
#endregion 
	