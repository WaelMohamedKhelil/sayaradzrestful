from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from sayaradz import settings


class UserManager(BaseUserManager):

    def create_user(self, email, **kwargs):
        if not email:
            raise ValueError('Users must have an email')

        user = self.model(
            email = self.normalize_email(email)
        )
        if 'password' in kwargs.keys():
            password = kwargs['password']
            user.set_password(password)

        user.save(using= self._db)
        return user

    def create_superuser(self, email, password):

        user = self.create_user(email,password= password)
        user.is_admin = True
        user.save(using= self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique= True)
    is_admin = models.BooleanField(default= False)
    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class AutomobisteManger(UserManager):
    def create_automobiliste(self, email, password, name):
        automobiliste = super().create_user(email, password = password)
        automobiliste.name = name
        automobiliste.save(using= self._db)

class Automobiliste(User):
    name = models.CharField(max_length=255)
    objects = AutomobisteManger()







