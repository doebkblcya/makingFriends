<template>
  <div class="login-page">
    <h1>登录</h1>
    <el-form :model="form" label-width="80px">
      <el-form-item label="用户名">
        <el-input v-model="form.username" placeholder="请输入用户名"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="form.password" type="password" placeholder="请输入密码"></el-input>
      </el-form-item>
      <el-button type="primary" @click="login">登录</el-button>
    </el-form>
    <el-button @click="goToRegister">没有账号？注册</el-button>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import apiClient from '../utils/apiClient';

export default {
  name: 'LoginPage',
  setup() {
    const router = useRouter();
    const form = ref({
      username: '',
      password: ''
    });

    // 登录功能
    const login = async () => {
      try {
        const response = await apiClient.post('login/', form.value);
        localStorage.setItem('auth_token', response.data.token);  // 存储 token
        router.push({ name: 'home' });  // 登录成功后跳转到主页
      } catch (error) {
        console.error('登录失败:', error);
      }
    };

    // 跳转到注册页面
    const goToRegister = () => {
      router.push({ name: 'register' });
    };

    return { form, login, goToRegister };
  }
};
</script>

<style scoped>
.login-page {
  text-align: center;
  margin-top: 20px;
}
</style>
