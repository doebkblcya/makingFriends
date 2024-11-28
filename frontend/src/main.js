import { createApp } from 'vue';  // 从 Vue 导入创建应用的函数
import App from './App.vue';  // 导入根组件 App.vue
import router from './router';  // 导入 Vue Router 配置
import axios from 'axios';  // 导入 axios 库，用于发送 HTTP 请求

// 引入 Element UI 和样式
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

// 配置 axios 全局默认设置
axios.defaults.baseURL = 'http://localhost:8000/api/';  // 设置 axios 的基础 URL，所有的请求将会以这个 URL 为基础
// 例如：axios.get('/user/') 实际会发请求到 http://localhost:8000/api/user/

// 创建 Vue 应用实例
const app = createApp(App);  // 创建 Vue 应用实例，并指定根组件

// 注册 Vue Router 插件
app.use(router);  // 注册路由插件，使应用支持客户端路由（页面跳转）

// 使用 Element UI
app.use(ElementPlus)

// 挂载应用到 DOM 中，指定挂载点为 id 为 'app' 的 DOM 元素
app.mount('#app');  // 将 Vue 应用挂载到页面中具有 id="app" 的元素上
