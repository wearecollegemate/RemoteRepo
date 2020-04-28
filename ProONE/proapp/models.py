from django.db import models


class ProData(models.Model):
    name = models.CharField(max_length=30)
    rollno = models.BigIntegerField()
    regno = models.BigIntegerField(primary_key=True)
    email = models.EmailField(max_length=50)
    college = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    user = models.EmailField(max_length=50)
    pwd = models.CharField(max_length=20)
    image= models.ImageField(upload_to='images')
    date = models.DateField(max_length=100)

    def __str__(self):
        return self.name


class StoryData(models.Model):
    date = models.DateField(max_length=100)
    story = models.CharField(max_length=1200)
    upost = models.CharField(max_length=30)

    def __str__(self):
        return self.upost


class CmtData(models.Model):
    storydata = models.ForeignKey(StoryData, on_delete=models.DO_NOTHING)
    cmt = models.CharField(max_length=1200)
    cpost = models.CharField(max_length=30)
    cdate = models.DateField(max_length=100)

    def __str__(self):
        return self.cpost


class FeedData(models.Model):
    feed = models.CharField(max_length=1200)
    fpost = models.CharField(max_length=30)
    fdate = models.DateField(max_length=100)
    ans = models.CharField(max_length=1200,null=True)

    def __str__(self):
        return self.feed

# student=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
