from django.contrib import admin
from .models import Library, Book, Booktenant
# Register your models here.

admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Booktenant)