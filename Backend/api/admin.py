from django.contrib import admin
from .models import Attendee, Exhibitor, Volunteer, Contact
# Register your models here.

admin.site.register(Attendee)
admin.site.register(Exhibitor)
admin.site.register(Volunteer)
admin.site.register(Contact)
