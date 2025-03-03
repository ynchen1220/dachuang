<template>
  <div class="navbar">
    <ul>
      <li><router-link to="/home2">首页</router-link></li>
      <li><router-link to="/about2">AI问答</router-link></li>
      <li><router-link to="/search2">知识检索</router-link></li>
      <li><router-link to="/" class="logout-button">退出登录</router-link></li>
    </ul>
  </div>
  <div class="box1">
    <div class="chat-container">
      <div class="messages" id="messages" ref="messages">
        <div v-for="(msg, index) in messages" :key="index" :class="['message', msg.sender]">
          <div class="message-text" v-html="msg.text"></div>
        </div>
      </div>
      <div class="input-container">
        <input v-model="userInput" @keyup.enter="sendMessage" class="input-box" placeholder="请输入你的问题..." :disabled="isSending" />
        <button @click="sendMessage" class="send-button" :disabled="isSending">发送</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: -10px;
  width: 100vw;
  height: 80px;
  background-color: rgba(218, 235, 251, 0.497);
  z-index: 999;
}

.navbar ul {
  list-style-type: none;
  display: flex;
  justify-content: center;
}

.navbar ul li {
  position: relative;
  padding-left: 50px;
  padding-top: 5px;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.navbar a {
  text-decoration: none;
  color: black;
  padding: 8px 16px;
}

.navbar a:visited {
  color: black;
}

.navbar a:hover {
  background-color: rgba(240, 248, 255, 0.599);
}

.navbar a:active,
.navbar a:focus {
  color: black;
}

.navbar ul li .logout-button {
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
  transition: background-color 0.1s;
  position: relative;
  background-color: #3967ff;
  color: #fff;
  cursor: pointer;
  border: none;
}

.navbar ul li .logout-button:hover {
  background-color: #0056b3;
}

.box1 {
  background-color: rgb(230, 241, 250);
  background-attachment: fixed;
  width: 100vw;
  height: 98vh;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.chat-container {
  display: flex;
  flex-direction: column;
  height: 89%;
  max-width: 700px;
  margin: 0 auto;
  padding-top: 80px;
}

.messages {
  flex: 1;
  overflow-y: auto;
  border-radius: 10px;
  padding: 10px;
  background-color: white;
  display: flex;
  flex-direction: column;
}

.message {
  display: flex;
  margin-bottom: 10px;
}

.message.user {
  justify-content: flex-start;
}

.message.ai {
  justify-content: flex-end;
}

.message-text {
  max-width: 60%;
  padding: 10px;
  border-radius: 10px;
  background-color: #f1f1f1;
  word-wrap: break-word;
}

.message.user .message-text {
  background-color: #e1ffc7;
  align-self: flex-start;
}

.message.ai .message-text {
  background-color: #d1d1f0;
  align-self: flex-end;
}

.input-container {
  display: flex;
  align-items: center;
  margin-top: 10px;
  margin-bottom: 20px;
}

.input-box {
  flex: 1;
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 10px;
}

.send-button {
  border: none;
  background-color: #007bff;
  border-radius: 10px;
  color: white;
  padding: 10px 20px;
  margin-left: 10px;
  cursor: pointer;
}

.send-button:disabled {
  background-color: #ccc; /* 灰色背景 */
  cursor: not-allowed; /* 鼠标样式改为不允许 */
}
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userInput: '',
      messages: [],
      isFirstInteraction: true,
      isSending: false // 添加一个标志位来控制发送按钮的启用状态
    };
  },
  mounted() {
    if (this.isFirstInteraction) {
      this.typeMessage({
        sender: 'ai',
        text: "你好！我是医疗助手AI，我在这里帮助你解答健康和医疗相关的问题。请随时向我提问。"
      });
      this.isFirstInteraction = false;
    }
  },
  methods: {
    async sendMessage() {
      if (this.userInput.trim() === '') return;

      this.isSending = true; // 开始发送时，禁用发送按钮

      this.messages.push({
        sender: 'user',
        text: this.userInput
      });

      const userInput = this.userInput;
      this.userInput = '';

      try {
        const response = await axios.post('/chat/', { message: userInput }, {
          headers: {
            'Content-Type': 'application/json',
          }
        });
        let responseText = response.data.response;
        if (typeof responseText === 'object' && responseText !== null) {
          responseText = responseText.output || JSON.stringify(responseText);
        }
        this.typeMessage({
          sender: 'ai',
          text: responseText
        });
      } catch (error) {
        console.error("Error calling AI:", error);
        this.messages.push({
          sender: 'ai',
          text: "对不起，无法回答该问题。请重新提问"
        });
        this.isSending = false; // 如果请求失败，恢复按钮状态
      }
    },
    typeMessage(message) {
      let text = message.text;
      let currentText = '';
      const interval = setInterval(() => {
        if (currentText.length < text.length) {
          currentText += text[currentText.length];
          this.messages[this.messages.length - 1].text = currentText;
        } else {
          clearInterval(interval);
          this.isSending = false; // 类型效果完成后恢复按钮状态
          this.scrollToBottom(); // 滚动到消息容器的底部
        }
      }, 80);
      this.messages.push({
        sender: message.sender,
        text: ''
      });
    },
    scrollToBottom() {
      this.$nextTick(() => {
        const messagesContainer = this.$refs.messages;
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
      });
    }
  }
};
</script>