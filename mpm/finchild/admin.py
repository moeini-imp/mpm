from django.contrib import admin
from .models import User,Events,CashFlow,UserAvatar,ShopEntity,BoughtItem,JobChallanges,Loan

# Register your models here.
admin.site.register(User)
admin.site.register(Events)
admin.site.register(CashFlow)
admin.site.register(UserAvatar)
admin.site.register(ShopEntity)
admin.site.register(BoughtItem)
admin.site.register(JobChallanges)
admin.site.register(Loan)
