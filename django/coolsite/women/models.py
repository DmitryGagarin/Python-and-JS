from django.db import models
from django.urls import reverse

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})
    
    class Meta:
        verbose_name = "Famous Women"
        verbose_name_plural = "Famous Women"
        ordering = ['time_created','title']
    
    
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Category')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_id": self.pk})
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['id']
    
    

    

