from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
#Job Application Model


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_img', blank=True, null=True )


class JobApplication(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Applied', 'Applied'),
        ('Interviewing', 'Interviewing'),
        ('Offer', 'Offer'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='applications')
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    application_date = models.DateField()
    job_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class InteractionNote(models.Model):
    job = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.job.company_name}"