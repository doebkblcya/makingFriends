<template>
    <div>
      <h1>注册</h1>
      <form @submit.prevent="registerUser">
        <label for="username">用户名:</label>
        <input type="text" v-model="username" required />
  
        <label for="password">密码:</label>
        <input type="password" v-model="password" required />
  
        <label for="email">电子邮箱:</label>
        <input type="email" v-model="email" required />
  
        <button type="submit">注册</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
        email: ''
      };
    },
    methods: {
      registerUser() {
        axios.post('http://localhost:8000/api/user/register/', {
          username: this.username,
          password: this.password,
          email: this.email
        })
        .then(response => {
          console.log('注册成功:', response.data);
          this.$router.push('/login');  // 注册成功后跳转到登录页
        })
        .catch(error => {
          console.log('注册失败:', error.response.data);
        });
      }
    }
  };
  </script>
  
  <style scoped>
  /* 样式 */
  </style>
  