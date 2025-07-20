from django.db import models
from django.utils import timezone


class Home(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главная"

    def __str__(self):
        return f"Image {self.id}"



class GalleryCategory(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория галереи"
        verbose_name_plural = "Категория галереи"


class Gallery(models.Model):

    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name='gallery')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"

    def __str__(self):
        return f"Image {self.id}"


class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')

class Stats(models.Model):
    number_of_teachers = models.PositiveIntegerField()
    number_of_clubs = models.PositiveIntegerField()
    number_of_students = models.PositiveIntegerField()
    number_of_workers = models.PositiveIntegerField()


    class Meta:
        verbose_name = "Статистика"
        verbose_name_plural = "Статистика"


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Члены команды"


class BlogCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория Новостей"
        verbose_name_plural = "Категории Новостей"


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    # project_url = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


class BlogImages(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='images/')

class FAQ(models.Model):
    question = models.TextField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Часто задаваемые вопросы"
        verbose_name_plural = "Часто задаваемые вопросы"



