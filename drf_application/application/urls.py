from django.urls import path
from application import views as api_views
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('dictionary/', api_views.DictionaryView.as_view(), name="dictionary"),
    path('dictionary/<int:pk>/', api_views.DictionaryDetailView.as_view(), name="dictionary-detail"),
    path('api-token-auth/', views.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
   