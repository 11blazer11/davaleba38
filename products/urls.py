from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [

]


router = DefaultRouter()
router.register('products', views.ProductModelViewSet)

urlpatterns += router.urls