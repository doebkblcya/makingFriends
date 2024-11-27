<template>
    <div class="login-page">
      <h2>登录</h2>
      <form @submit.prevent="login">
        <div>
          <label for="username">用户名：</label>
          <input
            type="text"
            id="username"
            v-model="username"
            placeholder="请输入用户名"
            required
          />
        </div>
  
        <div>
          <label for="password">密码：</label>
          <input
            type="password"
            id="password"
            v-model="password"
            placeholder="请输入密码"
            required
          />
        </div>
  
        <div v-if="errorMessage" class="error-message">
          <p>{{ errorMessage }}</p>
        </div>
  
        <div>
          <button type="submit">登录</button>
        </div>
      </form>
  
      <p>还没有账号？<router-link to="/register">注册</router-link></p>
    </div>
  </template>
  
  <script>
    import apiClient from '../utils/axios';  // 导入 axios 实例
  
  export default {
    data() {
      return {
        username: '',
        password: '',
        errorMessage: ''
      };
    },
    methods: {
      login() {
        const credentials = {
          username: this.username,
          password: this.password
        };
  
        // 使用 apiClient 发送登录请求
        apiClient.post('user/login/', credentials)
          .then(response => {
            console.log('Login successful', response);
            // 将返回的 token 存储在 localStorage 中
            localStorage.setItem('auth_token', response.data.token);
            // 登录成功后跳转到个人信息页面
            this.$router.push('/profile');
          })
          .catch(error => {
            if (error.response && error.response.data) {
              this.errorMessage = error.response.data.detail;  // 显示错误信息
            } else {
              this.errorMessage = '登录失败，请重试';  // 未知错误
            }
            console.error('Login error:', error);
          });
      }
    }
  };
  </script>
  
  <style scoped>
  .login-page {
    width: 300px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    text-align: center;
  }
  
  form div {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: #42b983;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #369c70;
  }
  
  .error-message {
    color: red;
    margin-bottom: 10px;
  }
  </style>
  