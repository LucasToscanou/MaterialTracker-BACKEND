from django.contrib import admin
from MaterialTrackerApp.models import *
 

# Register your models here.
admin.site.register(Project)
admin.site.register(Material)
admin.site.register(UserProfile)
admin.site.register(Location)
admin.site.register(MaterialImg)
admin.site.register(Currency)