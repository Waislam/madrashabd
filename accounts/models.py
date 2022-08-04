from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

# =============================== Address ================================


class Division(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return self.name


class Thana(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='thanas')

    def __str__(self):
        return self.name


class PostOffice(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='postoffices')

    def __str__(self):
        return self.name


class PostCode(models.Model):
    name = models.CharField(max_length=100)
    # district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='postcodes')
    post_office = models.ForeignKey(PostOffice, on_delete=models.CASCADE, related_name='postcodess', null=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, blank=True, null=True, related_name='divisions')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True, related_name='districts')
    thana = models.ForeignKey(Thana, on_delete=models.SET_NULL, blank=True, null=True, related_name='thanas')
    post_office = models.ForeignKey(PostOffice, on_delete=models.SET_NULL, blank=True, null=True, related_name='post_offices')
    post_code = models.ForeignKey(PostCode, on_delete=models.SET_NULL, blank=True, null=True, related_name='post_cods')
    address_info = models.TextField()

    def __str__(self):
        return self.division.name

# ============================== 3. Role Model ==========================


class Role(models.Model):
    role_name = models.CharField(max_length=200, unique=True)


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
        user = self.create_user(phone, password, is_staff=True, is_admin=True, **extra_fields)
        return user

    def create_staffuser(self, phone, password=None, **extra_fields):
        user = self.create_user(phone, password, is_staff=True, **extra_fields)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField( unique=True, max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)  # need to modify this one
    email = models.EmailField(unique=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name='user_roles', null=True, blank=True)
    avatar = models.ImageField(upload_to='user-image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = OurUserManager()

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

# ============================= Madrasha object =================


MADRASHA_STATUS = (
    ('active', 'Active'),
    ('inactive', 'Inactive')
)


class Madrasha(models.Model):
    name = models.CharField(max_length=255)
    madrasha_id = models.CharField(unique=True, max_length=30, blank=True)
    madrasha_address = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name='madrasha_address', null=True)
    madrasha_logo = models.ImageField(upload_to='madrasha/logo/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)
    active_status = models.CharField(max_length=10, default='Inactive', choices=MADRASHA_STATUS)

    def generate_madrasha_id(self):
        starting = 100
        last_madrasha = self.objects.last()
        last_madrasha_id = int(last_madrasha.id)
        if last_madrasha:
            new_id = last_madrasha_id + 1
        else:
            new_id = starting + 1
        generated_id = str(new_id)
        return generated_id

    def save(self, *args, **kwargs):
        if not self.madrasha_id:
            self.madrasha_id = self.generate_madrasha_id()
        super(Madrasha, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class MadrashaUserListing(models.Model):
    user = models.ForeignKey(CustomUser, related_name='users', on_delete=models.PROTECT)
    madrasha = models.ForeignKey(Madrasha, related_name='madrashas', on_delete=models.PROTECT)