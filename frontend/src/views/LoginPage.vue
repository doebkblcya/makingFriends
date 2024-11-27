<template>
    <div>
      <h1>登录</h1>
      <form @submit.prevent="loginUser">
        <label for="username">用户名:</label>
        <input type="text" v-model="username" required />
  
        <label for="password">密码:</label>
        <input type="password" v-model="password" required />
  
        <button type="submit">登录</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: ''
      };
    },
    methods: {
      loginUser() {
        axios.post('http://localhost:8000/api/user/login/', {
          username: this.username,
          password: this.password
        })
        .then(response => {
          console.log('登录成功:', response.data);
          localStorage.setItem('token', response.data.token);  // 保存 token
          this.$router.push('/profile');  // 登录成功后跳转到个人信息页
        })
        .catch(error => {
          console.log('登录失败:', error.response.data);
        });
      }
    }
  };
  </script>
  
  <style scoped>
  /* 样式 */
  </style>
  