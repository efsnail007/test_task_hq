from django.db import models


class Admin(models.Model):
    name = models.CharField(max_length=50, unique=True)


class User(models.Model):
    name = models.CharField(max_length=50)


class Lesson(models.Model):
    name = models.CharField(max_length=200, unique=True)
    link_video = models.URLField(unique=True)
    duration = models.PositiveBigIntegerField()


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    proprietor_name = models.ForeignKey(Admin, on_delete=models.PROTECT)
    lessons = models.ManyToManyField(Lesson)


class Account(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True
    )
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    products = models.ManyToManyField(Product)


class Viewing(models.Model):
    SEEN = "se"
    UNSEEN = "uns"
    STATUS_CHOICES = [
        (SEEN, "Seen"),
        (UNSEEN, "Unseen"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewing_time = models.PositiveBigIntegerField(default=0)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=UNSEEN
    )
    date_last_viewing = models.DateTimeField(auto_now=True)
