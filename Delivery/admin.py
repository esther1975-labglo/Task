from django.contrib import admin
from Delivery.models import Delivery
from grappelli.forms import GrappelliSortableHiddenMixin

class DeliveryAdmin(admin.ModelAdmin):
    list_display =('user', 'handled_DeliveryPartner', 
                 'order', 'delivery_location', 'status')
    search_fields = ('delivery_location', 'status')
    list_display_links = ( "order", )
    list_editable = ('user',)
    sortable_field_name = 'user'
    sortable_excludes = ('order', "status",)
    fieldsets = (
    ('D', {
        'classes': ('grp-collapse', 'grp-closed'),
        'fields' : ('user', 'order'),
    }),
)
    #list_filter = ('title', 'name')
    
admin.site.register(Delivery, DeliveryAdmin)

class MyInlineModelOptions(GrappelliSortableHiddenMixin, admin.TabularInline):
    fields = ("user",)


class MyCustomInlineModelOptions(GrappelliSortableHiddenMixin, admin.TabularInline):
    fields = ("user",)
    sortable_field_name = "order"
    