from django.db.models import Sum
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Account, Lesson, Product, Viewing
from .serializers import (InfoProductsSerializer, ProductLessonsSerializer,
                          UserProductsSerializer)


class UserProductsAPIView(APIView):
    def get(self, request, pk):
        try:
            user = Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        response = []
        for product in user.products.all().prefetch_related("lessons"):
            for lesson in product.lessons.all():
                viewing = Viewing.objects.get(
                    account__user__id=user.pk, lesson__id=lesson.pk
                )
                response.append(UserProductsSerializer(viewing).data)
        return Response(response, status=status.HTTP_201_CREATED)


class ProductLessonsAPIView(APIView):
    def get(self, request, user_pk, product_pk):
        try:
            user = Account.objects.get(pk=user_pk)
            product = user.products.get(pk=product_pk)
        except (Account.DoesNotExist, Product.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
        response = []
        for lesson in product.lessons.all():
            viewing = Viewing.objects.get(
                account__user__id=user.pk, lesson__id=lesson.pk
            )
            response.append(ProductLessonsSerializer(viewing).data)
        return Response(response, status=status.HTTP_201_CREATED)


class InfoProductsAPIView(APIView):
    def get(self, request):
        products = Product.objects.all().prefetch_related("lessons")
        users = Account.objects.all()
        for product in products:
            kol_student = users.filter(products__pk=product.pk).count()
            product.kol_student = kol_student
            all_viewing_time = 0
            kol_lessons_view = 0
            for lesson in product.lessons.all():
                viewings = Viewing.objects.filter(
                    lesson__id=lesson.pk, account__products__pk=product.pk
                )
                kol_lessons_view = viewings.filter(status="se").count()
                all_viewing_time += viewings.aggregate(Sum("viewing_time"))[
                    "viewing_time__sum"
                ]
            product.kol_lessons_view = kol_lessons_view
            product.all_viewing_time = all_viewing_time
            product.percentage_product_purchase = round(
                kol_student / users.count() * 100
            )
        response = InfoProductsSerializer(products, many=True)
        return Response(response.data, status=status.HTTP_201_CREATED)
