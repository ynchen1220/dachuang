<!-- <template>
	<div class="login-register">
		<div class="contain">
			<div class="big-box" :class="{active:isLogin}">
				<div class="big-contain" key="bigContainLogin" v-if="isLogin">
					
					<div class="btitle">用户端账户登录</div>
					<div class="bform">
						<input type="email" placeholder="邮箱" v-model="form.useremail">
						<input type="password" placeholder="密码" v-model="form.userpwd">
						<span class="errTips" v-if="emailError">* 邮箱或密码填写错误 *</span>
					</div>
					<button class="bbutton" @click="login">登录</button>
				</div>

				<div class="big-contain" key="bigContainRegister" v-else>
					<div class="btitle">创建账户</div>
					<div class="bform">
						<input type="text" placeholder="用户名" v-model="form.username">
						<input type="email" placeholder="邮箱" v-model="form.useremail">
						<span class="errTips" v-if="existed">邮箱已被注册！</span>
						<input type="password" placeholder="密码" v-model="form.userpwd">
					</div>
					<button class="bbutton" @click="register">注册</button>
				</div>
			</div>

			<div class="small-box" :class="{active:isLogin}">
				<div class="small-contain" key="smallContainRegister" v-if="isLogin">
					<div class="stitle">你好!</div>
					<p class="scontent">开始注册，和我们一起探索</p>
					<button class="sbutton" @click="changeType">注册</button>
				</div>
				<div class="small-contain" key="smallContainLogin" v-else>
					<div class="stitle">欢迎回来!</div>
					<p class="scontent">请登录你的账户</p>
					<button class="sbutton" @click="changeType">登录</button>
				</div>
			</div>
		</div>
	</div>
    
  
	
</template>

<script>
	export default{
		name:'login-register',
		data(){
			return {
				isLogin:false,
				emailError: false,
				existed: false,
				form:{
					username:'',
					useremail:'',
					userpwd:''
				}
			}
		},
		methods:{
			changeType() {
				this.isLogin = !this.isLogin
				this.form.username = ''
				this.form.useremail = ''
				this.form.userpwd = ''
			},
			login() {
				const self = this;
				if (self.form.useremail != "" && self.form.userpwd != "") {
					this.$axios({
						method:'post',
						headers: {
                            "Content-Type": "application/x-www-form-urlencoded" 
						},
						url: '/login/',
						data: {
							email: self.form.useremail,
							password: self.form.userpwd
						}
					})
					.then( res => {
						switch(res.data){
							case 'y': 
								alert("登录成功")
								this.$router.push('/home');
								//导航的登录注册消失
								//导航底侧显示退出登录
								break;
							case 'n':
								this.emailError = true;
								break;
						}
					})
					.catch( err => {
						console.log(err);
					})
				} else{
					alert("填写不能为空！");
				}
			},
			register(){
				const self = this;
				if(self.form.username != "" && self.form.useremail != "" && self.form.userpwd != ""){
					this.$axios({
						method:'post',
						url: '/register/',
						headers: {
                                   "Content-Type": "application/x-www-form-urlencoded"
                         },
						data: {
							username: self.form.username,
							email: self.form.useremail,
							password: self.form.userpwd
						}
					})
					.then( res => {
						switch(res.data){
							case 'y':
								alert("注册成功！");
								this.existed = false;
								break;
							case 'n':
								alert("注册失败！");
								this.existed = true;
								break;
						}
					})
					.catch( err => {
						console.log(err);
					})
				} else {
					alert("填写不能为空！");
				}
			}
		}
	}
</script>

