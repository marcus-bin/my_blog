"""drf_vue_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comment.views import CommentViewSet
from article import views
from user_info.views import UserViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="博客 API",
        default_version='v1',
        description="个人博客系统系统API接口文档",
        terms_of_service="",
        contact=openapi.Contact(email="marcus_bin@foxmail.com"),
        license=openapi.License(name="GPLv3 License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'tag', views.TagViewSet)
router.register(r'avatar', views.AvatarViewSet)
router.register(r'user', UserViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # path('api/article/', include('article.urls', namespace='article'))
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api_doc/', schema_view.with_ui('redoc', cache_timeout=0), name="blog API"),
]
