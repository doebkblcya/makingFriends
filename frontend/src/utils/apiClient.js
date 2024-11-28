import axios from 'axios';  // 引入 axios 库，用于发送 HTTP 请求

// 创建 axios 实例
const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api/',  // 后端 API 基础路径
  timeout: 5000,  // 设置请求超时时间，单位为毫秒，5秒超时
  headers: {
    'Content-Type': 'application/json',  // 默认请求头，适用于 JSON 数据
  },
});

// 请求拦截器
apiClient.interceptors.request.use(config => {
  const token = localStorage.getItem('auth_token');  // 从 localStorage 获取存储的 Token
  if (token) {
    config.headers.Authorization = `Token ${token}`;  // 如果有 Token，将其加入请求头
  }

  // 如果请求包含 FormData（如文件上传），更改 Content-Type 为 multipart/form-data
  if (config.data && config.data instanceof FormData) {
    config.headers['Content-Type'] = 'multipart/form-data';
  }

  return config;  // 返回配置后的请求
});

// 响应拦截器
apiClient.interceptors.response.use(
  response => response,  // 响应成功时直接返回响应数据
  error => {
    if (error.response && error.response.status === 401) {
      // 如果是未授权错误（401），可以跳转到登录页或清除用户信息
      localStorage.removeItem('auth_token');
      // 跳转到登录页面，假设你使用了 Vue Router
      window.location.href = '/login';  // 或者使用 this.$router.push('/login');
    }
    console.error('API 错误：', error);  // 控制台输出错误信息
    return Promise.reject(error);  // 返回错误
  }
);

// 导出配置好的 axios 实例，供应用中的其他模块使用
export default apiClient;