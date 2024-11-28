from django.urls import path
from .views import register, logout, update_user_info  # 引入视图函数
from rest_framework.authtoken.views import obtain_auth_token  # 引入 DRF 提供的 Token 认证视图

urlpatterns = [
    # 用户注册
    path('register/', register, name='register'),  # 映射到注册视图，通常用于新用户创建账户

    # 用户登录
    path('login/', obtain_auth_token, name='login'),  # 使用 DRF 提供的 `obtain_auth_token` 视图来获取登录用户的 Token

    # 用户注销
    path('logout/', logout, name='logout'),  # 映射到注销视图，通常用于用户登出，销毁会话或 Token

    # 更新用户信息
    path('update/', update_user_info, name='update_user_info'),  # 映射到更新用户信息的视图，用于修改用户的个人信息
]
