from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from JWT import views

router = DefaultRouter()
router.register('User_Admin', views.UserViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('User_Data/', include(router.urls)),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify')
]


# http://127.0.0.1:8000/User_Data/User_Admin/
# http://127.0.0.1:8000/gettoken/
