from django.contrib import admin
from .models import login,personal_data_user,publications

admin.site.register(login)
admin.site.register(personal_data_user)
admin.site.register(publications)

# Register your models here.
