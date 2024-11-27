import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';

// 配置 axios 全局默认设置
axios.defaults.baseURL = 'http://localhost:8000/api/';

// 创建 Vue 应用
const app = createApp(App);

// 注册 Vue Router
app.use(router);

// 挂载应用到 DOM
app.mount('#app');

