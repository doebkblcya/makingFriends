<template>
    <div>
      <h1>个人信息</h1>
      <form @submit.prevent="updateProfile">
        <label for="birthday">生日:</label>
        <input type="date" v-model="birthday" />
  
        <label for="phone_number">电话:</label>
        <input type="text" v-model="phone_number" />
  
        <label for="profile_picture">头像:</label>
        <input type="file" @change="handleFileUpload" />
  
        <button type="submit">更新</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        birthday: '',
        phone_number: '',
        profile_picture: null
      };
    },
    created() {
      this.fetchUserProfile();
    },
    methods: {
      fetchUserProfile() {
        const token = localStorage.getItem('token');
        axios.get('http://localhost:8000/api/user/profile/', {
          headers: { Authorization: `Token ${token}` }
        })
        .then(response => {
          const user = response.data;
          this.birthday = user.birthday;
          this.phone_number = user.phone_number;
        })
        .catch(error => {
          console.log('获取个人信息失败:', error.response.data);
        });
      },
      handleFileUpload(event) {
        this.profile_picture = event.target.files[0];
      },
      updateProfile() {
        const formData = new FormData();
        formData.append('birthday', this.birthday);
        formData.append('phone_number', this.phone_number);
        if (this.profile_picture) {
          formData.append('profile_picture', this.profile_picture);
        }
  
        const token = localStorage.getItem('token');
        axios.put('http://localhost:8000/api/user/update/', formData, {
          headers: {
            Authorization: `Token ${token}`,
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(response => {
          console.log('个人信息更新成功:', response.data);
        })
        .catch(error => {
          console.log('更新失败:', error.response.data);
        });
      }
    }
  };
  </script>
  
  <style scoped>
  /* 样式 */
  </style>
  