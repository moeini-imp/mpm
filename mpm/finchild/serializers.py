from rest_framework import serializers
from .models import User,Events,CashFlow,UserAvatar,ShopEntity,JobChallanges

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields="__all__"


class CashFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model=CashFlow
        fields="__all__"


class UserAvatarSerializers(serializers.ModelSerializer):
    class Meta:
        model=UserAvatar
        fields="__all__"


class ShopEntitySerializers(serializers.ModelSerializer):
    class Meta:
        model=ShopEntity
        fields="__all__"


class JobChallangeSerializers(serializers.ModelSerializer):
    class Meta:
        model=JobChallanges
        fields='__all__'