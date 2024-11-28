import { createStore } from 'vuex';
import axios from 'axios';  // 引入 axios 进行 API 请求

export default createStore({
  // 定义状态
  state: {
    user: null,  // 用户信息，默认是 null
    isLoggedIn: false,  // 登录状态
  },

  // 定义 mutations，用于同步更新状态
  mutations: {
    // 设置用户信息
    setUser(state, user) {
      state.user = user;
      state.isLoggedIn = !!user;  // 如果有用户信息，则标记为已登录
    },

    // 清除用户信息
    clearUser(state) {
      state.user = null;
      state.isLoggedIn = false;
    },
  },

  // 定义 actions，用于处理异步操作
  actions: {
    // 登录操作
    login({ commit }, credentials) {
      axios.post('/api/user/login/', credentials)  // 向后端发送登录请求
        .then(response => {
          const token = response.data.token;
          localStorage.setItem('auth_token', token);  // 存储 Token
          axios.defaults.headers['Authorization'] = `Token ${token}`;  // 设置 axios 默认的 Authorization header
          commit('setUser', response.data.user);  // 更新 Vuex 中的用户信息
        })
        .catch(error => {
          console.error('登录失败:', error);
        });
    },

    // 获取当前登录的用户数据
    fetchUser({ commit }) {
      const token = localStorage.getItem('auth_token');  // 从 localStorage 获取 Token
      if (token) {
        axios.get('/api/user/profile/', {  // 获取用户资料的接口
          headers: { Authorization: `Token ${token}` },
        })
          .then(response => {
            commit('setUser', response.data);  // 更新用户数据
          })
          .catch(error => {
            console.error('获取用户数据失败:', error);
            commit('clearUser');  // 如果获取失败，清除用户信息
          });
      }
    },

    // 注销操作
    logout({ commit }) {
      localStorage.removeItem('auth_token');  // 清除 Token
      delete axios.defaults.headers['Authorization'];  // 清除 axios 的 Authorization header
      commit('clearUser');  // 清除用户信息
    },

    // 更新用户信息
    updateUser({ commit }, userInfo) {
      axios.put('/api/user/update/', userInfo)  // 更新用户信息的接口
        .then(response => {
          commit('setUser', response.data);  // 更新 Vuex 中的用户信息
        })
        .catch(error => {
          console.error('更新用户信息失败:', error);
        });
    },
  },

  // 定义 getters，用于访问状态数据
  getters: {
    isLoggedIn(state) {
      return state.isLoggedIn;
    },
    getUser(state) {
      return state.user;
    },
  },

  // 持久化 Vuex 状态 (比如保持用户信息和登录状态)
  plugins: [
    store => {
      store.subscribe((mutation, state) => {
        if (state.user) {
          localStorage.setItem('user', JSON.stringify(state.user));  // 保存用户信息到 localStorage
        } else {
          localStorage.removeItem('user');  // 如果用户退出，移除用户信息
        }
      });
    },
  ],
});
