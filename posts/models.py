from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=60,null=False)
    address = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return f"{self.id}, name: {self.name}, address: {self.address}"
    
author1= Author.objects.filter(id = 1)

class Post(models.Model):
    title = models.CharField(max_length=50,blank=True,null=True)
    description = models.TextField(max_length=70,blank=True,null=True)
    thumbnail = models.ImageField(upload_to ="media",null=True,blank=True)
    media = models.ImageField(upload_to ="media",null=True,blank=True)
    # time of writing (timestamps)
    content = models.TextField(max_length=7000,blank=True,null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name="writes")

    def __str__(self):
        return f"{self.id},title:{self.title}, {self.description}..."
    
class Category(models.Model):
    name = models.CharField(max_length=100,null=False)
    posts = models.ManyToManyField(Post,blank=True,related_name="post_categories")

    def __str__(self):
        return f"{self.id} name: {self.name}"
    
class SubCategory(models.Model):
    name = models.CharField(max_length=100,null=False)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="main_categories")
    
    def __str__(self):
        return f"{self.id}, sub-category: {self.name} "