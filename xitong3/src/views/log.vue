<!-- <template>
	<div class="login-register">
		<div class="contain">
			<div class="big-box" :class="{active:isLogin}">
				<div class="big-contain" key="bigContainLogin" v-if="isLogin">
					
					<div class="btitle">医生端账户登录</div>
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
								this.$router.push('/home2');
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
		<div class="form-box" :style="{ maxWidth: isLogin ? '420px' : '90%' }">
			<div class="form-content">
				<!-- 登录表单 -->
				<form class="login-form" v-if="isLogin">
					<h2 class="title">账户登录</h2>
					
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

				<!-- 注册表单改为分步式 -->
				<form class="register-form" v-else>
					<h2 class="title">{{ steps[currentStep].title }}</h2>
					
					<!-- 步骤指示器 -->
					<div class="step-indicator">
						<div v-for="(step, index) in steps" 
							 :key="index"
							 :class="['step', { active: index === currentStep, completed: index < currentStep }]">
							{{ index + 1 }}
						</div>
					</div>

					<!-- 第一步：基本信息 -->
					<div class="step-content" v-if="currentStep === 0">
						<div class="input-group">
							<div class="input-field">
								<i class="fas fa-user"></i>
								<input type="text" placeholder="姓名" v-model="form.username">
							</div>

							<div class="radio-group">
								<label>性别：</label>
								<label><input type="radio" v-model="form.gender" value="male">男</label>
								<label><input type="radio" v-model="form.gender" value="female">女</label>
							</div>

							<div class="input-field">
								<i class="fas fa-calendar"></i>
								<input type="date" placeholder="出生日期" v-model="form.birthdate">
							</div>

							<div class="input-field">
								<i class="fas fa-phone"></i>
								<input type="tel" placeholder="联系电话" v-model="form.phone">
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
						</div>
					</div>

					<!-- 第二步：学历与专业背景 -->
					<div class="step-content" v-if="currentStep === 1">
						<div class="input-group">
							<div class="select-field">
								<i class="fas fa-graduation-cap"></i>
								<select v-model="form.education" :class="{ 'selected': form.education }">
									<option value="">选择最高学历</option>
									<option value="bachelor">学士</option>
									<option value="master">硕士</option>
									<option value="doctor">博士</option>
								</select>
							</div>
							
						

							<div class="input-field">
								<i class="fas fa-university"></i>
								<input type="text" placeholder="毕业院校" v-model="form.school">
							</div>

							<div class="input-field">
								<i class="fas fa-book-medical"></i>
								<input type="text" placeholder="专业" v-model="form.major">
							</div>

							<div class="select-field">
								<i class="fas fa-clock"></i>
								<select v-model="form.experience" :class="{ 'selected': form.experience }">
									<option value="">选择从业经验</option>
									<option value="1-3">1-3年</option>
									<option value="3-5">3-5年</option>
									<option value="5-10">5-10年</option>
									<option value="10+">10年以上</option>
								</select>
							</div>
						</div>
					</div>

					<!-- 第三步：执业信息 -->
					<div class="step-content" v-if="currentStep === 2">
						<div class="input-group">
							<div class="input-field">
								<i class="fas fa-id-card"></i>
								<input type="text" placeholder="执业医师资格证号码" v-model="form.licenseNo">
							</div>

							<div class="file-field">
								<label>
									<i class="fas fa-upload"></i>
									<span>上传资格证扫描件</span>
									<input type="file" @change="handleFileUpload($event, 'license')" accept=".pdf,.jpg,.jpeg,.png">
								</label>
								<div class="file-preview" v-if="form.licenseFile">
									<div class="preview-info">
										<span class="file-name">{{ form.licenseFile.name }}</span>
										<i class="fas fa-times" @click="removeFile('license')"></i>
									</div>
									<img v-if="previewUrl && isImageFile(form.licenseFile)" :src="previewUrl" class="image-preview">
								</div>
							</div>

							<div class="select-field">
								<i class="fas fa-user-md"></i>
								<select v-model="form.title" :class="{ 'selected': form.title }">
									<option value="">选择专业职称</option>
									<option value="resident">住院医师</option>
									<option value="attending">主治医师</option>
									<option value="associate">副主任医师</option>
									<option value="chief">主任医师</option>
								</select>
							</div>

							<div class="department-select">
								<label class="department-label">选择执业科室</label>
								<div class="department-options">
									<label class="department-item" v-for="dept in departments" :key="dept.value">
										<input type="checkbox" 
												:value="dept.value" 
												v-model="form.departments">
										<span>{{ dept.label }}</span>
									</label>
								</div>
							</div>

							<div class="input-field full-width">
								<i class="fas fa-hospital"></i>
								<input type="text" placeholder="注册执业地点" v-model="form.workplace">
							</div>
						</div>
					</div>

					<!-- 导航按钮 -->
					<div class="form-navigation">
						<button type="button" 
								class="nav-btn back" 
								v-if="currentStep > 0"
								@click="prevStep">
								上一步
							</button>
						
						<div class="right-buttons">
							<button type="button" 
									class="nav-btn next" 
									v-if="currentStep < steps.length - 1"
									@click="nextStep">
									下一步
								</button>
							
							<button class="submit-btn" 
									v-if="currentStep === steps.length - 1"
									@click.prevent="register">
									提交注册
								</button>
						</div>
					</div>

					<div class="error-message" v-if="existed">
						* 该邮箱已被注册
					</div>

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
	export default{
		name:'login-register',
		data(){
			return {
				isLogin:true,
				emailError: false,
				existed: false,
				currentStep: 0,
				steps: [
					{ title: '基本信息' },
					{ title: '学历背景' },
					{ title: '执业信息' }
				],
				form:{
					username:'',
					useremail:'',
					userpwd:'',
					confirmPwd:'',
					gender:'',
					birthdate:'',
					phone:'',
					education:'',
					school:'',
					major:'',
					experience:'',
					licenseNo:'',
					licenseFile: null,
					title:'',
					departments:[],
					workplace:''
				},
				departments: [
					{ label: '内科', value: 'internal' },
					{ label: '外科', value: 'surgery' },
					{ label: '儿科', value: 'pediatrics' },
					{ label: '妇产科', value: 'gynecology' },
					{ label: '骨科', value: 'orthopedics' },
					{ label: '眼科', value: 'ophthalmology' },
					{ label: '耳鼻喉科', value: 'ent' },
					{ label: '口腔科', value: 'dental' },
					{ label: '皮肤科', value: 'dermatology' },
					{ label: '其他', value: 'other' }
				],
				previewUrl: null,
			}
		},
		methods:{
			changeType() {
				this.isLogin = !this.isLogin
				if (!this.isLogin) {
					this.resetForm()
				} else {
					this.form.useremail = ''
					this.form.userpwd = ''
				}
				this.emailError = false  // 重置错误状态
				this.existed = false
			},
			login() {
				const self = this;
				if (self.form.useremail != "" && self.form.userpwd != "") {
					this.$axios({
						method:'post',
								headers: {
									"Content-Type": "application/x-www-form-urlencoded" 
								},
								url: '/doctorlogin/',
								data: {
									email: self.form.useremail,
									password: self.form.userpwd
								}
							})
							.then( res => {
								switch(res.data){
									case 'y': 
										alert("登录成功")
										this.$router.push('/home2');
										//导航的登录注册消失
										//导航底侧显示退出登录
										break;
									case 'n':
									    alert("登录失败")
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
			register() {
				// 首先验证当前步骤
				if (!this.validateCurrentStep()) {
					return;
				}

				// 创建 FormData 对象来处理文件上传
				const formData = new FormData();
				
				// 添加基本信息
				formData.append('username', this.form.username);
				formData.append('email', this.form.useremail);
				formData.append('password', this.form.userpwd);
				formData.append('gender', this.form.gender);
				formData.append('birth_date', this.form.birthdate);
				formData.append('phone', this.form.phone);
				
				// 添加学历背景
				formData.append('education', this.form.education);
				formData.append('university', this.form.school);
				formData.append('major', this.form.major);
				formData.append('experience', this.form.experience);
				
				// 添加执业信息
				formData.append('license_number', this.form.licenseNo);
				formData.append('title', this.form.title);
				formData.append('departments', JSON.stringify(this.form.departments));
				formData.append('workplace', this.form.workplace);
				
				// 添加资格证文件
				if (this.form.licenseFile) {
					formData.append('license_image', this.form.licenseFile);
				}
				
				// 添加用户类型标识
				formData.append('userType', 'doctor');

				// 发送求
				this.$axios({
					method: 'post',
					url: '/doctorregister/',  // 医生的注册接口
					headers: {
						'Content-Type': 'multipart/form-data'  // 修改Content-Type以支持文件上传
					},
					data: formData
				})
				.then(res => {
					if (res.data === 'y') {
						alert("注册成功,请等待管理员审核")
						this.existed = false
						this.isLogin = true
						this.emailError = false  // 重置错误状态
						// 重置表单
						this.resetForm()
					} else if (res.data === 'email_exists') {
						this.existed = true
					} else {
						alert("注册失败请检查填写的信息")
					}
				})
				.catch(err => {
					console.log(err);
					alert("注册失败，请后重试");
				});
			},
			nextStep() {
				if (this.validateCurrentStep()) {
					this.currentStep++
				}
			},
			prevStep() {
				this.currentStep--
			},
			validateCurrentStep() {
				// 根不同步骤进行相应的表单验证
				switch(this.currentStep) {
					case 0:
						return this.validateBasicInfo()
					case 1:
						return this.validateEducation()
					case 2:
						return this.validateLicense()
					default:
						return true
				}
			},
			handleFileUpload(event, type) {
				const file = event.target.files[0]
				if (file) {
					this.form[`${type}File`] = file
					
					if (this.isImageFile(file)) {
						this.createPreviewUrl(file)
					}
				}
			},
			createPreviewUrl(file) {
				if (this.previewUrl) {
					URL.revokeObjectURL(this.previewUrl)
				}
				this.previewUrl = URL.createObjectURL(file)
			},
			isImageFile(file) {
				return file.type.startsWith('image/')
			},
			removeFile(type) {
				this.form[`${type}File`] = null
				if (this.previewUrl) {
					URL.revokeObjectURL(this.previewUrl)
					this.previewUrl = null
				}
			},
			// 验证基本信息
			validateBasicInfo() {
				const { username, gender, birthdate, phone, useremail, userpwd, confirmPwd } = this.form
				
				// 检查必填项是否为空
				if (!username || !gender || !birthdate || !phone || !useremail || !userpwd || !confirmPwd) {
					alert('请填写所有必填项')
					return false
				}

				// 验证邮箱格式
				const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
				if (!emailRegex.test(useremail)) {
					alert('请输入有效的邮箱地址')
					return false
				}

				// 验证手机号格式
				const phoneRegex = /^1[3-9]\d{9}$/
				if (!phoneRegex.test(phone)) {
					alert('请输入有效的手机号码')
					return false
				}

				// 验证密码长度
				if (userpwd.length < 6) {
					alert('密码长度至少为6')
					return false
				}

				// 验证两次密码是否一致
				if (userpwd !== confirmPwd) {
					alert('两次输入的密码不一致')
					return false
				}

				return true
			},

			// 证学历信息
			validateEducation() {
				const { education, school, major, experience } = this.form

				// 检查必填
				if (!education || !school || !major || !experience) {
					alert('请填写所有必填项')
					return false
				}

				return true
			},

			// 验证执业信息
			validateLicense() {
				const { licenseNo, licenseFile, title, departments, workplace } = this.form

				// 检查必填项
				if (!licenseNo || !title || !workplace || departments.length === 0) {
					alert('请填写所有必填项')
					return false
				}

				// 验证执业证号格式（示例格式，需要根据实际情况调整）
				const licenseRegex = /^\d{6,}$/
				if (!licenseRegex.test(licenseNo)) {
					alert('请输入有效的执业医师资格证号码')
					return false
				}

				// 检查是否上传了资格证文件
				if (!licenseFile) {
					alert('请上传资格证扫描件')
					return false
				}

				return true
			},

			// 重置表单数据
			resetForm() {
				this.form = {
					username: '',
					useremail: '',
					userpwd: '',
					confirmPwd: '',
					gender: '',
					birthdate: '',
					phone: '',
					education: '',
					school: '',
					major: '',
					experience: '',
					licenseNo: '',
					licenseFile: null,
					title: '',
					departments: [],
					workplace: ''
				}
				this.currentStep = 0
			}
		},
		beforeDestroy() {
			if (this.previewUrl) {
				URL.revokeObjectURL(this.previewUrl)
			}
		}
	}
</script>

<style scoped>
	.login-container {
		min-height: 100vh;
		display: flex;
		align-items: center;
		justify-content: center;
		background-color:  rgb(230, 241, 250);
		background-size: cover;
		background-position: center;
		background-repeat: no-repeat;
		font-family: 'Roboto', sans-serif;
		padding: 20px;
	}

	.form-box {
		background: rgba(255, 255, 255, 0.97);
		border-radius: 24px;
		box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
		overflow: hidden;
		width: 100%;
		padding: 40px;
		box-sizing: border-box;
		backdrop-filter: blur(10px);
	}

	.form-box.login-form {
		max-width: 420px;
	}

	.form-box.register-form {
		max-width: 90%;
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
		display: flex;
		flex-direction: column;
		gap: 25px;
		width: 100%;
		margin-bottom: 30px;
		box-sizing: border-box;
	}

	.input-field,
	.select-field {
		width: 100%;
		margin: 0;
		position: relative;
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

	.social-login {
		margin-top: 35px;
		text-align: center;
	}

	.social-login p {
		color: #90A4AE;
		margin-bottom: 15px;
		font-size: 14px;
	}

	.social-icons {
		display: flex;
		justify-content: center;
		gap: 15px;
		margin-bottom: 25px;
	}

	.social-icon {
		width: 40px;
		height: 40px;
		border-radius: 50%;
		border: 2px solid #E3F2FD;
		display: flex;
		align-items: center;
		justify-content: center;
		color: #1976D2;
			transition: all 0.3s ease;
		background: white;
		box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
	}

	.social-icon:hover {
		background: #E3F2FD;
		transform: translateY(-2px);
		box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
		color: #1565C0;
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

	/* 添加新的样式 */
	.step-indicator {
		display: flex;
		justify-content: center;
		margin: 0 auto 35px;
		max-width: 400px;
	}

	.step {
		width: 35px;
		height: 35px;
		border-radius: 50%;
		background: #E3F2FD;
		color: #1976D2;
		display: flex;
		align-items: center;
		justify-content: center;
		margin: 0 20px;
		position: relative;
		font-weight: 600;
		transition: all 0.3s ease;
		box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
	}

	.step.active {
		background: #1976D2;
		color: white;
		transform: scale(1.1);
		box-shadow: 0 4px 10px rgba(25, 118, 210, 0.3);
	}

	.step.completed {
		background: #4CAF50;
		color: white;
	}

	.step:not(:last-child)::after {
			content: '';
			position: absolute;
			width: 120%;
			height: 3px;
			background: #E3F2FD;
			left: 100%;
			top: 50%;
			transform: translateY(-50%);
	}

	.file-field {
		margin: 0;
		padding: 10px 0;
	}

	.file-field label {
		display: inline-flex;
		align-items: center;
		gap: 8px;
		padding: 12px 20px;
		background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
		color: #1976D2;
		border-radius: 8px;
		cursor: pointer;
		transition: all 0.3s ease;
		font-weight: 500;
		box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
	}

	.file-field label:hover {
		background: linear-gradient(135deg, #BBDEFB, #90CAF9);
		transform: translateY(-1px);
		box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
	}

	.file-field input[type="file"] {
		display: none;
	}

	.file-name {
		margin-left: 10px;
		color: #666;
	}

	.select-field {
		position: relative;
	}


	.select-field select {
		width: 100%;
		padding: 14px 14px 14px 45px;
		border: 2px solid #E3F2FD;
		border-radius: 12px;
		font-size: 15px;
		color: #B0BEC5;  /* 默认为灰色 */
		background: white;
		appearance: none;
		cursor: pointer;
		transition: all 0.3s ease;
	}

	/* 当有选择值时的样式 */
	.select-field select.selected {
		color: #2c3e50;  /* 选中后显示黑色 */
	}

	/* 下拉选项的样式 */
	.select-field select option {
		color: #2c3e50;  /* 选项始终显示黑色 */
	}

	/* 默认选项的样式 */
	.select-field select option[value=""] {
		color: #B0BEC5;  /* 默认选项显示灰色 */
	}

	.multi-select-field select {
		height: 100px;
	}

	.radio-group {
		margin: 0;
		padding: 10px 0;
		display: flex;
		align-items: center;
		gap: 25px;
	}

	.radio-group label:first-child {
		color: #2c3e50;
		margin-right: 15px;
	}

	.radio-group label {
		display: flex;
		align-items: center;
		gap: 8px;
		color: #2c3e50;
		font-size: 15px;
		cursor: pointer;
		white-space: nowrap;
	}

	.form-navigation {
		display: flex;
		justify-content: space-between;  /* 保持两端对齐 */
		margin-top: 30px;
		padding: 0 20px;
	}

	/* 添加一个包装器用于右侧按钮 */
	.form-navigation .right-buttons {
		display: flex;
		gap: 20px;  /* 按钮之间的间距 */
	}

	.nav-btn {
		padding: 12px 25px;
		border: none;
		border-radius: 8px;
		cursor: pointer;
		font-weight: 500;
		transition: all 0.3s ease;
		font-size: 15px;
		letter-spacing: 0.5px;
	}

	.nav-btn.back {
		background: #E3F2FD;
		color: #1976D2;
		white-space: nowrap;
		min-width: 80px;
		text-align: center;
	}

	.nav-btn.back:hover {
		background: #BBDEFB;
		transform: translateY(-1px);
	}

	.nav-btn.next {
		background: linear-gradient(135deg, #1976D2, #1565C0);
		color: white;
		box-shadow: 0 4px 15px rgba(25, 118, 210, 0.2);
	}

	.nav-btn.next:hover {
		background: linear-gradient(135deg, #1E88E5, #1976D2);
		transform: translateY(-1px);
		box-shadow: 0 6px 20px rgba(25, 118, 210, 0.3);
	}

	/* 添加响应式滚动 */
	.step-content {
		max-height: 65vh;
		overflow-y: auto;
		padding: 10px 15px;
		margin: 0 -15px;
	}

	.step-content::-webkit-scrollbar {
		width: 5px;
	}

	.step-content::-webkit-scrollbar-track {
		background: #F5F7FA;
	}

	.step-content::-webkit-scrollbar-thumb {
		background: #CFD8DC;
		border-radius: 3px;
	}

	.step-content::-webkit-scrollbar-thumb:hover {
		background: #B0BEC5;
	}

	.department-select {
		margin: 0;
		padding: 10px 0;
	}

	.department-label {
		display: block;
		color: #2c3e50;
		font-size: 15px;
		margin-bottom: 10px;
		font-weight: 500;
	}

	.department-options {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 15px;
		background: #F5F7FA;
		padding: 15px;
		border-radius: 12px;
		border: 2px solid #E3F2FD;
	}

	.department-item {
		display: flex;
		align-items: center;
		gap: 8px;
		cursor: pointer;
		padding: 8px;
		border-radius: 6px;
		transition: all 0.2s ease;
	}

	.department-item:hover {
		background: #E3F2FD;
	}

	.department-item input[type="checkbox"] {
		width: 18px;
		height: 18px;
		border: 2px solid #1976D2;
		border-radius: 4px;
		cursor: pointer;
		accent-color: #1976D2;
	}

	.department-item span {
		color: #2c3e50;
		font-size: 14px;
	}

	.file-preview {
		margin-top: 15px;
		padding: 10px;
		background: #F5F7FA;
		border-radius: 8px;
		border: 2px solid #E3F2FD;
	}

	.preview-info {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 10px;
	}

	.file-name {
		color: #2c3e50;
		font-size: 14px;
		word-break: break-all;
		margin-right: 10px;
	}

	.preview-info i {
		color: #90A4AE;
		cursor: pointer;
		padding: 5px;
		transition: all 0.2s ease;
	}

	.preview-info i:hover {
		color: #f44336;
	}

	.image-preview {
		max-width: 100%;
		max-height: 200px;
		border-radius: 4px;
		display: block;
		margin: 10px auto 0;
	}
</style>

