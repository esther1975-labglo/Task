from django.contrib import admin
from DeliveryPartner.models import (
    profile,
    service,
    task
)
admin.site.register(profile)
admin.site.register(service)
admin.site.register(task)


