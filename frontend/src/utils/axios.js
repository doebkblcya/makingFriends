import axios from 'axios';

// 创建 axios 实例
const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api/', // 后端 API 基础路径
  timeout: 5000, // 请求超时时间
  headers: {
    'Content-Type': 'application/json',
  },
});

// 请求拦截器
apiClient.interceptors.request.use(config => {
  // 如果需要，可以在此处添加 Authorization 令牌
  const token = localStorage.getItem('auth_token');
  if (token) {
    config.headers.Authorization = `Token ${token}`;
  }
  return config;
});

// 响应拦截器
apiClient.interceptors.response.use(
  response => response,
  error => {
    console.error('API 错误：', error);
    return Promise.reject(error);
  }
);

export default apiClient;
