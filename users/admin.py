from django.contrib import admin
from .models import Contact,Profile
# Register your models here.
admin.site.site_header='FUNSSIGNMENT-ADMIN'
admin.site.site_title='FUNSSIGNMENT ADMIN'
admin.site.index_title='FUNSSIGNMENT-STAFF'

admin.site.register(Contact)
admin.site.register(Profile)