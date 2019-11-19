from django.contrib import admin
from gram.models import UserProfile,Location,\
Product,Store, Gram

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Location)
admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Gram)

