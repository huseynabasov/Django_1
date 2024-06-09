from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Basliq")
    content = RichTextUploadingField(verbose_name="Mezmun")
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to="Article Image",blank=True, null=True, verbose_name="Sekil")

    def __str__(self):
        return f"{self.title} | {self.author}" 
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Meqale", related_name="comments")
    comment_author = models.CharField(max_length=75, verbose_name="Ad")
    comment_content = models.TextField(verbose_name="Comment mezmunu")
    comment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.comment_author}"