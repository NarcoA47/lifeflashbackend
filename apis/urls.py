from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserRegistrationView, UserLoginView

# router = DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('user/<int:pk>', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'partial_update',
        'delete': 'destroy',
    })),
]