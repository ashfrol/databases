from django.db import models


class Phone(models.Model):

    id = models.IntegerField(
        primary_key=True
    )
    name = models.TextField(
        blank=False
    )
    price = models.FloatField(
        blank=True,
        default='-'
    )
    image = models.ImageField(
        blank=True
    )
    release_date = models.DateField(
        blank=True,
        default='-'
    )
    lte_exists = models.BooleanField(
        blank=True,
        null=True,
        default='NULL'
    )
    slug = models.CharField(
        max_length=80
    )
