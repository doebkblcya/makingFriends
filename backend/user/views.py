from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# 注册视图
@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not username or not email or not password:
        return Response({"error": "缺少必填字段"}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({"message": "注册成功"}, status=status.HTTP_201_CREATED)

# 注销视图
@api_view(['POST'])
def logout(request):
    auth_logout(request)
    return Response({"message": "注销成功"}, status=status.HTTP_200_OK)

# 更新用户信息视图
@api_view(['POST'])
def update_user_info(request):
    if not request.user.is_authenticated:
        return Response({"error": "用户未登录"}, status=status.HTTP_401_UNAUTHORIZED)
    
    user = request.user  # 假设用户已登录并通过 Token 认证
    email = request.data.get('email')
    if email:
        user.email = email
        user.save()
        return Response({"message": "更新成功"}, status=status.HTTP_200_OK)
    return Response({"error": "缺少邮箱字段"}, status=status.HTTP_400_BAD_REQUEST)
