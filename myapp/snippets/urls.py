from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views
from snippets.views import SnippetViewSet, UserViewSet

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
