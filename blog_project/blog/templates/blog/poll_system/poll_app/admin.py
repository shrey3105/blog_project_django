from django.contrib import admin
from poll_app.models import Question,Options
# Register your models here.
admin.site.register(Question)
admin.site.register(Options)
