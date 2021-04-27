from django.contrib import admin
from cart.models import AccessRecord, Brands, WebPage

# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Brands)
admin.site.register(WebPage)