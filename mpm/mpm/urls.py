from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from finchild.views import (
    EventsView, UserView, CashFlowView, UserAvatarView, AllAvatarsView,
    ShopView, ShopImagesView, ShopPurchaseView, EventUpdateMoneyView,JobChallangesImageView
    ,JobChallangeView
)

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('events/', EventsView.as_view(), name='events-list'),
    path('user/', UserView.as_view(), name='user-create'),
    path('user/<int:id>', UserView.as_view(), name='user-fetch'),
    path('events/<int:id>', EventsView.as_view(), name='events-detail'),
    path('cashflow/', CashFlowView.as_view(), name='cashflow-list'),
    path('cashflow/<int:id>', CashFlowView.as_view(), name='cashflow-detail'),
    path('avatars/', AllAvatarsView.as_view(), name='avatars-list'),
    path("avatars/<str:slug>", UserAvatarView.as_view(), name='avatar-detail'),
    path("shop/", ShopView.as_view(), name='shop-list'),
    path("shop/<int:id>", ShopView.as_view(), name='shop-detail'),
    path("shopEntityImage/<str:slug>", ShopImagesView.as_view(), name='shop-image-detail'),
    path("shop/purchase", ShopPurchaseView.as_view(), name='shop-purchase'),
    path("events/update-money/", EventUpdateMoneyView.as_view(), name='event-update-money'),
    path("JobChallanges/",JobChallangeView.as_view(),name="jobs_lists"),
    path("JobChallanges/<int:id>",JobChallangeView.as_view(),name='job_details'),
    path("JobChallangesImage/<str:slug>",JobChallangesImageView.as_view(),name='job_details')


]
