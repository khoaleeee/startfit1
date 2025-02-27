from django.db import models
from django.utils import timezone


# Create your models here.

# class User(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField()
#     phonenumber=models.CharField(max_length=12)
#     passwd = models.CharField(max_length=100)
#     age = models.IntegerField()
#     year = models.IntegerField()

#     def __str__(self):
#         return self.name + ' ' + self.email
    
# class Activitie(models.Model):
#     name = models.TextField(max_length=100)
#     description = models.TextField(max_length=100)
#     bodyParts = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
    
class TrackedActivitie(models.Model):
    # id = models.IntegerField(primary_key=True)
    # userID = models.ForeignKey("user", on_delete=models.CASCADE)
    # activityID = models.ForeignKey("activitie", on_delete=models.CASCADE) 
    # date = models.DateField(max_length=10)
    activityType = models.CharField(max_length=100)
    duration = models.IntegerField()
    notes = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.activityType} on {self.date}"

    
    # class Meta:
    #         db_table="Coach_details"
    


 
     
