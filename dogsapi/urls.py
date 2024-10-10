from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .controllers import DogList, DogDetail, BreedViewSet
from . import views

router = DefaultRouter()
router.register(r'breeds', BreedViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('about/', views.about, name='about'),
    path('dogs/', DogList.as_view(), name='dog-list'),
    path('dogs/<int:pk>/', DogDetail.as_view(), name='dog-detail'),
]
