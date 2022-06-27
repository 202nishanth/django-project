from calendar import day_name
from distutils.command.upload import upload
from pickle import TRUE
from tarfile import PAX_NAME_FIELDS
from django.db import models

# Create departments sections.

class departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(departments, on_delete=models.CASCADE)
    dep_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr. ' + self.doc_name + ' - (' + self.doc_spec + ')'

class Booking(models.Model):
    Patient_name = models.CharField(max_length=200)
    Patient_phone = models.CharField(max_length=13)
    Patient_email = models.EmailField()
    Doc_name = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    Booking_date = models.DateField()
    Booked_on = models.DateField(auto_now=TRUE)






