from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    specialties = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class Session(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=3, decimal_places=1)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name