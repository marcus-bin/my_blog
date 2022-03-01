from rest_framework import status, generics, filters
from article.models import Article, Tag, Avatar
from article.permissions import IsAdminUserOrReadOnly
from article.models import Category
from article.serializers import CategorySerializer, CategoryDetailSerializer, TagSerializer, ArticleDetailSerializer, \
    AvatarSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import viewsets
from article.serializers import ArticleSerializer


class APIDoc(object):
    openapi = openapi

    def __init__(self):
        self.GET_ARGS = []

    def add_GET_ARGS(self, arg, description, type=openapi.TYPE_STRING, required=False):
        self.GET_ARGS.append(
            openapi.Parameter(arg, openapi.IN_QUERY, description=description, type=type, required=required))

    def get_GET_ARGS(self):

        return self.GET_ARGS


class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        else:
            return CategoryDetailSerializer


# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleListSerializer
#     permission_classes = [IsAdminUserOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
#
#     # class Meta:
#     #     read_only_fields = ['author']
#
#
# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleDetailSerializer
#     permission_classes = [IsAdminUserOrReadOnly]
#
#
