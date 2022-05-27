from datetime import date

from django.conf import settings
from django.db import models

from django.core.validators import MinLengthValidator
# from users.models import User
from django.utils.datetime_safe import datetime
from users.models import User



class Ad(models.Model):
    title = models.CharField(max_length=50, null=False, validators=[MinLengthValidator(5)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(validators=[MinLengthValidator(0)])
    description = models.TextField(max_length=1000, null=True, blank=True)
    # comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='logos/', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявления"


class Comment(models.Model):
    text = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=10, validators=[MinLengthValidator(5)], unique=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    ad = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


    #
    # def __str__(self):
    #     return self.name
