from django.db import models
from django import forms
# Create your models here.


# class MakerSpace(models.Model):
#     prompt = models.CharField(max_length=255)  #prompt

# class Member(models.model):
#     memberID 
#     password 
#     email = models.EmailField()


# class Member_space(models.Model):
#      picturebook_ID = models.CharField(max_length=255,null=False)
#      bookshielf_ID = models.CharField(max_length=255,null=False)

## 關鍵字種類
class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name

## 關鍵字資料庫
class PromptBase(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE
                                 ,related_name='promptbase')
    keyword = models.CharField(max_length=200, db_index=True)
    class Meta:
        ordering = ('category','keyword')

    def getCategory(self):
        return self.category

##繪本資料庫
class Picturebook(models.Model):
    # picturebook_ID = models.CharField(max_length=255,null=False,primary_key=True)
    # author = models.CharField(max_length=30,null=False)
    title = models.CharField(max_length=255,null=False)
    outline = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
   

class Image(models.Model):
    picturebook = models.ForeignKey(Picturebook,on_delete=models.CASCADE,default=None)
    # Image_ID = models.AutoField(primary_key=True)
    prompt = models.CharField(max_length=255)
    height = models.IntegerField(default=512)
    width = models.IntegerField(default=512)
    steps = models.IntegerField(default=50)
    seeds = models.IntegerField(default=222222222)
    scale = models.IntegerField(default=7)
    description = models.TextField()


    