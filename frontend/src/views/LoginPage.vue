<template>
  <div class="login-page">
    <h1>登录</h1>
    <el-form :model="form" label-width="80px" ref="loginForm" :rules="formRules">
      <el-form-item label="用户名" prop="username">
        <el-input v-model="form.username" placeholder="请输入用户名"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input v-model="form.password" type="password" placeholder="请输入密码"></el-input>
      </el-form-item>
      <el-button type="primary" @click="login" :loading="loading" :disabled="loading">登录</el-button>
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
    const loading = ref(false);  // 控制按钮加载状态

    // 表单验证规则
    const formRules = {
      username: [
        { required: true, message: '请输入用户名', trigger: 'blur' }
      ],
      password: [
        { required: true, message: '请输入密码', trigger: 'blur' }
      ]
    };

    // 登录功能
    const login = async () => {
      loading.value = true;  // 登录请求开始时，设置按钮为加载状态
      try {
        const response = await apiClient.post('user/login/', form.value);
        localStorage.setItem('auth_token', response.data.token);  // 存储 token
        router.push({ name: 'home' });  // 登录成功后跳转到主页
      } catch (error) {
        console.error('登录失败:', error);
      } finally {
        loading.value = false;  // 请求结束后，恢复按钮的状态
      }
    };

    // 跳转到注册页面
    const goToRegister = () => {
      router.push({ name: 'register' });
    };

    return { form, login, goToRegister, formRules, loading };
  }
};
</script>

<style scoped>
.login-page {
  text-align: center;
  margin-top: 20px;
}
</style>
