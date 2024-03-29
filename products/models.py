import random , os
from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator

def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.split(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1,99999)
    name, ext = get_file_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )

class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)
    def active(self):
        return self.filter(active=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    def all(self):
        return self.get_queryset().active()
    def featured(self):
        qs = self.get_queryset().featured()
        return qs
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank = True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = ProductManager()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/products/{slug}/".format(slug=self.slug)

def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_reciever, sender=Product)