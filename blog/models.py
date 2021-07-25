from django.db import models
from django.urls import reverse
from django.contrib import admin
from account.models import User
from django.db.models.fields import related
from django.utils.html import format_html
from django.utils import timezone
from extensions.utils import converter
# Create your models here.

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class Category(models.Model):
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name="children", verbose_name='زیر دسته')
    title = models.CharField(max_length = 150, verbose_name='عنوان')
    slug = models.SlugField(max_length = 50, unique=True, verbose_name='آدرس')
    status = models.BooleanField(default=True, verbose_name='وضعیت')
    position = models.IntegerField(verbose_name='آیا نمایش داده شود؟')
    
    objects = CategoryManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها '
        ordering = ["parent_id", "position"]


class Article(models.Model):
    STATUS_CHOICES =(
        ('d', 'Darft'),
        ('p', 'Published'),
        ('i', 'Investigation'),
        ('b', 'Back'),
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles')
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50, unique=True)
    category = models.ManyToManyField(Category, related_name='articles')
    body = models.TextField()
    snippet = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_special = models.BooleanField(default=False, verbose_name='Special')
    status = models.CharField(max_length = 1, choices=STATUS_CHOICES)
    
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("account:home")

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish']

    @admin.action(description='دسته بندی ها')   
    def category_to_str(self):
        return ", " .join([ category.title for category in self.category.active()])

    @admin.action(description='عکس')
    def image_tag(self):
        return format_html(f"<img width=110 height=70 src='{self.image.url}' style='border-radius: 14px;' alt="">")

    # def jpublish(self):
    #     return converter(self.publish)

    

        
    objects = ArticleManager()

