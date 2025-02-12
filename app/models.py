from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главная"


class Stats(models.Model):
    number_of_teachers = models.PositiveIntegerField()
    number_of_clubs = models.PositiveIntegerField()
    number_of_students = models.PositiveIntegerField()
    number_of_workers = models.PositiveIntegerField()
    background_image = models.ImageField()

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Члены команды"


class BlogCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория Новостей"
        verbose_name_plural = "Категории Новостей"


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    description = models.TextField()
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


class FAQ(models.Model):
    question = models.TextField(max_length=255)
    answer = models.TextField()

    class Meta:
        verbose_name = "Часто задаваемые вопросы"
        verbose_name_plural = "Часто задаваемые вопросы"


class Contact(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    open_days = models.CharField(max_length=255)
    open_hours = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
