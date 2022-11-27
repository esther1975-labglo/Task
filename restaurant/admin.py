from django.contrib import admin
from restaurant.models import Restaurant, Category, Menu


from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class RestaurantAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }

admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Menu)