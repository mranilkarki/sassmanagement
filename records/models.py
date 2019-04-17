from django.db import models
from django.db.models import CharField
from datetime import datetime    



class list_students(models.Model):
    name = models.CharField(max_length=100, unique=False,null=True)
    birthdate = models.DateTimeField(default=datetime.now(),help_text="Please specify english date: <em>YYYY-MM-DD</em>.")
    placeofbirth= models.CharField(max_length=200, null=True,blank=True)
    FATHERLESS = 'Fatherless'
    MOTHERLESS = 'Motherless'
    PARENTS = 'Parents'
    family_stat = (
        (FATHERLESS, 'Fatherless'),
        (MOTHERLESS, 'Motherless'),
        (PARENTS, 'Parents'),
        
    )
    Family_status = models.CharField(
        max_length= 20,
        choices= family_stat,
        default= PARENTS,
    )

    class_attend= models.IntegerField(null=True,blank=True)
    school= models.CharField(max_length=200, null=True,blank=True)
    father= models.CharField(max_length=200, null=True, blank=True)
    mother= models.CharField(max_length=200, null=True,blank=True)
    family_history= models.TextField(blank=False, default='none')
    # Proimage= models.ImageField(upload_to='media/', blank=True, null='True',default='default.png')
    


    def __str__(self):
        return self.name

    # def clean_name(self):
    #     return self.cleaned_data["name"].upper()
class image_students(models.Model):
    image = models.FileField(upload_to='media/', default='default.png')



    
