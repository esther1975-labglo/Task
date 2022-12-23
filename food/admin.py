from django.contrib import admin
from food.models import FoodCategory, Food
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

admin.site.register(FoodCategory)
admin.site.register(Food)


# class FoodCategoryInline(SortableInlineAdminMixin, admin.TabularInline):
#     model = FoodCategory
#     extra = 0

# @admin.register(Food)
# class JobAdmin(SortableAdminMixin, admin.ModelAdmin):
#     list_display = ['id', 'name', 'phone_number', 'image',
#                   'joining_date']
#     list_filter = ['name']
#     search_fields = ['name','id']
   
#     # fieldsets = [
#     #     (None, {'fields': ['requestedby','account','requestdate','requireddate','noofsides','noofcopies'] }),
#     #     ('Requirements', {'fields': ['color','sided','paper','finishing']}),
#     #     ('Additional Information', {'fields': ['additionalinfo']}),
#     # ]
#     # inlines = [ResourceInline]