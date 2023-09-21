from rest_framework import serializers

from .models import Account, Product, Viewing


class InfoProductsSerializer(serializers.ModelSerializer):
    kol_lessons_view = serializers.IntegerField(default=0)
    all_viewing_time = serializers.IntegerField(default=0)
    kol_student = serializers.IntegerField(default=0)
    Percentage_product_purchase = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = [
            "name",
            "kol_lessons_view",
            "all_viewing_time",
            "kol_student",
            "Percentage_product_purchase",
        ]


class UserProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewing
        fields = ["user", "lesson", "viewing_time", "status"]


class ProductLessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewing
        fields = [
            "user",
            "lesson",
            "viewing_time",
            "status",
            "date_last_viewing",
        ]
