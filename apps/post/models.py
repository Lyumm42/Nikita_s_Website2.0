from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField(max_length=100)
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="post",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"