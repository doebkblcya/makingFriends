# user/serializers.py
from rest_framework import serializers
from user.models import CustomUser  # 引用您的自定义用户模型

class CustomUserSerializer(serializers.ModelSerializer):
    """
    序列化器，用于将 CustomUser 实例转换为 JSON 格式，或者将输入数据反序列化为 CustomUser 实例。
    """

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']  # 根据需要添加更多字段

    def create(self, validated_data):
        """
        重写 create 方法，确保在创建用户时进行密码加密。
        """
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """
        重写 update 方法，允许更新用户的字段。
        """
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance
