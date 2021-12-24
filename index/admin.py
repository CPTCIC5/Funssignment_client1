from django.contrib import admin
from .models import QuizPost,Question,Result

admin.site.register(QuizPost)
admin.site.register(Question)
admin.site.register(Result)