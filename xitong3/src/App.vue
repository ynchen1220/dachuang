<!-- <template>
  <router-view></router-view>
</template>

<script>
</script>

<style>
</style> -->
<template>
  <div id="app">
    <!-- <div class="navbar">
      <ul>
        <li><router-link to="/home">首页</router-link></li>
        <li><router-link to="/about">AI问答</router-link></li>
        <li><router-link to="/search">知识检索</router-link></li>
        <li><router-link to="/">辅助诊断</router-link></li>
      </ul>
    </div> -->
    <router-view></router-view> <!-- 确保这里有 router-view -->
  </div>
</template>

<style>
/* 样式保持不变 */
.app{
  align-items: center; /* 水平居中 */
  justify-content: center; /* 垂直居中 */
}
.navbar {
  position: fixed;
  top: 0;
  left:-10px;
  width: 100vw;
  height:80px;
  background-color:rgba(218, 235, 251, 0.497);
  z-index: 999;
}

.navbar ul {
  list-style-type: none;
  display: flex;
  justify-content: center;
}

.navbar ul li {
  position: relative;
  padding-left:50px;
  padding-top:5px;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
.navbar a {
  text-decoration: none;
  color: black; /* 设置初始颜色 */
  padding: 8px 16px;
}

.navbar a:visited {
  color: black; /* 点击后仍保持黑色 */
}

.navbar a:hover {
  background-color:rgba(240, 248, 255, 0.599); /* 悬停时变化 */
}

.navbar a:active,
.navbar a:focus {
  color: black; /* 点击或聚焦时保持不变 */
}

</style>

<!-- <template>
  <div class="navbar">
    <ul>
      <li>
        <router-link to="/about">首页</router-link>
      </li>
      <li>
        <router-link to="/ai">AI问答</router-link>
      </li>
      <li>
        <router-link to="/search">知识检索</router-link>
      </li>
      <li>
        <router-link to="/login">登录|注册</router-link>
      </li>
    </ul>
  </div>
</template>

<style>
.navbar {
  background-color: #333;
  padding: 10px;
}

.navbar ul {
  list-style-type: none;
  display: flex;
  justify-content: space-around;
}

.navbar li {
  color: white;
}

.navbar a {
  text-decoration: none;
  color: white;
  padding: 8px 16px;
}

.navbar a:hover {
  background-color: #555;
}
</style> -->

<!-- <template>
  <div class="navbar">
    <ul>
      <li>
        <router-link to="/HelloWorld">首页</router-link> 
      </li>
      <li>
        AI问答
      </li>
      <li>
        <router-link to="/Searchview">知识检索</router-link>
      </li>
      <li>
        <router-link to="/denglu">登录|注册</router-link> 
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      dropdowns: {
        home: false,
        diagnosis: false,
        qa: false
      }
    }
  },
  methods: {
    showDropdown(menu) {
      this.$set(this.dropdowns, menu, true);
    },
    hideDropdown(menu) {
      this.$set(this.dropdowns, menu, false);
    },
  }
}
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left:-10px;
  width: 1399px;
  height:70px;
  background-color:rgba(218, 235, 251, 0.497);
  z-index: 999;
}

.navbar ul {
  list-style-type: none;
  display: flex;
  justify-content: center;
}

.navbar ul li {
  position: relative;
  padding-left:50px;
  padding-top:5px;
  cursor: pointer;
}

</style> -->