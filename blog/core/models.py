from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='members_profile')

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)