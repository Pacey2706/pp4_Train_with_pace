from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Trainer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField()
    specialties = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.user.username


class Session(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=1)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Booking(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_bookings')
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    review = models.OneToOneField('Review', on_delete=models.SET_NULL, null=True, blank=True, related_name='booking_review')

    def __str__(self):
        return f"{self.client.user.username} - {self.session.name}"


class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='booking')
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.booking}"
