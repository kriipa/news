from datetime import datetime
from django.db import models

# Create your models here.

## for contact
class Contactus(models.Model):
    phone_num = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    ad_email = models.EmailField(max_length=300)

class Contact(models.Model):
    email = models.EmailField(max_length=300)
    number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
            return self.email


### video models
class Vid_cont(models.Model):
    name= models.TextField()
    heading = models.TextField(blank=True)
    image = models.ImageField(upload_to= 'media')
    desc = models.TextField()
    caption = models.CharField(max_length=600, blank=True)
    full_desc = models.TextField(blank=True)
    rank = models.IntegerField(default=0)
    

    def __str__(self):
            return self.name

### Adverisements
class Ad(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank= True)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    


### Category page
class Category(models.Model):
    name= models.TextField(blank=True)
    desc = models.TextField(blank=True)
    slug = models.CharField(max_length=500, unique= True, blank=True)

    def __str__(self):
            return self.name


LABELS = (('', 'default'), ('trending', 'trending'), ('videos', 'videos'), ('cat', 'cat'))

class News(models.Model):
    name = models.TextField(blank=True)
    heading = models.TextField()
    image = models.ImageField(upload_to= 'media')
    desc = models.TextField()
    long_desc = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    
    author_name = models.CharField(max_length=300, blank=True)
    author_image = models.ImageField(upload_to= 'media', blank=True)
    labels = models.CharField(choices=LABELS, max_length=50, blank=True)

    def __str__(self):
            return self.name

### profile page
class Profile(models.Model):
    name = models.CharField(max_length= 500)
    email = models.EmailField(max_length= 500)
    Description = models.TextField()
    picture = models.ImageField(upload_to= 'pictures')

    def __str__(self):
        return self.name

### home page

class Customer(models.Model):
    username=models.CharField(max_length= 500)
    email = models.EmailField(max_length= 500)
    password=models.CharField(max_length= 500)

    def __str__(self):
        return self.username