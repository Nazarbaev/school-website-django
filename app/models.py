from django.db import models

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title
    class Meta:
            verbose_name = "Главная"      
            verbose_name_plural = "Главная"