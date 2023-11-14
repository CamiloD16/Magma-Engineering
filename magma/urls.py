from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from apis.views import MyTokenObtainPairView, ChangePasswordAPIView

from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("data-information/", include("apis.urls")),
    path('data-information/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('data-information/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('data-information/change-password/', ChangePasswordAPIView.as_view(), name='change_password_api'),
    re_path(r"^(?:.*)/?$", TemplateView.as_view(template_name="index.html")),
]
