from django.db import models
from user.models import User
from django_google_maps import fields as map_fields
from django.db.models import JSONField
#class Restaurant(models.Model):
    #name = models.CharField(max_length=50)
    #address = models.TextField()
   # mobile_num  = models.IntegerField(null = True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)


class Restaurant(models.Model):
    OPEN = 1
    CLOSED = 2

    OPENING_STATUS = (
        (OPEN, 'open'),
        (CLOSED, 'closed'),
        )

    BREAKFAST = 1
    LAUNCH = 2
    DINNER = 3
    DELIVERY = 4
    CAFE = 5
    LUXURY = 6
    NIGHT = 7

    FEATURE_CHOICES = (
        (BREAKFAST, 'breakfast'),
        (LAUNCH, 'launch'),
        (DINNER, 'dinner'),
        (DELIVERY, 'delivery'),
        (CAFE, 'cafe'),
        (LUXURY, 'luxury dining'),
        (NIGHT, 'night life'),
        )

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


    TIMING_CHOICES = (
        (MONDAY, 'monday'),
        (TUESDAY, 'tuesday'),
        (WEDNESDAY, 'wednesday'),
        (THURSDAY, 'thursday'),
        (FRIDAY, 'friday'),
        (SATURDAY, 'saturday'),
        (SUNDAY, 'sunday'),
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    restaurant_name = models.CharField(max_length=150, db_index=True)
    image = models.ImageField(upload_to = 'img', null = True)
    slug = models.SlugField(max_length=150, db_index=True)
    address = map_fields.AddressField(max_length=200, null = True)
    geolocation = map_fields.GeoLocationField(max_length=100, null = True)
    city = models.CharField(max_length=100, null = True)
    restaurant_phone_number = models.PositiveIntegerField()
    restaurant_email = models.EmailField(blank=True, null=True)
    owner_email = models.EmailField(blank=True, null=True)
    opening_status = models.IntegerField(choices=OPENING_STATUS, default=OPEN)
    email = models.EmailField()
    features = models.IntegerField(choices = FEATURE_CHOICES, default = DINNER)
    timings = models.IntegerField(choices = TIMING_CHOICES, default = MONDAY)
    opening_from = models.TimeField()
    opening_to = models.TimeField()
    other_details = models.TextField()
    available = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True, null = True)
    updated = models.DateTimeField(auto_now = True)


    class Meta:
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'
        ordering = ('restaurant_name',)
        index_together = (('id','slug'),)


    def __str__(self):
        return self.restaurant_name

    # def get_absolute_url(self):
    #   return reverse('restaurant:restaurant_detail', args=[self.id, self.slug])



class Category(models.Model):
    name = models.CharField(max_length=120,db_index=True) #veg, non-veg
    slug = models.SlugField(max_length=120,db_index=True)

    class Meta:
        ordering=('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name



class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=120,db_index=True)
    slug = models.SlugField(max_length=120,db_index=True)
    image = models.ImageField(upload_to='products', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering=('name', )
        index_together = (('id', 'slug'), )
        verbose_name = 'menu'

    def __str__(self):
        return self.name



class From(models.Model):
    district = models.CharField(max_length = 100)
    geolocation = map_fields.GeoLocationField(max_length=100, null = True)

class To(models.Model):
    district = models.CharField(max_length = 100)
    geolocation = map_fields.GeoLocationField(max_length=100, null = True)

class distance(models.Model):
    from_location = models.ForeignKey(From, on_delete=models.CASCADE, blank=True, null=True)
    to_location = models.ForeignKey(To, on_delete=models.CASCADE, blank=True, null=True)

