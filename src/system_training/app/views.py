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
        products = user.products.all()
        response = []
        for product in products:
            for lesson in product.lessons.all():
                print(lesson)
                viewing = Viewing.objects.get(
                    user__id=user.pk, lesson__id=lesson.pk
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
                user__id=user.pk, lesson__id=lesson.pk
            )
            response.append(ProductLessonsSerializer(viewing).data)
        return Response(response, status=status.HTTP_201_CREATED)


class InfoProductsAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        response = InfoProductsSerializer(products, many=True)
        return Response(response.data, status=status.HTTP_201_CREATED)
