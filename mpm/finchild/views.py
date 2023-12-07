from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse

from .models import User, Events, CashFlow, UserAvatar, ShopEntity, BoughtItem,JobChallanges
from .serializers import (
    UserSerializer, EventSerializer, CashFlowSerializer,
    UserAvatarSerializers, ShopEntitySerializers,JobChallangeSerializers
)

class EventsView(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        if self.request.method == "GET" and "id" in self.kwargs:
            return Events.objects.filter(id=self.kwargs['id'])
        else:
            return Events.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class UserView(mixins.RetrieveModelMixin, generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset=User.objects.all()
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        if "id" in self.kwargs:
            user = get_object_or_404(User, id=self.kwargs['id'])
            # perform any actions you need with the user instance
            return Response(UserSerializer(user).data)
        else:
            return User.objects.all()
    
    

class CashFlowView(generics.ListCreateAPIView):
    serializer_class = CashFlowSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        if self.request.method == "GET" and "id" in self.kwargs:
            return CashFlow.objects.filter(id=self.kwargs['id'])
        else:
            return CashFlow.objects.all()

class UserAvatarView(generics.ListCreateAPIView, APIView):
    serializer_class = UserAvatarSerializers

    def perform_create(self, serializer):
        serializer.save()

    def get(self, request, *args, **kwargs):
        if "slug" in self.kwargs:
            user_profile = get_object_or_404(UserAvatar, avatar__endswith=self.kwargs['slug'])
            avatar_path = user_profile.avatar.path
            return FileResponse(open(avatar_path, 'rb'), content_type='image/jpeg')

class AllAvatarsView(generics.ListAPIView):
    serializer_class = UserAvatarSerializers
    queryset = UserAvatar.objects.all()

class ShopView(generics.ListCreateAPIView):
    serializer_class = ShopEntitySerializers

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        if self.request.method == "GET" and "id" in self.kwargs:
            return ShopEntity.objects.filter(id=self.kwargs['id'])
        else:
            return ShopEntity.objects.all()

class ShopImagesView(APIView):
    serializer_class = ShopEntitySerializers

    def get(self, request, *args, **kwargs):
        if "slug" in self.kwargs:
            entity_image = get_object_or_404(ShopEntity, image__endswith=self.kwargs['slug'])
            image_path = entity_image.image.path
            return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')

class ShopPurchaseView(APIView):

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        item_id = request.data.get('item_id')

        # Check if both user_id and item_id are provided in the request
        if not user_id or not item_id:
            return Response('Both user_id and item_id are required for the purchase.', status=400)

        user = get_object_or_404(User, id=user_id)
        item = get_object_or_404(ShopEntity, id=item_id)

        if user.buy_item(item.price, item.happiness):
            user.store_bought_item_data(item.title, item.price)
            user.save()
            return Response('Purchase successful')
        else:
            return Response('Insufficient funds', status=400)

class EventUpdateMoneyView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        event_id = request.data.get('event_id')

        user = get_object_or_404(User, id=user_id)
        event = get_object_or_404(Events, id=event_id)

        user.update_money_based_on_event(event)
        user.save()

        return JsonResponse({'message': 'Money updated based on event'})



class JobChallangeView(generics.ListCreateAPIView):
    serializer_class=JobChallangeSerializers

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        if self.request.method == "GET" and "id" in self.kwargs:
            return JobChallanges.objects.filter(id=self.kwargs['id'])
        else:
            return JobChallanges.objects.all()
        

class JobChallangesImageView(APIView):
    serializer_class = JobChallangeSerializers

    def get(self, request, *args, **kwargs):
        if "slug" in self.kwargs:
            entity_image = get_object_or_404(JobChallanges, image__endswith=self.kwargs['slug'])
            image_path = entity_image.image.path
            return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')