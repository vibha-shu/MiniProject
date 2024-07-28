from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=20)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.email

class category(models.Model):
    cname=models.CharField(max_length=40)
    cpic=models.ImageField(upload_to='static/category/',default="")
    cdate=models.DateField()

    def __str__(self):
        return self.cname


class registration(models.Model):
    name=models.CharField(max_length=128)
    mobile=models.CharField(max_length=20)
    email=models.EmailField(max_length=80,primary_key=True)
    passwd=models.CharField(max_length=100)
    ppic=models.ImageField(upload_to='static/profile/',default="")
    address=models.TextField(max_length=200)

class recuiters(models.Model):
    rname=models.CharField(max_length=200)
    rpic=models.ImageField(upload_to='static/recuiters/',default="")
    rdate=models.DateField()

class gallery(models.Model):
    pdes=models.CharField(max_length=200)
    gpic=models.ImageField(upload_to='static/gallery/',default="")
    gdate=models.DateField()

class courses(models.Model):
    cname=models.CharField(max_length=200)
    cpic=models.ImageField(upload_to='static/courses/',default="")
    cfee=models.CharField(max_length=100)
    cdate=models.DateField()
    def __str__(self):
        return self.cname


class placements(models.Model):
    name=models.CharField(max_length=100)
    pcourse=models.ForeignKey(courses,on_delete=models.CASCADE)
    branch=models.CharField(max_length=80)
    cmpname=models.CharField(max_length=80)
    cmplogo=models.ImageField(upload_to='static/placements/',default="")
    city=models.CharField(max_length=100)
    pyear=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    stupic=models.ImageField(upload_to='static/studentpic/',default="")
    pdate=models.DateField()

