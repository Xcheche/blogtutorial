from django.contrib.auth.models import User  # Importing Django Default User Model
from django.db import models

"""
When ever we are creating a model or using foreignkey, it should be on top of the model.
"""


# Category Model1
class Category1(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Category1"


# Category Model2
class Category2(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Category2"


# Post Model
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    body = models.TextField(blank=True)
    image = models.FileField(
        upload_to="blog-post-image", default="blog-post-image/default.jpg"
    )
    first_category = models.ForeignKey(Category1, on_delete=models.CASCADE)
    second_category = models.ForeignKey(Category2, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    number_of_clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Posts"
