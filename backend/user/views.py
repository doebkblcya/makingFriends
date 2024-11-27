# user/views.py
from django.http import JsonResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from user.serializers import CustomUserSerializer  # 导入自定义用户序列化器

# 获取自定义用户模型
CustomUser = get_user_model()

# 注册视图
@api_view(['POST'])
def register(request):
    """
    注册一个新用户
    """
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()  # 使用序列化器创建用户
        return Response({"message": "注册成功"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 登录视图 (使用 DRF 内置的 Token 认证)
@api_view(['POST'])
def login(request):
    """
    使用用户名和密码登录，返回 Token
    """
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "缺少用户名或密码"}, status=status.HTTP_400_BAD_REQUEST)

    user = CustomUser.objects.filter(username=username).first()

    if user and user.check_password(password):
        # 登录成功，生成并返回 Token
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    
    return Response({"error": "用户名或密码错误"}, status=status.HTTP_400_BAD_REQUEST)

# 注销视图
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # 确保只有已登录用户可以访问
def logout(request):
    try:
        # 删除用户的认证 Token
        request.user.auth_token.delete()
        return Response({"message": "注销成功"})
    except AttributeError:
        # 如果未登录用户尝试访问
        return Response({"error": "用户未认证"}, status=400)

# 更新用户信息视图（例如：更新邮箱）
@api_view(['POST'])
def update_user_info(request):
    """
    更新当前认证用户的个人信息
    """
    # 确保用户已认证
    if not request.user.is_authenticated:
        return Response({"error": "用户未认证"}, status=status.HTTP_401_UNAUTHORIZED)
    
    user = request.user  # 当前认证用户

    # 只允许更新邮箱，您可以根据需求扩展
    email = request.data.get('email')
    if email:
        user.email = email
        user.save()
        return Response({"message": "更新成功"}, status=status.HTTP_200_OK)
    
    return Response({"error": "缺少邮箱字段"}, status=status.HTTP_400_BAD_REQUEST)
