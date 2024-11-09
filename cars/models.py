from django.db import models
from django.utils.text import slugify


# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class car(models.Model):
    Proname = models.CharField(max_length=50)
    yearofpp = models.DateField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    stok = models.IntegerField(validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to="posts", null=True)
    discr = models.TextField(default='')
    sped = models.IntegerField(validators=[MaxValueValidator(250)], default=0)
    slug = models.SlugField(unique=True, db_index=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Proname)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.Proname
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

class Producer(models.Model):
    name = models.CharField(max_length=20)
    carsp = models.ForeignKey(car, verbose_name="Car", on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name