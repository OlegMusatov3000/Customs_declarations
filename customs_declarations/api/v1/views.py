import datetime as dt
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from posting.models import (
    Seller,
    Etgb_of_posting,
)
from .authentication import ClientIdApiKeyAuthentication
from .serializers import (
    SignUpSerializer,
    AuthSerializer,
    Etgb_of_postingSerializer,
)
from .utils import send_confirmation_code


class SignUpViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Создание обьектов класса Seller
    и отправка кода подтверждения на указанный email.
    """
    queryset = Seller.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = SignUpSerializer(data=request.data)
        if (
                not serializer.is_valid()
                and not Seller.objects.filter(**serializer.data)
        ):
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        user, _ = Seller.objects.get_or_create(**serializer.data)
        confirmation_code = default_token_generator.make_token(user)
        send_confirmation_code(user.email, confirmation_code)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Выдает пользователю его идентификатор и Api-ключ."""
    queryset = Seller.objects.all()
    serializer_class = AuthSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = AuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        confirmation_code = serializer.validated_data.get('confirmation_code')
        user = get_object_or_404(Seller, username=username)
        if default_token_generator.check_token(user, confirmation_code):
            message = {
                'Client-id': user.client_id,
                'Api-key': user.api_key
            }
            return Response(message, status=status.HTTP_200_OK)
        message = {'confirmation_code': 'Код подтверждения неверен'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


class GetEtgbViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    """
    Метод для получения таможенных деклараций
    Elektronik Ticaret Gümrük Beyannamesi (ETGB)
    для продавцов из Турции.
    """
    serializer_class = Etgb_of_postingSerializer
    authentication_classes = (ClientIdApiKeyAuthentication, )

    def get_queryset(self):
        if self.request.data.get('date'):
            date = (
                dt.datetime.strptime(
                    self.request.data.get('date').get('from'),
                    '%Y-%m-%dT%H:%M:%S.818Z'
                ),
                dt.datetime.strptime(
                    self.request.data.get('date').get('to'),
                    '%Y-%m-%dT%H:%M:%S.818Z'
                )
            )
            new_queryset = Etgb_of_posting.objects.filter(
                seller=self.request.user,
                etgb__date__gte=date[0]
            ).filter(etgb__date__lte=date[1])
            return new_queryset

        date = [
            dt.datetime.now(),
            dt.timedelta(days=4)
        ]
        new_queryset = Etgb_of_posting.objects.filter(
            seller=self.request.user,
            etgb__date__gte=date[0] - date[1]
        )
        return new_queryset

    def create(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