<style scoped="scoped">
	.login-register{
		width: 100vw;
		height: 100vh;
		box-sizing: border-box;
		background-color:aliceblue;
	}
	.contain{
		width: 60%;
		height: 60%;
		position: relative;
		top: 50%;
		left: 50%;
		transform: translate(-50%,-50%);
		background-color: #fff;
		border-radius: 20px;
		box-shadow: 0 0 3px #f0f0f0,
					0 0 6px #f0f0f0;
	}
	.big-box{
		width: 70%;
		height: 100%;
		position: absolute;
		top: 0;
		left: 30%;
		transform: translateX(0%);
		transition: all 1s;
	}
	.big-contain{
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	.btitle{
		font-size: 1.5em;
		font-weight: bold;
		color: rgb(57, 99, 176);
	}
	.bform{
		width: 100%;
		height: 40%;
		padding: 2em 0;
		display: flex;
		flex-direction: column;
		justify-content: space-around;
		align-items: center;
	}
	.bform .errTips{
		display: block;
		width: 50%;
		text-align: left;
		color: red;
		font-size: 0.7em;
		margin-left: 1em;
	}
	.bform input{
		width: 50%;
		height: 30px;
		border: none;
		outline: none;
		border-radius: 10px;
		padding-left: 2em;
		background-color: #f0f0f0;
	}
	.bbutton{
		width: 20%;
		height: 40px;
		border-radius: 24px;
		border: none;
		outline: none;
		background-color: rgb(57, 63, 176);
		color: #fff;
		font-size: 0.9em;
		cursor: pointer;
	}
	.small-box{
		width: 30%;
		height: 100%;
		background: linear-gradient(135deg,rgb(75, 94, 187),rgb(31, 72, 187));
		position: absolute;
		top: 0;
		left: 0;
		transform: translateX(0%);
		transition: all 1s;
		border-top-left-radius: inherit;
		border-bottom-left-radius: inherit;
	}
	.small-contain{
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	.stitle{
		font-size: 1.5em;
		font-weight: bold;
		color: #fff;
	}
	.scontent{
		font-size: 0.8em;
		color: #fff;
		text-align: center;
		padding: 2em 4em;
		line-height: 1.7em;
	}
	.sbutton{
		width: 60%;
		height: 40px;
		border-radius: 24px;
		border: 1px solid #fff;
		outline: none;
		background-color: transparent;
		color: #fff;
		font-size: 0.9em;
		cursor: pointer;
	}
	
	.big-box.active{
		left: 0;
		transition: all 0.5s;
	}
	.small-box.active{
		left: 100%;
		border-top-left-radius: 0;
		border-bottom-left-radius: 0;
		border-top-right-radius: inherit;
		border-bottom-right-radius: inherit;
		transform: translateX(-100%);
		transition: all 1s;
	}
</style> -->
<template>
	<div class="login-container">
	  <div class="form-box">
		<div class="form-content">
		  <!-- 登录表单 -->
		  <form class="login-form" v-if="isLogin">
			<h2 class="title">患者登录</h2>
			
			<div class="input-group">
			  <div class="input-field">
				<i class="fas fa-envelope"></i>
				<input type="email" placeholder="邮箱地址" v-model="form.useremail">
			  </div>
			  
			  <div class="input-field">
				<i class="fas fa-lock"></i>
				<input type="password" placeholder="密码" v-model="form.userpwd">
			  </div>
			  
			  <div class="error-message" v-if="emailError">
				* 邮箱或密码填写错误
			  </div>
			</div>
  
			<button class="submit-btn" @click.prevent="login">
			  登录
			</button>
  
			<p class="toggle-text">
			  还没有账号？
			  <span @click="changeType">立即注册</span>
			</p>
		  </form>
  
		  <!-- 注册表单 -->
		  <form class="register-form" v-else>
			<h2 class="title">患者注册</h2>
			
			<div class="input-group">
			  <div class="input-field">
				<i class="fas fa-user"></i>
				<input type="text" placeholder="用户名" v-model="form.username">
			  </div>
  
			  <div class="input-field">
				<i class="fas fa-envelope"></i>
				<input type="email" placeholder="邮箱地址" v-model="form.useremail">
			  </div>
  
			  <div class="input-field">
				<i class="fas fa-lock"></i>
				<input type="password" placeholder="密码" v-model="form.userpwd">
			  </div>
  
			  <div class="input-field">
				<i class="fas fa-lock"></i>
				<input type="password" placeholder="确认密码" v-model="form.confirmPwd">
			  </div>
  
			  <div class="error-message" v-if="existed">
				* 该邮箱已被注册
			  </div>
			</div>
  
			<button class="submit-btn" @click.prevent="register">
			  注册
			</button>
  
			<p class="toggle-text">
			  已有账号？
			  <span @click="changeType">立即登录</span>
			</p>
		  </form>
		</div>
	  </div>
	</div>
  </template>
  
  <script>
  export default {
	name: 'patient-login-register',
	data() {
	  return {
		isLogin: true,
		emailError: false,
		existed: false,
		form: {
		  username: '',
		  useremail: '',
		  userpwd: '',
		  confirmPwd: ''
		}
	  }
	},
	methods: {
	  changeType() {
		this.isLogin = !this.isLogin
		this.form = {
		  username: '',
		  useremail: '',
		  userpwd: '',
		  confirmPwd: ''
		}
		this.emailError = false
		this.existed = false
	  },
	  login() {
		// 使用原有的登录逻辑，但需要添加用户类型标识
		const self = this
		if (self.form.useremail && self.form.userpwd) {
		  this.$axios({
			method: 'post',
			headers: {
			  "Content-Type": "application/x-www-form-urlencoded"
			},
			url: '/patientlogin/',
			data: {
			  email: self.form.useremail,
			  password: self.form.userpwd,
			  userType: 'patient' // 添加用户类型标识
			}
		  })
		  .then(res => {
			if (res.data === 'y') {
			  alert("登录成功")
			  this.$router.push('/home')
			} else {
			  this.emailError = true
			}
		  })
		  .catch(err => {
			console.log(err)
		  })
		} else {
		  alert("填写不能为空！")
		}
	  },
	  register() {
		// 验证表单
		if (!this.validateForm()) {
		  return
		}
  
		const self = this
		this.$axios({
		  method: 'post',
		  url: '/patientregister/',
		  headers: {
			"Content-Type": "application/x-www-form-urlencoded"
		  },
		  data: {
			username: self.form.username,
			email: self.form.useremail,
			password: self.form.userpwd,
			userType: 'patient' // 添加用户类型标识
		  }
		})
		.then(res => {
		  if (res.data === 'y') {
			alert("注册成功！")
			this.existed = false
			this.isLogin = true
			this.emailError = false
			this.form = {
			  username: '',
			  useremail: '',
			  userpwd: '',
			  confirmPwd: ''
			}
		  } else {
			this.existed = true
		  }
		})
		.catch(err => {
		  console.log(err)
		})
	  },
	  validateForm() {
		if (!this.form.username || !this.form.useremail || !this.form.userpwd || !this.form.confirmPwd) {
		  alert("填写不能为空！")
		  return false
		}
  
		// 验证邮箱格式
		const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
		if (!emailRegex.test(this.form.useremail)) {
		  alert('请输入有效的邮箱地址')
		  return false
		}
  
		// 验证密码长度
		if (this.form.userpwd.length < 6) {
		  alert('密码长度至少为6位')
		  return false
		}
  
		// 验证两次密码是否一致
		if (this.form.userpwd !== this.form.confirmPwd) {
		  alert('两次输入的密码不一致')
		  return false
		}
  
		return true
	  }
	}
  }
  </script>
  
  <!-- 使用与 DoctorLog.vue 相同的样式，但移除不需要的部分 -->
  <style scoped>
  .login-container {
	min-height: 100vh;
	display: flex;
	align-items: center;
	justify-content: center;
	background: linear-gradient(120deg, #e0f2f1 0%, #1976D2 100%);
	font-family: 'Roboto', sans-serif;
	padding: 20px;
  }
  
  .form-box {
	background: rgba(255, 255, 255, 0.97);
	border-radius: 24px;
	box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
	overflow: hidden;
	width: 100%;
	max-width: 600px;
	padding: 40px;
	box-sizing: border-box;
	backdrop-filter: blur(10px);
  }
  
  .title {
	color: #1565C0;
	font-size: 2em;
	font-weight: 600;
	text-align: center;
	margin-bottom: 30px;
	letter-spacing: 0.5px;
	text-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
  }
  
  .input-group {
	width: 100%;
	margin-bottom: 20px;
	box-sizing: border-box;
  }
  
  .input-field {
	position: relative;
	width: 100%;
	margin-bottom: 20px;
	box-sizing: border-box;
  }
  
  .input-field input {
	width: 100%;
	padding: 14px 14px 14px 45px;
	border: 2px solid #E3F2FD;
	border-radius: 12px;
	font-size: 15px;
	color: #2c3e50;
	transition: all 0.3s ease;
	box-sizing: border-box;
	outline: none;
	background: rgba(255, 255, 255, 0.9);
  }
  
  .input-field input::placeholder {
	color: #B0BEC5;
	font-size: 14px;
	transition: all 0.3s ease;
  }
  
  .input-field input:focus::placeholder {
	opacity: 0;
  }
  
  .input-field i {
	position: absolute;
	left: 15px;
	top: 50%;
	transform: translateY(-50%);
	font-size: 18px;
	color: #90A4AE;
	transition: all 0.3s ease;
  }
  
  .input-field input:focus {
	border-color: #1976D2;
	box-shadow: 0 0 0 4px rgba(25, 118, 210, 0.1);
	transform: translateY(-1px);
  }
  
  .input-field input:focus + i {
	color: #1976D2;
  }
  
  .submit-btn {
	width: 100%;
	padding: 12px;
	border: none;
	border-radius: 8px;
	background: linear-gradient(135deg, #1976D2, #1565C0);
	color: white;
	font-size: 14px;
	font-weight: 600;
	text-transform: uppercase;
	letter-spacing: 1px;
	cursor: pointer;
	transition: all 0.3s ease;
	box-shadow: 0 4px 15px rgba(25, 118, 210, 0.2);
  }
  
  .submit-btn:hover {
	background: linear-gradient(135deg, #1E88E5, #1976D2);
	transform: translateY(-2px);
	box-shadow: 0 6px 20px rgba(25, 118, 210, 0.3);
  }
  
  .error-message {
	color: #f44336;
	font-size: 14px;
	margin-top: 8px;
	text-align: left;
	padding-left: 15px;
  }
  
  .toggle-text {
	text-align: center;
	color: #90A4AE;
	font-size: 15px;
	margin-top: 25px;
  }
  
  .toggle-text span {
	color: #1976D2;
	cursor: pointer;
	font-weight: 500;
	margin-left: 5px;
  }
  
  .toggle-text span:hover {
	text-decoration: underline;
  }
  
  .login-form,
  .register-form {
	animation: fadeIn 0.6s ease-out;
  }
  
  @keyframes fadeIn {
	from {
	  opacity: 0;
	  transform: translateY(20px);
	}
	to {
	  opacity: 1;
	  transform: translateY(0);
	}
  }
  
  /* 修改登录表单的输入框布局 */
  .login-form .input-group {
	display: flex;
	flex-direction: column;
	gap: 20px;
	width: 100%;
	margin-bottom: 20px;
  }
  
  .login-form .input-field {
	width: 100%;
	margin-bottom: 0;
  }
  </style> 