from django.contrib import admin

# Register your models here.
from Notes.notes_app.models import Note, Profile

admin.site.register(Note)
admin.site.register(Profile)
