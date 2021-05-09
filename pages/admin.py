from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'category')
    list_filter = ('uploaded_at', 'category')

admin.site.site_header = 'Εργοχειράς Σελίδα Διαχείρησης'
admin.site.register(Image, ImageAdmin)
admin.site.unregister(Group)
