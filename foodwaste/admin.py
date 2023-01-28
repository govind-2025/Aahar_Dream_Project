from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(State)
admin.site.register(City)
admin.site.register(Contact)
admin.site.register(Donor)
admin.site.register(Food)
admin.site.register(Foodrequests)

