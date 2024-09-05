from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Menu(MPTTModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    position = models.IntegerField(blank=True, null=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    status = models.BooleanField(default=True)


    class MPTTMeta:
        order_insertion_by = ["title"]
        
    class Meta:
        db_table = 'menu'
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    def __str__(self):
        return self.title
    


class Page(models.Model):
    title =  models.CharField(max_length=500, null=True, blank=True)
    text =  RichTextUploadingField()
    url  = models.CharField(max_length=200)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'page'
        verbose_name = 'Yangi Sahifa'
        verbose_name_plural = 'Yangi Sahifa'
    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'pk': self.pk})




class File(models.Model):
    name  =  models.CharField(max_length=300)
    file  =  models.FileField(upload_to="Image/Fayl")

    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = 'file'
        verbose_name = 'Fayl'
        verbose_name_plural = 'Fayl'




class Partners(models.Model):
    title  =  models.CharField(max_length=300)
    image =  models.ImageField(upload_to="Image/Partners")

    def __str__(self) -> str:
        return self.title
    class Meta:
        db_table = 'partners'
        verbose_name = 'Hamkorlar'
        verbose_name_plural = 'Hamkorlar'