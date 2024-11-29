from rest_framework import serializers
from user.models import CustomUser  # 引用自定义用户模型

class CustomUserSerializer(serializers.ModelSerializer):
    """
    序列化器，用于将 CustomUser 实例转换为 JSON 格式，
    或者将输入数据反序列化为 CustomUser 实例。
    """

    class Meta:
        model = CustomUser  # 使用自定义用户模型（CustomUser）
        fields = [
            'id', 'username', 'email', 'password', 
            'birthday', 'phone_number', 'profile_picture', 
            'region', 'tier'  # 修正为 'tier' 而非 'rank'
        ]  # 增加了生日、电话、头像、大区和段位字段

        extra_kwargs = {
            'password': {'write_only': True},  # 密码字段仅用于写入，返回时不会显示
        }

    def create(self, validated_data):
        """
        重写 create 方法，确保在创建用户时进行密码加密， 
        并处理所有自定义字段（例如头像、生日、大区、段位等）
        """
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            birthday=validated_data.get('birthday'),
            phone_number=validated_data.get('phone_number'),
            profile_picture=validated_data.get('profile_picture'),
            region=validated_data.get('region'),
            tier=validated_data.get('tier')  # 使用 'tier' 而非 'rank'
        )
        return user

    def update(self, instance, validated_data):
        """
        重写 update 方法，允许更新用户的字段，
        同时对密码字段进行哈希处理，更新头像、大区、段位等。
        """
        # 更新基本字段（用户名、邮箱）
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        
        # 如果提供了新密码，则更新密码，且进行哈希处理
        if 'password' in validated_data and validated_data['password']:
            instance.set_password(validated_data['password'])  # 确保密码被加密

        # 更新生日、电话号码、头像、大区和段位等
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.region = validated_data.get('region', instance.region)
        instance.tier = validated_data.get('tier', instance.tier)  # 使用 'tier' 而非 'rank'
        
        # 保存更新后的用户实例
        instance.save()
        return instance
