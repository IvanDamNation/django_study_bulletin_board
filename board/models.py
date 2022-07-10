from django.db import models
from django.urls import reverse

from usersaccounts.models import User


class Files(models.Model):  # TODO Don't forget add MEDIA_URL and MEDIA_ROOT
    file = models.FileField()


# class Images(models.Model):  # TODO
#     url = models.ImageField()


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    title = models.CharField(max_length=128, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Photo')
    is_published = models.BooleanField(default=True, verbose_name='Published?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')
    # TODO
    # images = models.ManyToManyField(Images)
    # files = models.ManyToManyField(Files)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at', 'title']


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='News', related_name='comment_news')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Comment author')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Commentary date')
    text = models.TextField(verbose_name='Commentary text')
    accept = models.BooleanField(default=False, verbose_name='Accepted?')

    def get_absolute_url(self):
        return reverse('comment', kwargs={'comment_id': self.pk})

    def __str__(self):
        return '{}'.format(self.text)

    class Meta:
        verbose_name = 'Commentary'
        verbose_name_plural = 'Commentaries'
        ordering = ['-created_at', 'news']


class Category(models.Model):
    title = models.CharField(max_length=128, db_index=True, verbose_name='Category')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']
