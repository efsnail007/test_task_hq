from django.urls import path

from .views import (InfoProductsAPIView, ProductLessonsAPIView,
                    UserProductsAPIView)

urlpatterns = [
    path("api/v1/user/<int:pk>/products/", UserProductsAPIView.as_view()),
    path(
        "api/v1/user/<int:user_pk>/product/<int:product_pk>/lessons/",
        ProductLessonsAPIView.as_view(),
    ),
    path("api/v1/product/info/", InfoProductsAPIView.as_view()),
]
