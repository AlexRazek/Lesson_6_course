from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
# from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
from users.managers import UserManager


class UserRoles:
    # TODO закончите enum-класс для пользователя
    pass


class User(AbstractBaseUser):
    USER = "user"
    ADMIN = "admin"
    ROLES = [
        ("user", "Пользователь"),
        ("admin", "Администратор"),
    ]

    first_name = models.CharField(max_length=20, null=True, blank=True, verbose_name="Имя пользователя")
    last_name = models.CharField(max_length=25, null=True, blank=True, verbose_name="Фамилия пользователя")
    phone = PhoneNumberField(verbose_name="Телефон пользователя", null=True)
    email = models.EmailField(max_length=120, unique=True, null=True, verbose_name="Электронный адрес пользователя")
    role = models.CharField(max_length=10, choices=ROLES, default="user")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    # для корректной работы нам также необходимо
    # переопределить менеджер модели пользователя

    # Необходимые параметры для корректной работе Django
    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def is_active(self):
        return self.is_active

    # также для работы модели пользователя должен быть переопределен
    # менеджер объектов
    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == 'admin'                #UserRoles.ADMIN  #

    @property
    def is_user(self):
        return self.role == 'user'                  #UserRoles.USER
