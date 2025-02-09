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


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()


class Blog(models.Model):
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.title


class BlogDetail(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="details")
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    content = models.TextField()

    def __str__(self):
        return self.title


class Achievement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()


class Contact(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    open_days = models.CharField(max_length=255)
    open_hours = models.CharField(max_length=255)
