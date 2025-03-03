import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/home',
    name: 'home',
    component: () => import(/* webpackChunkName: "about" */ '../views/HomeView.vue')
  },
  {
    path: '/home2',
    name: 'home2',
    component: () => import(/* webpackChunkName: "about" */ '../views/Homeview2.vue')
  },
  {
    path:'/',
    name:'shouye',
    component: () => import(/* webpackChunkName: "about" */ '../views/shouye.vue')
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },{
    path: '/about2',
    name: 'about2',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView2.vue')
  },
  {
    path:'/search',
    name:'search',
    component: () => import(/* webpackChunkName: "about" */ '../views/SearchView.vue')
  },{
    path:'/login',
    name:'login',
    component: () => import(/* webpackChunkName: "about" */ '../views/log.vue')
  },{
    path:'/search2',
    name:'search2',
    component: () => import(/* webpackChunkName: "about" */ '../views/SearchView2.vue')
  },{
    path:'/login2',
    name:'login2',
    component: () => import(/* webpackChunkName: "about" */ '../views/log2.vue')
  },{
    path:'/user',
    name:'user',
    component: () => import(/* webpackChunkName: "about" */ '../views/usermanage.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

// import { ChatOpenAI } from "@langchain/openai";

// const model = new ChatOpenAI({
// });

// async function getAIResponse() {
//   try {
//     // 确保输入参数是一个字符串
//     const res = await model.call("写一首诗，限制20个字");
//     console.log("API response:", res);
//   } catch (error) {
//     console.error("Error calling API:", error);
//   }
// }

// getAIResponse();
