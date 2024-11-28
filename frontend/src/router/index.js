import { createRouter, createWebHistory } from 'vue-router';  // 从 vue-router 导入路由相关的函数
import HomePage from '../views/HomePage.vue';  // 导入首页视图组件
import LoginPage from '../views/LoginPage.vue';  // 导入登录页视图组件
import RegisterPage from '../views/RegisterPage.vue';  // 导入注册页视图组件
import ProfilePage from '../views/ProfilePage.vue';  // 导入个人信息页视图组件

// 定义路由配置
const routes = [
  { path: '/', name: 'home', component: HomePage },  // 首页路由，访问 '/' 时显示 HomePage 组件
  { path: '/login', name: 'login', component: LoginPage },  // 登录页路由，访问 '/login' 时显示 LoginPage 组件
  { path: '/register', name: 'register', component: RegisterPage },  // 注册页路由，访问 '/register' 时显示 RegisterPage 组件
  { path: '/profile', name: 'profile', component: ProfilePage },  // 个人信息页路由，访问 '/profile' 时显示 ProfilePage 组件
];

// 创建 Vue Router 实例
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),  // 使用 HTML5 History 模式，支持前端路由管理
  routes,  // 注册路由规则
});

// 导出路由实例
export default router;
