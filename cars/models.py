from django.db import models
from django.utils.text import slugify


# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Producer(models.Model):
    name = models.CharField(max_length=20)
    logo = models.ImageField(upload_to="posts", null=True)

    def __str__(self):
        return self.name

class car(models.Model):
    Proname = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    yearofpp = models.DateField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    stok = models.IntegerField(validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to="posts", null=True)
    discr = models.TextField(default='')
    sped = models.IntegerField(validators=[MaxValueValidator(250)], default=0)
    slug = models.SlugField(unique=True, db_index=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='cars', null=True, blank=True, default=None)  # ForeignKey placed here

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Proname)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Proname

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
