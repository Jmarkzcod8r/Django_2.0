from django.db import models

# Create your models here.
class Section(models.Model):
  name = models.CharField(max_length=255, blank=False, null=True,)

  def __str__(self):
    return self.name

class Product(models.Model):
  name = models.CharField(max_length=255, blank=False, null=True,)
  section = models.ForeignKey(Section,on_delete=models.CASCADE)

class Post(models.Model):
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()

class Testimony (models.Model):
    title=models.TextField( unique=True)

class Photo(models.Model):
    kid = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tag = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.kid

class Photo2(models.Model):
    kid = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tag = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.kid

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')
# class LinkedListNode(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     tags = models.CharField(max_length=200)
#     photo = models.ImageField(upload_to='photos/')
#     prev = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='previous')
#     next = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='next')

#     def __str__(self):
#         return self.title