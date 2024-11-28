<template>
  <div class="home-page">
    <h1>Hello World</h1>
    <el-button type="primary" @click="logout">注销</el-button>
    <el-button type="info" @click="goToProfile">修改个人信息</el-button>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';
import apiClient from '../utils/apiClient';  // 引入之前配置的 axios 实例

export default {
  name: 'HomePage',
  setup() {
    const router = useRouter();

    // 注销功能
    const logout = async () => {
      try {
        await apiClient.post('logout/');
        localStorage.removeItem('auth_token');  // 清除本地存储的 token
        router.push({ name: 'login' });  // 注销成功后跳转到登录页面
      } catch (error) {
        console.error('注销失败:', error);
      }
    };

    // 跳转到个人信息修改页面
    const goToProfile = () => {
      router.push({ name: 'profile' });
    };

    return { logout, goToProfile };
  }
};
</script>

<style scoped>
.home-page {
  text-align: center;
  margin-top: 20px;
}
</style>
