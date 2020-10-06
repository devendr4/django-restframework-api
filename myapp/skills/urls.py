from django.urls import path, include
from rest_framework.routers import DefaultRouter
from skills import views

router = DefaultRouter()
router.register(r'skills', views.SkillViewSet)

urlpatterns = [
    path('', include(router.urls))
]
