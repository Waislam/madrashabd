from django.db import models
from accounts.models import Madrasha
from django.template.defaultfilters import slugify


class Department(models.Model):
    name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT, related_name='madrasha_departments')

    def save(self, *ars, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + self.madrasha.name)
        return super().save(*ars, **kwargs)

    class Meta:
        unique_together = [['name', 'madrasha']]
        ordering = ['name']

    def __str__(self):
        return self.name + " " + self.madrasha.name


class Designation(models.Model):
    name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT, related_name='madrasha_designations')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_designations', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *ars, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + self.madrasha.name)
        return super().save(*ars, **kwargs)

    class Meta:
        unique_together = [['name', 'madrasha']]
        ordering = ['name']

    def __str__(self):
        return self.name


class MadrashaClasses(models.Model):
    name = models.CharField(max_length=150, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='department_classes')
    is_active = models.BooleanField(default=True)
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT, related_name='madrasha_classes')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *ars, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + self.madrasha.name)
        return super().save(*ars, **kwargs)

    class Meta:
        unique_together = [['name', 'madrasha']]
        ordering = ['name']

    def __str__(self):
        return self.name


class MadrashaGroup(models.Model):
    name = models.CharField(max_length=150, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='department_madrasha_group')
    madrasha_class = models.ForeignKey(MadrashaClasses, on_delete=models.PROTECT, related_name='class_madrasha_group')
    is_active = models.BooleanField(default=True)
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT, related_name='madrasha_groups')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *ars, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + self.madrasha.name)
        return super().save(*ars, **kwargs)

    class Meta:
        unique_together = [['name', 'madrasha']]
        ordering = ['name']

    def __str__(self):
        return self.name


class Shift(models.Model):
    name = models.CharField(max_length=150)
    shift_time = models.TimeField()  # look at this carefully
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='department_shifts')
    madrasha_class = models.ForeignKey(MadrashaClasses, on_delete=models.PROTECT, related_name='class_shifts')
    is_active = models.BooleanField(default=True)
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT, related_name='madrasha_shift')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *ars, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + self.madrasha.name)
        return super().save(*ars, **kwargs)

    class Meta:
        unique_together = [['name', 'madrasha']]
        ordering = ['name']

    def __str__(self):
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=150, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='department_books')
    madrasha_class = models.ForeignKey(MadrashaClasses, on_delete=models.PROTECT, related_name='class_books')
    is_active = models.BooleanField(default=True)
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT, related_name='madrasha_books')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *ars, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + self.madrasha.name)
        return super().save(*ars, **kwargs)

    class Meta:
        unique_together = [['name', 'madrasha']]
        ordering = ['name']

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=150, blank=True)
    actual_year = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT, related_name='madrasha_sessions')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *ars, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + self.madrasha.name)
        return super().save(*ars, **kwargs)

    class Meta:
        unique_together = [['name', 'madrasha']]
        ordering = ['name']

    def __str__(self):
        return self.name


class Fees(models.Model):
    name = models.CharField(max_length=150, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='department_fees')
    madrasha_class = models.ForeignKey(MadrashaClasses, on_delete=models.PROTECT, related_name='class_fees')
    amount = models.FloatField()
    is_active = models.BooleanField(default=True)
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT, related_name='madrasha_fees')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *ars, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + self.madrasha.name)
        return super().save(*ars, **kwargs)

    class Meta:
        unique_together = [['name', 'madrasha']]
        ordering = ['name']

    def __str__(self):
        return self.name


class ExamRules(models.Model):
    text_input = models.TextField(max_length=2000)
    is_active = models.BooleanField(default=True)
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT, related_name='madrasha_exam_rules')

    def __str__(self):
        return self.text_input



