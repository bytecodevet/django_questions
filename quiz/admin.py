from django.contrib import admin

from .models import Answer, Question


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question')

admin.site.register(Question)
admin.site.register(Answer, AnswerAdmin)