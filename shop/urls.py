from django.urls import path, include
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter

from shop.apps import ShopConfig
from shop.views import CategoryViewSet, ProductListAPIView, ProductRetrieveAPIView, BasketItemViews, \
    BasketViewSet

app_name = ShopConfig.name

router = SimpleRouter()
router.register(r"cat", CategoryViewSet, basename="cat")
router.register(r"basket", BasketViewSet, basename="basket")

urlpatterns = [
    path("product/", ProductListAPIView.as_view(permission_classes=(AllowAny,)), name="product_list"),
    path("product/<int:pk>/", ProductRetrieveAPIView.as_view(permission_classes=(AllowAny,)), name="product-retrieve"),
    path('basket-items/', BasketItemViews.as_view()),
    path('basket-items/<int:id>/', BasketItemViews.as_view()),
    path('', include(router.urls))
]
# urlpatterns += router.urls
