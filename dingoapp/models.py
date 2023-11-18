import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


# Create your models here.


class TagsModel(models.Model):
    tags = models.CharField(verbose_name='Tags', max_length=150)

    def __str__(self):
        return self.tags


class FoodModel(models.Model):
    title = models.CharField(verbose_name='Title', max_length=155)
    about = models.TextField(verbose_name='About')
    exsclusive = models.BooleanField(verbose_name='Exclusive', default=False)
    price = models.FloatField(verbose_name='Price',
                              validators=(
                                  MinValueValidator(0),
                                  MaxValueValidator(1000),
                              ))
    picture = models.ImageField(upload_to='food/', default='.static/img/logo.png')
    created = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Updated', auto_now=True)
    category = models.ManyToManyField('Category', verbose_name='Category')
    tag = models.ManyToManyField(TagsModel,verbose_name='Tags')

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField('Category name', max_length=150)
    created = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Updated', auto_now=True)

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ['created']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Chefs(models.Model):
    full_name = models.CharField(verbose_name='Full Name', max_length=150)
    level = models.ForeignKey('ChefLevel', on_delete=models.CASCADE)
    picture = models.ImageField(verbose_name='Picture', upload_to='chef/')
    fasebook = models.URLField(verbose_name='Fasebook', max_length=150, null=True, blank=True)
    instagram = models.URLField(verbose_name='Instagram', max_length=150, null=True, blank=True)
    x_tvit = models.URLField(verbose_name='X', max_length=150, null=True, blank=True)
    skype = models.URLField(verbose_name='Skype', max_length=150, null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chefs'


class ChefLevel(models.Model):
    ch_level = models.CharField(verbose_name='Chef Level', max_length=150)

    def __str__(self):
        return self.ch_level


def past_date_validator(value):
    if value < datetime.date.today():
        raise ValidationError('The date cannot be in the past.')

    return value


def past_time_validator(value):
    current_time = datetime.datetime.now()

    if value.hour < current_time.hour and current_time.date() == datetime.datetime.today():
        raise ValidationError('The time cannot be in the past for today.')

    return str(value.hour)


class BookingModel(models.Model):
    name = models.CharField(verbose_name='Name', max_length=150)
    email = models.EmailField(verbose_name='Email',max_length=150, blank=True, null=True)
    num_of_g = models.IntegerField(verbose_name='Number of guests')
    fone_number = models.CharField(verbose_name='Phone number', max_length=15)
    date = models.DateField(verbose_name='Date', validators=[past_date_validator])
    time = models.TimeField(verbose_name='Time', validators=[past_time_validator])
    note = models.TextField(verbose_name='Note', null=True, blank=True)


    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(verbose_name='Name',max_length=200)
    phone = models.CharField(verbose_name='Phone', max_length=40)
    subject = models.CharField(verbose_name='Subject', max_length=200)
    message = models.TextField()
    create = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse ('contact',)

    def __str__(self):
        return self.name