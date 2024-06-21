from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DoctorProfile(models.Model):
    name = models.CharField(max_length=150)
    specialization = models.CharField(max_length=150,null=True)
    qualification = models.CharField(max_length=150,null=True)
    works_at = models.CharField(max_length=150,null=True)
    contact_no = models.CharField(max_length=150,null=True)
    email_id = models.EmailField(null=True)
    location = models.TextField(null=True)
    profile_photo = models.ImageField(upload_to='profile-upload/doctor/',null = True,)
    user = models.ForeignKey(User,models.DO_NOTHING)
    class Meta:
        verbose_name = 'DoctorProfiles'
        verbose_name_plural = 'DoctorProfiles'
        
    def __str__(self):
        return  self.name
    

class PatientProfile(models.Model):
    name = models.CharField(max_length=150,null=True)
    contact_no = models.CharField(max_length=150,null=True)
    email_id = models.EmailField(null=True)
    location = models.TextField(null=True)
    patient_case = models.CharField(max_length=150,null=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    profile_photo = models.ImageField(upload_to='profile-upload/patient/',null = True)
    user = models.ForeignKey(User,models.DO_NOTHING)
    
    class Meta:
        verbose_name = 'PatientProfiles'
        verbose_name_plural = 'PatientProfiles'
        
    def __str__(self):
        return  self.name
    