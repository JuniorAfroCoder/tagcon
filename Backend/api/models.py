# models.py
from django.db import models

SEX_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]
class Attendee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, default='sex')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tagcon_attendees'  



class Exhibitor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    company_description = models.TextField()
    space_needed = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tagcon_exhibitors' 

class Volunteer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, default='sex')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tagcon_volunteers' 

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=200, default='TAGCON Get In Touch')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tagcon_contacts'