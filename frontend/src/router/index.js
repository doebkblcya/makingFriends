import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';  // 首页
import LoginPage from '../views/LoginPage.vue';  // 登录页
import RegisterPage from '../views/RegisterPage.vue';  // 注册页
import ProfilePage from '../views/ProfilePage.vue';  // 个人信息页

const routes = [
  { path: '/', name: 'home', component: HomePage },
  { path: '/login', name: 'login', component: LoginPage },
  { path: '/register', name: 'register', component: RegisterPage },
  { path: '/profile', name: 'profile', component: ProfilePage },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
