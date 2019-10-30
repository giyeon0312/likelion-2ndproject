from django.db import models
from django.conf import settings
# Create your models here.

class Essay(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    body=models.TextField()

#사진을 업로드할 수 있는 클래스
class Album(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images")
    desc=models.CharField(max_length=100)

#what are the differences?
class Files(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    myfile=models.FileField(blank=False,null=False,upload_to="files")
    desc=models.CharField(max_length=100)