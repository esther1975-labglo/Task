from django.contrib import admin
from restaurant.models import Restaurant, Category, Menu, To, From, distance
import json
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class RestaurantAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     map_fields.AddressField: {
    #       'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    # }
    formfield_overrides = {
    map_fields.AddressField: { 'widget':
    map_widgets.GoogleMapsAddressWidget(attrs={
      'data-autocomplete-options': json.dumps({ 'types': ['geocode',
      'establishment'], 'componentRestrictions': {
                  'country': 'india'
              }
          })
      })
    },
}
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(distance)
admin.site.register(From)
admin.site.register(To)