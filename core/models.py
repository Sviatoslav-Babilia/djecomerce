from pyexpat import model
from django.db import models
from django.conf import settings
# Create your models here.

CATEGORY_CHOICES =(
    ('S', 'Shirt'),
    ('SW', 'Sportwear'),
    ('OW', 'Outwear')
)
LABEL_CHOICES =(
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

class Item (models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    discaunt_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, default='S')
    lable = models.CharField(choices=LABEL_CHOICES, max_length=1, default='S')
    slug = models.SlugField()
    description = models.TextField(max_length=1000)


    def __str__(self):
        return self.title


class OrderItem (models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
