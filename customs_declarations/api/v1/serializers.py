from rest_framework import serializers

from posting.models import (
    Seller,
    Etgb_of_posting,
    Etgb,
)


class SignUpSerializer(serializers.ModelSerializer):
    """Создает нового пользователя при регистрации."""

    class Meta:
        fields = ('username', 'email',)
        model = Seller


class AuthSerializer(serializers.Serializer):
    """Сериализатор для класса Seller при получении кода подтверждения."""

    username = serializers.RegexField(
        regex=r'^[\w.@+-]+$',
        max_length=150,
        required=True
    )
    confirmation_code = serializers.CharField(
        max_length=150,
        required=True
    )


class EtgbSerializer(serializers.ModelSerializer):
    """Сериализатор для модели "Etgb"."""

    class Meta:
        model = Etgb
        fields = ('number', 'date', 'url')


class Etgb_of_postingSerializer(serializers.ModelSerializer):
    """Сериализатор для модели "Etgb_of_posting"."""
    etgb = EtgbSerializer(read_only=True, many=False)

    class Meta:
        model = Etgb_of_posting
        fields = ('posting_number', 'etgb')
