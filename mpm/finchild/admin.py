from django.contrib import admin
from .models import User,Events,CashFlow,UserAvatar,ShopEntity

# Register your models here.
admin.site.register(User)
admin.site.register(Events)
admin.site.register(CashFlow)
admin.site.register(UserAvatar)
admin.site.register(ShopEntity)