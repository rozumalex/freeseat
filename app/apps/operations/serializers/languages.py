from apps.operations.models import Language
from rest_framework import serializers

__all__ = ["LanguageSerializer" ""]


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = [
            "code",
            "name_en",
            "name_ru",
            "name_uk",
            "name_pl",
        ]
