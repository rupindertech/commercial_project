from django.db import models
from django.utils.timezone import now
from tinymce import models as tmodel
from django.template.defaultfilters import slugify

# Create your models here.
CATEGORY_CHOICES=(
    ('CR','Card'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('PN','Paneer'),
)

class Product(models.Model):
    title=models.Charfield(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    composition=models.TextField(default='')
    prodapp=models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image=models.ImageField(upload_to='product')
    def __str__(self):
        return self.title