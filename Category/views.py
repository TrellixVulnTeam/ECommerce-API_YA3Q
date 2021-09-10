from Product.models import Product
from Product.serializers import ProductSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from .models import Category
from .serializers import CategorySerializer
from core.custompermissions import IsAdminOrReadOnly
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

class CategoryViewSet(ModelViewSet):
	my_tags = ['Category']
	permission_classes = (IsAdminOrReadOnly,)
	queryset = Category.objects.all()
	search_fields = ['category_name', ]
	filter_backends = [SearchFilter, OrderingFilter]
	serializer_class = CategorySerializer


class ProductsinCategoryView(GenericAPIView):

	"""
	APIView for retrieving a list of Products that belongs to a Category
	by the category id.
	Operation can be carried out any user.
	"""
	my_tags = ['Category']
	permission_classes = (AllowAny,)

	def get(self, request, id):
		product = Product.objects.filter(category=id)

		ser = ProductSerializer(product, many=True)

		return Response(ser.data)
