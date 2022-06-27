from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=128, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Photo')
    is_published = models.BooleanField(default=True, verbose_name='Published?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')

    # def get_absolute_url(self):
    #     pass

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at', 'title']


class Category(models.Model):
    title = models.CharField(max_length=128, db_index=True, verbose_name='Category')

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']
