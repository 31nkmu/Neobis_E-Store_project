from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from applications.product.models import Product
from applications.product.serializers import ProductSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from applications.feedback.mixins import FavoriteMixin, CommentMixin, RatingMixin, LikeMixin


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ProductViewSet(FavoriteMixin, CommentMixin, RatingMixin, LikeMixin, ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    filterset_fields = ['category']
    search_fields = ['title']
    ordering_fields = ['id', 'price']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['DELETE'])
    def del_images(self, request, pk=None):
        """
        Удаляет все картинки выбранного продукта
        :param request: запрос
        :param pk: id продукта
        """
        product = self.get_object()
        images = product.images.all()
        images.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
