from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [

]


router = DefaultRouter()

router.register('products', ProductModelViewSet, basename='product')
router.register('reviews', ReviewModelViewSet, basename='review')
router.register('product-tags', ProductTagModelViewSet, basename='producttag')
router.register('favorite-products', FavoriteProductModelViewSet, basename='favoriteproduct')
router.register('carts', CartModelViewSet, basename='cart')
router.register('product-images', ProductImageModelViewSet, basename='productimage')


urlpatterns += router.urls