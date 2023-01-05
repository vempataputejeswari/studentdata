from django.contrib import admin

# Register your models here.
from .models import studenttable,classtable

admin.site.register(studenttable)
admin.site.register(classtable)

