from django.db import models

# Create your models here.
# MJ9PxRUEpRk

class Course(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    discount=models.IntegerField(default=0)
    active=models.BooleanField(default=False)
    thumbnail=models.ImageField(upload_to='files/thumbnail')
    date=models.DateTimeField(auto_now_add=True)
    resource=models.FileField(upload_to='files/resource')
    length=models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.name
class CourseProperty(models.Model):
    description=models.CharField(max_length=20,null=False)
    course=models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    class Meta:
        abstract=True

class Tag(CourseProperty):
    pass
class Prerequisite(CourseProperty):
    pass
class Learning(CourseProperty):
    pass
class Video(models.Model):
    title=models.CharField(max_length=30,null=False)
    course=models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    serial_number=models.IntegerField(default=0,null=False)
    video_id=models.CharField(max_length=20,null=False)
    is_preview=models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.title

    




