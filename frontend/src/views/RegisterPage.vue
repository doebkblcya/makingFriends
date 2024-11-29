<template>
  <div class="register-page">
    <h1>注册</h1>
    <el-form :model="form" label-width="80px">
      <el-form-item label="用户名">
        <el-input v-model="form.username" placeholder="请输入用户名"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="form.password" type="password" placeholder="请输入密码"></el-input>
      </el-form-item>
      <el-form-item label="生日">
        <el-date-picker v-model="form.birthday" placeholder="请选择生日"></el-date-picker>
      </el-form-item>
      <el-form-item label="电话">
        <el-input v-model="form.phone_number" placeholder="请输入电话号码"></el-input>
      </el-form-item>
      <el-form-item label="头像">
        <el-upload
          action=""
          :show-file-list="false"
          :on-change="handleAvatarChange"
          :before-upload="beforeAvatarUpload"
        >
          <el-button size="small" type="primary">点击上传头像</el-button>
        </el-upload>
      </el-form-item>
      <el-form-item label="大区">
        <el-select v-model="form.region" placeholder="请选择大区">
          <el-option v-for="region in regionOptions" :key="region.value" :label="region.label" :value="region.value"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="段位">
        <el-select v-model="form.tier" placeholder="请选择段位">
          <el-option v-for="tier in tierOptions" :key="tier.value" :label="tier.label" :value="tier.value"></el-option>
        </el-select>
      </el-form-item>
      <el-button type="primary" @click="register">注册</el-button>
    </el-form>
    <el-button @click="goToLogin">已有账号？登录</el-button>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import apiClient from '../utils/apiClient';

export default {
  name: 'RegisterPage',
  setup() {
    const router = useRouter();
    const form = ref({
      username: '',
      password: '',
      birthday: '',
      phone_number: '',
      profile_picture: null,
      region: '',
      tier: ''
    });

    const regionOptions = [
      { value: 'A1', label: '联盟一区' },
      { value: 'A2', label: '联盟二区' },
      { value: 'A3', label: '联盟三区' },
      { value: 'A4', label: '联盟四区' },
      { value: 'A5', label: '联盟五区' },
      { value: 'IONIA', label: '艾欧尼亚' },
      { value: 'ROSE', label: '黑色玫瑰' },
      { value: 'SUMMITS', label: '峡谷之巅' },
    ];

    const tierOptions = [
      { value: 'IRON', label: '坚韧黑铁' },
      { value: 'BRONZE', label: '英勇黄铜' },
      { value: 'SILVER', label: '不屈白银' },
      { value: 'GOLD', label: '荣耀黄金' },
      { value: 'PLATINUM', label: '华贵铂金' },
      { value: 'EMERALD', label: '流光翡翠' },
      { value: 'DIAMOND', label: '璀璨钻石' },
      { value: 'MASTER', label: '超凡大师' },
      { value: 'GRANDMASTER', label: '傲世宗师' },
      { value: 'CHALLENGER', label: '最强王者' },
    ];

    const register = async () => {
      try {
        await apiClient.post('user/register/', form.value);
        router.push({ name: 'login' });  // 注册成功后跳转到登录页面
      } catch (error) {
        console.error('注册失败:', error);
      }
    };

    const goToLogin = () => {
      router.push({ name: 'login' });
    };

    const handleAvatarChange = (file) => {
      form.value.profile_picture = file.raw;
    };

    const beforeAvatarUpload = (file) => {
      const isImage = file.type.startsWith('image/');
      const isSizeValid = file.size < 2 * 1024 * 1024; // 限制为 2MB
      if (!isImage) {
        this.$message.error('只能上传图片文件!');
      }
      if (!isSizeValid) {
        this.$message.error('图片大小不能超过 2MB!');
      }
      return isImage && isSizeValid;
    };

    return { form, register, goToLogin, regionOptions, tierOptions, handleAvatarChange, beforeAvatarUpload };
  }
};
</script>

<style scoped>
.register-page {
  text-align: center;
  margin-top: 20px;
}
</style>
