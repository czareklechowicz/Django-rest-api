from django.db import models

from django.utils.translation import gettext_lazy as _


class Products(models.Model):
    prd_name = models.CharField(
        _("prd_name"),
        unique=True,
        max_length=50, 
        blank=False, 
        error_messages={
            "unique": _("A product with that name already exists."),
        },
    )
    prd_created = models.DateTimeField(auto_now_add=True)
    prd_warehouse = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.prd_name

    class Meta:
        ordering = ['prd_name']

class Warehouses(models.Model):
    whs_name = models.CharField(
        _("whs_name"),
        unique=True,
        max_length=50, 
        blank=False, 
        error_messages={
            "unique": _("A warehause with that name already exists."),
        },
    )
    whs_address = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.whs_name

    class Meta:
        ordering = ['whs_name']
