from rest_framework.permissions import  IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Group, Staff, Product, Shift, Order, UserModel
from .serializers import GroupSerializer, StaffSerializer, ProductSerializer, ShiftSerializer, OrderSerializer, UserModelSerializer
from .permissions import GroupPermission

# Группы пользователей менять, видеть, удалять, добавлять может только админ
@api_view(['GET'])
@permission_classes([IsAdminUser])
def group_list(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)

@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def group_list_detail(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)

# Сотрудников менять, видеть, удалять, добавлять может только админ
@api_view(['GET'])
@permission_classes([IsAdminUser])
def staff_list(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)

@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def staff_list_detail(request):
    staff = Staff.objects.all()
    serializer = StaffSerializer(staff, many=True)
    return Response(serializer.data)

# Товары видят только админ и официант
@api_view(['GET'])
@permission_classes([GroupPermission(['admin', 'waiter'])])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# Товары менять, удалять, добавлять может только админ
@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

# Смены менять, видеть, удалять, добавлять может только админ
@api_view(['GET'])
@permission_classes([IsAdminUser])
def shift_list(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)

@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def shift_list_detail(request):
    shifts = Shift.objects.all()
    serializer = ShiftSerializer(shifts, many=True)
    return Response(serializer.data)

# Заказы видят админ, официант и повар
@api_view(['GET'])
@permission_classes([GroupPermission(['admin', 'waiter', 'cook'])])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

# Заказы менять, добавлять может только повар и официант
@api_view(['POST', 'PUT'])
@permission_classes([GroupPermission(['cook', 'waiter'])])
def order_list_detail(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)

# Заказы удалять может только официант
@api_view(['DELETE'])
@permission_classes([GroupPermission(['waiter'])])
def order_delete(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)

# Пользователей менять, видеть, удалять, добавлять может только админ
@api_view(['GET'])
@permission_classes([IsAdminUser])
def users_list(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)

@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def users_list_detail(request):
    users = UserModel.objects.all()
    serializer = UserModelSerializer(users, many=True)
    return Response(serializer.data)