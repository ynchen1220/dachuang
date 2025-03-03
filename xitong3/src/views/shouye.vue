<template>
    <div class="denglu">
          <div class="box4">
              <h1>用人工智能守护生命健康</h1>
          </div>
          <div class="box5" @click="navigateToLog">
            <p>我是医生</p>
          </div>
          <div class="box6" @click="navigateToLog2">
              <p>我是患者</p>
          </div>
      </div>
  </template>
  
  <script>
  export default {
    methods: {
    navigateToLog2(){
        this.$router.push('/login2');
    },
    navigateToLog() {
      this.$router.push('/login');
    }
  }
  }
  </script>
  
  
  <style scoped lang="scss">
  .denglu {
    position:relative;
      background-color: aliceblue;
      width: 100vw;
      height: 800px;
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
    top:160px;
    border: 2px solid white; 
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  }
  .box4 h1{
    position:relative;
    text-align: center;
    // left:265px;
     top:30px;
  }
  
  .box5 {
    position:relative;
    height:200px;
    width:200px;
    left:400px;
    top:-370px;
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
    top:-770px;
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
  