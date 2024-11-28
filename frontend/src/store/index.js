import { createStore } from 'vuex';  // 从 vuex 导入 createStore 方法

// 创建并导出 Vuex 存储实例
export default createStore({
  // 定义应用的状态
  state: {
    user: null,  // 默认没有用户信息，后续可以设置为登录的用户数据
  },

  // 定义 mutations，用于同步修改状态
  mutations: {
    // 修改 user 状态的 mutation 方法
    setUser(state, user) {
      state.user = user;  // 将 user 对象设置为状态中的 user
    },
  },

  // 定义 actions，用于处理异步操作
  actions: {
    // 异步获取用户数据
    fetchUser({ commit }) {
      axios.get('/users/')  // 发送 GET 请求到后端获取用户数据
        .then(response => {
          commit('setUser', response.data);  // 请求成功后，提交 mutation 修改用户信息
        });
    },
  },

  // 定义 getters，用于获取状态中的数据
  getters: {
    // 获取当前的用户信息
    getUser: (state) => state.user,  // 返回状态中的 user 值
  },
});
