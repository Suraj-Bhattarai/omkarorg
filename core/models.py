from django.db import models
import random
import os
from django.db.models.signals import pre_save
from django.urls import reverse
from django.template.defaultfilters import slugify
from omkarorg.utils import unique_slug_generator
from ckeditor.fields import RichTextField
from django.conf import settings


class ProductManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
 

class Category(models.Model):
    name = models.CharField(max_length=100, default ='')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={'slug': self.slug})


class SubCategory(models.Model):
    category = models.ForeignKey('Category', related_name='subcategory',
                                 on_delete=models.CASCADE)
    name     = models.CharField(max_length=50)
    slug     = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'SubCategory'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ecomapp:subcat-listing", kwargs={'slug': self.slug})


TYPE = (
    ('IT', 'IT Product'),
    ('POS', 'POS Product'),
)


class Product(models.Model):
    # Basic Information
    title       = models.CharField(max_length=120)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default ='')
    brand       = models.CharField(max_length=120, blank= True)
    
    #Description
    features      = RichTextField(blank=True, null=True)
    specification = RichTextField(blank=True, null=True)
    description   = RichTextField(blank=True, null=True)

    #Price and Colors
    price    = models.BigIntegerField(default='')
    color    = models.CharField(max_length=100, blank= True)
    model_no = models.CharField(max_length=100, blank= True)

    product_brocher = models.CharField(max_length=300, blank= True)
    easymart_link   = models.CharField(max_length=300, blank= True)

    #Misc
    published = models.DateTimeField(auto_now=True)
    slug      = models.SlugField(unique=True, blank=True)
    best_seller = models.BooleanField(default=False)
    
    #warrenty
    warrenty_type = models.CharField(max_length=200, null=True, blank=True)
    warrenty_period = models.CharField(max_length=120, null=True, blank=True)

    #cloudnary
    cloudName = models.CharField(max_length=200, null=True, blank=True)
    photo_tag = models.CharField(max_length=200, null=True, blank=True)
    video_tag = models.CharField(max_length=200, null=True, blank=True)

    image_url = models.CharField(max_length=500, null=True, blank=True)

    product_type = models.CharField(choices=TYPE, max_length=128, default='')
     

    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug":self.slug})


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance=instance)
    
pre_save.connect(product_pre_save_receiver, sender=Product)


STATUS = (
    ('RO', 'Repair Ongoing'),
    ('RF', 'Repair Finished'),
)


class Service(models.Model):
    customer_name = models.CharField(max_length=200)
    tracking_code = models.CharField(max_length=200)
    product_name = models.CharField(max_length=500)
    price  = models.BigIntegerField(default='')
    estimate_time = models.DateTimeField()
    slug   = models.SlugField(unique=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=128, default='')
    note = models.CharField(max_length=500)

    published = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tracking_code)
        return super().save(*args, **kwargs)
     
    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return reverse("addservice", kwargs={"slug":self.slug})

