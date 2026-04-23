from django.contrib import admin

# Import all required models
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


# Inline for Choice inside Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# Inline for Question inside Lesson
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 3


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Course Admin
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# Lesson Admin (attach questions here)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]


# Question Admin (attach choices here)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


# Register models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Instructor)
admin.site.register(Learner)
