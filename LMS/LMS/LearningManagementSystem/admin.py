# Register your models here.
from django.contrib import admin
from .models import Members, Book, Issue, OverdueReturn

admin.site.register(Members)
admin.site.register(Book)
admin.site.register(Issue)
admin.site.register(OverdueReturn)
