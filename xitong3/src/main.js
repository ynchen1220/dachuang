import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

import ElementPlus from 'element-plus';
// import 'element-plus/dist/index.css';  // Element Plus 样式
import axios from 'axios';
import VueAxios from 'vue-axios';
import * as echarts from 'echarts';
import installElementPlus from './plugins/element'

// 创建应用
const app = createApp(App);

// 使用插件
app.use(store);
app.use(router);
app.use(ElementPlus);
app.use(VueAxios, axios);

// 设置 Axios 的基本 URL
axios.defaults.baseURL = 'http://127.0.0.1:8000/api';

// 将 ECharts 添加到 Vue 实例中
app.config.globalProperties.$echarts = echarts;
app.config.globalProperties.$axios = axios;

// 挂载应用
app.mount('#app');
