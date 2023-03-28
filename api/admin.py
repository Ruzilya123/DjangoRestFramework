from django.contrib import admin
from .models import User, Country, Cart, Tour, Excursion, PersonalCabinet

admin.site.register(User)
admin.site.register(Country)
admin.site.register(Cart)
admin.site.register(Tour)
admin.site.register(Excursion)
admin.site.register(PersonalCabinet)

