from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Wear(models.Model):
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    character = models.TextField()
    UZ = "so'm"
    RU = "rubl"
    USA = "$"
    the_price = (
        (UZ, "so'm"),
        (RU, "rubl"),
        (USA, "$"),
    )
    price_type = models.CharField(max_length=10, choices=the_price, default="so'm")
    price = models.IntegerField()
    image = models.ImageField(upload_to='media')


    def __str__(self):
        return self.name


class Buy(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=30)
    product = models.ForeignKey(Wear, on_delete=models.CASCADE, null=True)
    ALL_SIZE = (
        ("M", "M"),
        ("L", "L"),
        ("S", "S"),
        ("X", "X"),
        ("XXL", "XXL"),
    )
    size = models.CharField(max_length=100, choices=ALL_SIZE)
    ALL_VALUES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "4"),
        ("5", "5"),
    )
    how = models.CharField(max_length=100, choices=ALL_VALUES)
    map = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Reklame(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media')


    def __str__(self):
        return self.title



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name