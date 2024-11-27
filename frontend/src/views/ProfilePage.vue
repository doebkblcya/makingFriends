<template>
    <div>
      <h1>更新个人信息</h1>
      <form @submit.prevent="updateUserInfo">
        <div>
          <label for="email">新的邮箱:</label>
          <input type="email" v-model="email" id="email" required />
        </div>
        <button type="submit">提交</button>
      </form>
      <div v-if="message" class="message">{{ message }}</div>
      <div v-if="error" class="error">{{ error }}</div>
    </div>
  </template>
  
  <script>
  import apiClient from '../utils/axios'; // 导入配置好的 axios 实例

export default {
  data() {
    return {
      email: '',
      errorMessage: '',
    };
  },
  methods: {
    updateUserInfo() {
      const updatedData = {
        email: this.email, // 假设你只更新邮箱
      };

      // 在请求头中添加 Authorization
      apiClient
        .post('user/update/', updatedData)  // 使用正确的 API 路径
        .then(response => {
          console.log('更新成功', response);
          // 处理更新成功逻辑，如跳转等
        })
        .catch(error => {
          if (error.response && error.response.data) {
            this.errorMessage = error.response.data.detail || '更新失败';
          } else {
            this.errorMessage = '更新失败，请重试';
          }
          console.error('更新失败：', error);
        });
    },
  },
  created() {
    // 获取用户的 email 或其他信息（这里假设邮箱作为初始数据）
    const token = localStorage.getItem('auth_token');
    if (token) {
      // 如果 token 存在，可以在 created 生命周期钩子中加载当前用户数据
      apiClient
        .get('user/info/')  // 假设有一个获取用户信息的接口
        .then(response => {
          this.email = response.data.email;  // 填充用户信息
        })
        .catch(error => {
          console.error('加载用户信息失败', error);
        });
    }
  },
};
  </script>
  
  <style scoped>
  /* 样式可以根据需要进行调整 */
  form {
    max-width: 400px;
    margin: 0 auto;
  }
  input {
    width: 100%;
    padding: 8px;
    margin: 5px 0;
  }
  button {
    padding: 10px 15px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
  }
  button:hover {
    background-color: #45a049;
  }
  .message {
    margin-top: 10px;
    color: green;
  }
  .error {
    margin-top: 10px;
    color: red;
  }
  </style>
  