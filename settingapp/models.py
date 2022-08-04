from django.db import models
from accounts.models import Madrasha
from django.template.defaultfilters import  slugify

# Create your models here.


class Status(models.Model):
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.is_active


class Department(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='departments')
    slug = models.SlugField(unique=True)
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT)

    def save(self, *ars, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*ars, **kwargs)

    def __str__(self):
        return self.name


class Designation(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='designations_status')
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True)

    def save(self, *ars, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*ars, **kwargs)

    def __str__(self):
        return self.name


class MadrashaClasses(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='department_classes')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='classes_status')
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True)

    def save(self, *ars, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*ars, **kwargs)

    def __str__(self):
        return self.name


class MadrashaGroup(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='department_madrasha_group')
    madrasha_class = models.ForeignKey(MadrashaClasses, on_delete=models.PROTECT, related_name='class_madrasha_group')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='madrasha_group_status')
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True)

    def save(self, *ars, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*ars, **kwargs)

    def __str__(self):
        return self.name


class Shift(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=True)
    shift_time = models.TimeField()  # look at this carefully
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='department_shifts')
    madrasha_class = models.ForeignKey(MadrashaClasses, on_delete=models.PROTECT, related_name='class_shifts')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='shift_status')
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True)

    def save(self, *ars, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*ars, **kwargs)

    def __str__(self):
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='department_books')
    madrasha_class = models.ForeignKey(MadrashaClasses, on_delete=models.PROTECT, related_name='class_books')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='books_status')
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True)

    def save(self, *ars, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*ars, **kwargs)

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='session_status')
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True)

    def save(self, *ars, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*ars, **kwargs)

    def __str__(self):
        return self.name


class Fees(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='department_fees')
    madrasha_class = models.ForeignKey(MadrashaClasses, on_delete=models.PROTECT, related_name='class_fees')
    amount = models.FloatField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='fees_status')
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True)

    def save(self, *ars, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*ars, **kwargs)

    def __str__(self):
        return self.name


class ExamRules(models.Model):
    text_input = models.TextField(max_length=2000)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='examrules_status')
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT)



