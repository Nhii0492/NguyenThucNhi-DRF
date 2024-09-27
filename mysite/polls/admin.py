from django.contrib import admin
from .models import Choice, Question

admin.site.site_header = "Polls Administration"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Number of extra choices to display

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    ordering = ['-pub_date']  # Order questions by publication date, newest first

admin.site.register(Question, QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')
    list_filter = ('question',)  # Add filtering by question
    fieldsets = [
        (None, {'fields': ['question', 'choice_text', 'votes']}),
    ]

admin.site.register(Choice, ChoiceAdmin)
