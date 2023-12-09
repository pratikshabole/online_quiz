from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(QuizCategory)
admin.site.register(QuizQuestion)
admin.site.register(SubmitAnswer)