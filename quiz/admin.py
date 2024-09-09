from django.contrib import admin

from .models import Answer, Question, Quiz, QuizTaker, Response, categories

# Register your models here.
admin.site.register(categories)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuizTaker)
admin.site.register(Response)
