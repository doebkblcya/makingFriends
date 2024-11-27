import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios';
import router from './router';

createApp(App).mount('#app')

axios.defaults.baseURL = 'http://localhost:8000/api/'; // 后端API地址

// 在需要的地方使用 axios 发送请求
axios.get('users/')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });

const app = createApp(App);
app.use(router);
app.mount('#app');
