from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from user.serializers import CustomUserSerializer
from user.models import CustomUser  # 引用自定义用户模型

# 注册视图
@api_view(['POST'])
def register(request):
    """
    注册一个新用户
    """
    # 获取请求数据并验证
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        # 创建用户并保存
        serializer.save()
        return Response({"message": "注册成功"}, status=status.HTTP_201_CREATED)
    # 如果数据无效，返回错误信息
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 登录视图
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
@permission_classes([IsAuthenticated])  # 只有认证用户可以访问
def logout(request):
    """
    注销当前用户
    """
    try:
        # 删除当前用户的认证 Token
        request.user.auth_token.delete()
        return Response({"message": "注销成功"}, status=status.HTTP_200_OK)
    except AttributeError:
        # 如果未认证用户尝试注销，返回错误
        return Response({"error": "用户未认证"}, status=status.HTTP_401_UNAUTHORIZED)

# 更新用户信息视图
@api_view(['PUT'])
@permission_classes([IsAuthenticated])  # 只有认证用户可以访问
def update_user_info(request):
    """
    更新当前认证用户的个人信息，包括头像、大区、段位等
    """
    user = request.user  # 当前认证用户

    # 获取请求中的更新数据
    email = request.data.get('email')
    birthday = request.data.get('birthday')
    phone_number = request.data.get('phone_number')
    profile_picture = request.data.get('profile_picture')
    region = request.data.get('region')
    tier = request.data.get('tier')

    # 更新用户信息
    if email:
        user.email = email
    if birthday:
        user.birthday = birthday
    if phone_number:
        user.phone_number = phone_number
    if profile_picture:
        user.profile_picture = profile_picture
    if region:
        user.region = region
    if tier:
        user.tier = tier

    # 保存更新后的用户信息
    user.save()

    return Response({"message": "更新成功"}, status=status.HTTP_200_OK)
