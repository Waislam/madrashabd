from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class OurUserManager(BaseUserManager):
    def create_user(self, phone, password=None, is_staff=False, is_active=True, **extra_fields):
        if not phone:
            raise ValueError('Phone number must required')
        if not password:
            raise ValueError('Password is required')

        # phone = self.normalize_email(phone)
        phone = OurUserManager.normalize_email(phone)
        user = self.model(phone=phone, is_staff=is_staff, is_active=is_active, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        user = self.create_user(phone, password, is_staff=True, is_admin=True, **extra_fields)  # is_superuser should use no need?


    def create_staffuser(self):
        pass


class CustomUser(AbstractBaseUser):
    username = models.CharField( unique=True, max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)  # need to modify this one
    email = models.EmailField(unique=True, blank=True)
    avatar = models.ImageField(upload_to='user-image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
