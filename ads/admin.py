from django.contrib import admin

from ads.models import User, Category, Ad
from users.models import Location


admin.site.register(Location)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Ad)

