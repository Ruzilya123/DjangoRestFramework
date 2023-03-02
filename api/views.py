from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Cart
from .serializers import ProductSerializer, CartSerializer

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"products": serializer.data})
    
    def post(self, request):
        product = request.data.get('products')

        serializer = ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()

        return Response({
            "success": "Product '{}' created successfull".format(product_saved.title)
        })
    
    def put(self, request, pk):
        saved_product = get_object_or_404(Product.objects.all(), pk=pk)
        data = request.data.get('products')

        serializer = ProductSerializer(instance=saved_product, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()

        return Response({
            "success": "Product '{}' update successfull".format(product_saved.title)
        })
    
    def delete(self, request, pk):
        product = get_object_or_404(Product.objects.all(), pk=pk)
        product.delete
        return Response({
            "message": "Product with id '{}' has been deleted".format(pk)
        }, status=204)
    

class CartView(APIView):
    def get(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response({"carts": serializer.data})
    
    def post(self, request):
        cart = request.data.get('carts')

        serializer = CartSerializer(data=cart)
        if serializer.is_valid(raise_exception=True):
            cart_saved = serializer.save()

        return Response({
            "success": "Cart '{}' created successfull".format(cart_saved.title)
        })
    
    def put(self, request, pk):
        saved_cart = get_object_or_404(Cart.objects.all(), pk=pk)
        data = request.data.get('carts')

        serializer = CartSerializer(instance=saved_cart, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            cart_saved = serializer.save()

        return Response({
            "success": "Cart '{}' update successfull".format(cart_saved.title)
        })
    
    def delete(self, request, pk):
        cart = get_object_or_404(Cart.objects.all(), pk=pk)
        cart.delete
        return Response({
            "message": "Cart with id '{}' has been deleted".format(pk)
        }, status=204)
    