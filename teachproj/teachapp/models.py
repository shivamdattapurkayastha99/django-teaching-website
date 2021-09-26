from django.db import models

# Create your models here.


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