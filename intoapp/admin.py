from django.contrib import admin

# Register your models here.
from .models import SaveTicketEvent

admin.site.register(SaveTicketEvent)