from django.db import models

class File(models.Model):
    Inspection_Date = models.DateField(null = True)
    Permittee_Name = models.CharField(max_length = 150)
    Permit_ID = models.IntegerField(null = True)
    Full_Address = models.TextField(null = True)
    Inspection_Purpose = models.CharField(max_length = 100)
    Violation = models.BooleanField(default = True)
    Is_Critical = models.BooleanField(default = True)
    Short_Description = models.CharField(max_length = 100)
    Violation_Comments = models.TextField(null = True)
    GeoLocation = models.TextField(null = True)
