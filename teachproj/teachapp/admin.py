from django.contrib import admin
from . models import *
# Register your models here.
class TagAdmin(admin.TabularInline):
    model=Tag
class LearningAdmin(admin.TabularInline):
    model=Learning
class VideoAdmin(admin.TabularInline):
    model=Video
class PrerequisiteAdmin(admin.TabularInline):
    model=Prerequisite
class CourseAdmin(admin.ModelAdmin):
    inlines=[TagAdmin,LearningAdmin,PrerequisiteAdmin,VideoAdmin]


admin.site.register(Course,CourseAdmin)

admin.site.register(Video)