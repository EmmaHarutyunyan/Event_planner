from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="events", null=True)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Canceled', 'Canceled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, null=True, blank=True)  
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.title if self.event else 'No Event'}"



class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.first_name} {self.last_name}"


class Package(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    benefits = models.TextField(help_text="List the benefits of this package")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="packages")
    events = models.ManyToManyField(Event, related_name="packages")
    image = models.ImageField(upload_to='packages/')
    available = models.BooleanField(default=True) 
    def __str__(self):
        return self.name

