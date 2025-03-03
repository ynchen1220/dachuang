<template>
    <!-- <div class="navbar">
      <ul>
        <li>
          首页
        </li>
        <li>
          辅助诊断
        </li>
        <li>
          AI问答
        </li>
        <li>
          知识检索
        </li>
        <li>
          <router-link to="/denglu">登录|注册</router-link> 
        </li>
      </ul>
    </div> -->
    <div id="app">
      <div class="navbar">
        <ul>
          <li><router-link to="/home2">首页</router-link></li>
          <li><router-link to="/about2">AI问答</router-link></li>
          <li><router-link to="/search2">知识检索</router-link></li>
          <li><router-link to="/" class="logout-button">退出登录</router-link></li>
          <!-- <li><router-link to="/login">登录|注册</router-link></li> -->
        </ul>
      </div>
          <div class="SwiperBox" @mouseenter="MouseFun('移入')" @mouseleave="MouseFun('移出')">
              <!-- 图片 -->
              <img :class="['imgCss',ShowImg==index?'ShowCss':'']"
              :src="item.imgUrl" v-for="(item,index) in imgList" :key="index" />
              <div v-if="ShowImg === 0" class="textOverlay">
                  <h1>用人工智能<br>守护生命健康</h1>
                  <p>PROTECT LIFE AND HEALTH WITH AI</p>
                  <!-- <button :type="type" :disabled="disabled" @click="navigateToSearch">
                      <slot>{{ label }}</slot>
                      <p>点击体验</p>
                  </button> -->
              </div>
          </div>
    </div>
    <div id="app1">
          <div class="SwiperBox1">
          </div>
          <div class="overlayText">
              <h1>核心优势</h1>
              <p>促进医疗健康产业迅速发展</p>
              <h2>技术体系<br>依托多模态知识图谱，打造疾病风险预警模型，输入相关症状，<br>即可获得对应疾病风险</h2>
              <div class="button1">
                  <button :type="type" :disabled="disabled" @click="navigateToSearch">
                      <slot>{{ label }}</slot>
                      <p>点击体验</p>
                  </button>
              </div>
          </div>
      </div>
      <div class="jiansuo">
        <div class="box1">
            <h1>智慧AI问答，智慧知识检索</h1>
            <p>依托中国中医科学院数据库，构建知识图谱</p>
        </div>
        <div class="box2" @click="navigateToAIQanda">
          <p>AI问答</p>
        </div>
        <div class="box3" @click="navigateToSearch">
            <p>知识检索</p>
        </div>
    </div>
    <div class="denglu">
          <div class="box4">
              <h1>用人工智能守护生命健康</h1>
          </div>
          <div class="box5" @click="navigateToLog">
            <p>我是医生</p>
          </div>
          <div class="box6" @click="navigateToLog">
              <p>我是患者</p>
          </div>
      </div>
      <div class="bottombar">
          <h2>版权所有@陈嘉怡</h2>
          <p>联系方式:ynchen1220@bjfu.edu.cn</p>
      </div> 
  </template>
  
  <script>
  export default {
    name: 'HelloWorld',
    props: {
      msg: String
    },
    components: {},
    props: ['label', 'type', 'disabled'],
      emits: ['click'],
    //   methods: {
    //   onClick() {
    //     this.$emit('click');
    //   }
    // },
    data() {
      return {
        imgList: [
        {imgUrl:  require('@/assets/23.jpg') },
        {imgUrl:  require('@/assets/22.jpg') },
        {imgUrl:  require('@/assets/45.jpg')},
        ],
        ShowImg:0,  // 表示当前显示的图片
        flag:true, // 用来节流防止重复点击
        start:null, // 自动执行下一张定时器
      };
    },
    mounted() {
      this.setTimeoFun()
    },
    methods: {
      // 这里定义一个鼠标移入移出事件，鼠标悬停时停止自动轮播，鼠标移出则重新执行自动轮播
      MouseFun(type){// 停止定时器            // 重新执行定时器
        type=='移入'?clearTimeout(this.start):this.setTimeoFun()
      },
      setTimeoFun(){
          this.start = setInterval(()=>{
          this.NextFun()
        },2000)
      }, navigateToAIQanda() {
        this.$router.push('/about2');
    },navigateToSearch(){
        this.$router.push('/search2');
    },
    navigateToLog() {
      this.$router.push('/login2');
    },
      // 这里通过额外封装的节流函数触发 PrevFun() 和 NextFun(),以达到防止重复点击的效果
      throttle(fun) {
          if (this.flag) {
              this.flag = false;
              fun(); // 此为模板中传递进来的PrevFun()或NextFun()函数
            setTimeout(() => {
                  this.flag = true;
              }, 2000); // 节流间隔时间
          }
      },
      // 上一张
      PrevFun(){
        if(this.ShowImg!==0){
           this.ShowImg--
        }else{
           this.ShowImg=this.imgList.length-1
        }
      },
      // 下一张
      NextFun(){
        if(this.ShowImg!==this.imgList.length-1){
           this.ShowImg++
        }else{
           this.ShowImg=0
        }
      },
      onClick() {
        this.$emit('click');
      }
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped lang="scss">
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
  
  .SwiperBox {
      position: relative;
      width: 100vw;
      height: 720px;
      left:-7px;
      box-sizing: border-box;
      cursor: pointer;
      top:-10px;
    }
    /* 图片默认样式 */
    .imgCss {
      position: absolute;
      left: 0px;
      top: 0;
      width: 100%;
      height: 720px;
      opacity: 0;
      transition: 0.8s;  /* 淡入淡出过渡时间 */
    }
    /* 图片选中样式(继承上方默认样式) */
    .ShowCss {
      opacity: 1;
    }
    .textOverlay {
      position: absolute;
      top: 50%;
      left: 77%;
      transform: translate(-50%, -50%);
      color: rgb(0, 0, 0);
      font-size: 20px;
      padding: 10px;
      pointer-events: none; /* 防止文字层干扰点击事件 */
      transition: opacity 0.8s; /* 与图片过渡时间匹配 */
    }
    button{
      position: relative;
      height:30px;
      width:50px;
      padding: 30px 80px;
      border-radius: 20px;
      background-color: #3967ff;
      color: #fff;
      cursor: pointer;
      border: none;
    }
    button:hover {
    background-color: #0056b3;
  }
    button p{
      position: absolute; 
      top:-2px;
    left: 40px;  
    color:#fff; 
    font-size:20px;
    }
    
.navbar ul li .logout-button {
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
  transition: background-color 0.3s;
  position: relative;
  background-color: #3967ff;
  color: #fff;
  cursor: pointer;
  border: none;
}

.navbar ul li .logout-button:hover {
  background-color: #0056b3;
}
    .SwiperBox1 {
      position: relative;
      width: 100vw;
      height: 720px;
      margin-top:-10px;
      left:-7px;
      box-sizing: border-box;
      cursor: pointer;
      background-image: url('@/assets/56.jpg');
      background-size: cover; 
    }
  
    .imageContainer {
    position: relative;
  }
  
  .overlayText h1{
    position: absolute;
    left: 600px;   
    top:750px;
    color: rgb(0, 0, 0); 
  }
  .overlayText p{
    position: absolute;
    left: 570px;   
    top:820px;
    color: rgb(0, 0, 0); 
  }
  .overlayText h2{
    position: absolute;
    left: 70px;   
    top:950px;
    color: rgb(0, 0, 0); 
  }
  button {
    position: relative;
    padding: 30px 80px;
    border-radius: 20px;
    background-color: #3967ff;
    color: #fff;
    cursor: pointer;
    border: none;
  }
  button:hover {
    background-color: #0056b3;
  }
  .button1 {
    position: absolute; 
    top: 1100px;
    left: 100px;   
  }
  .button1 p{
    position: absolute; 
    top: -2px;
    left: 36px;  
    color:#fff; 
  }
  .jiansuo {
    position:relative;
      background-color: aliceblue;
      align-items: center;
      width: 100vw;
      height: 720px;
      left:-7px;
      top:-40px;
  }
  .box1 {
    position:relative;
    border-radius: 50px;
    background-color: rgb(229, 241, 252);
    width:900px;
    height:500px;
    left:250px;
    top:90px;
    border: 2px solid white; 
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  }
  .box1 h1{
    position:relative;
    text-align: center;
    // left:265px;
    top:20px;
  }
  .box1 p{
    position:relative;
    // left:295px;
    text-align: center;
    top:20px;
  }
  .box2 {
    position:relative;
    height:200px;
    width:200px;
    left:400px;
    top:-250px;
    background-image: url(@/assets/logo1.png);
  }
  .box2 p{
    position: relative;
    text-align: center;
    left:13px;
  }
  .box3 {
    position:relative;
    height:200px;
    width:200px;
    left:790px;
    top:-465px;
    background-image: url(@/assets/logo2.png);
  }
  .box3 p{
    position: relative;
    text-align: center;
    left:13px;
  }
  
  .box2:hover {
    transform: translateY(-10px); 
  }
  .box3:hover {
    transform: translateY(-10px); 
  }
  .denglu {
    position:relative;
      background-color: aliceblue;
      width: 100vw;
      height: 720px;
      left:-7px;
      top:-40px;
  }
  .box4 {
    position:relative;
    border-radius: 50px;
    background-color: rgb(229, 241, 252);
    width:900px;
    height:500px;
    left:250px;
    top:90px;
    border: 2px solid white; 
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  }
  .box4 h1{
    position:relative;
    text-align: center;
    // left:265px;
     top:20px;
  }
  
  .box5 {
    position:relative;
    height:200px;
    width:200px;
    left:400px;
    top:-450px;
    background-image: url(@/assets/logo3.png);
  }
  .box5 p{
    position: relative;
    text-align: center;
    margin-top:200px;
  }
  .box6 {
    position:relative;
    height:200px;
    width:150px;
    left:790px;
    top:-850px;
    background-image: url(@/assets/logo4.png);
    background-size: contain; /* 适应容器大小 */
    background-repeat: no-repeat; /* 防止重复显示 */
    background-position: center; /* 背景居中对齐 */
  }
  .box6 p{
    position: relative;
    text-align: center;
    margin-top:200px;
  }
  .box5:hover {
    transform: translateY(-10px); 
  }
  .box6:hover {
    transform: translateY(-10px); 
  }
  .bottombar{
      position: relative;
      left:-7px;
      width:100vw;
      height: 300px;
      margin-top:-60px;
      background-color: rgb(241, 248, 255);
  }
  .bottombar h2{
      position: relative;
      text-align: center;
      // left:580px;
      top:130px;
  }
  .bottombar p{
      position: relative;
      // left:550px;
      text-align: center;
      top:130px;
  }
  </style>
  