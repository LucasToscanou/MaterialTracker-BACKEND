from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()
    
    def __str__(self):
        return self.user.email
    
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Material(models.Model):
    ref = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    main_img = models.ImageField(default="{% static 'img/MaterialTrackerApp/generic_user.png' %}", blank=True)
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    cost = models.FloatField()
    currency = models.TextField(blank=True)
    quality_exp_date = models.DateTimeField(default=timezone.now)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ref

class MaterialImg(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    img = models.ImageField(default="{% static 'img/MaterialTrackerApp/generic_user.png' %}", blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.item.name


class Currency(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    dolar_value = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

