<template>
  <el-container class="login-container">
    <el-card class="box-card">
      <el-header class="login-text">登录</el-header>
      <el-form :model="loginForm" :rules="rules" ref="loginFormRef">
        <el-form-item label="用户名" prop="username" label-position="right" label-width="100px">
          <el-input v-model="loginForm.username" autocomplete="off" style="width: 80%"/>
        </el-form-item>
        <el-form-item label="密码" prop="password" label-position="right" label-width="100px">
          <el-input type="password" v-model="loginForm.password" autocomplete="off" style="width: 80%"/>
        </el-form-item>
        <p>
          NOTE: 初次登录请使用服务器上的用户名，会自动跳转注册
        </p>
        <el-form-item class="bottom-group">
          <el-button type="success" @click="handleLogin" style="width: 100px">登录</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </el-container>
</template>

<script setup>
import {ref} from 'vue'
import axios from 'axios';
import router from "../router";
// 使用路由

const loginForm = ref({
  username: '',
  password: ''
});
const loginFormRef = ref(null);

// 自定义验证规则
const validatePassword = (rule, value, callback) => {
  if (!value) {
    return callback(new Error('请输入密码'));
  }
  // if (value.length < 6) {
  //   return callback(new Error('密码长度不能少于6位'));
  // }
  // if (!/[A-Za-z]/.test(value)) {
  //   return callback(new Error('密码必须包含英文字符'));
  // }
  // if (!/\d/.test(value)) {
  //   return callback(new Error('密码必须包含数字'));
  // }
  callback();
};

const rules = ref({
  username: [
    {required: true, message: '请输入用户名', trigger: 'blur'}
  ],
  password: [
    {validator: validatePassword, trigger: 'blur', required: true}
  ]
});

// TODO: 使用vuex传入用户名
const handleLogin = () => {
  loginFormRef.value.validate(async (valid) => {
    if (valid) {
      try {
        const response = await axios.post('http://127.0.0.1:8000/login', loginForm.value);
        console.log(response)
        if (response.status === 200) {
          alert("hello!")
          // router.push('/home');
        }
      } catch (error) {
        if (error.response) {
          // 请求已发出，服务器以状态码响应
          const statusCode = error.response.status;
          const message = error.response.data.detail || '未知错误';

          if (statusCode === 400) {
            alert('登录失败：' + message);
          } else if (statusCode === 402) {
            alert(message);
            await router.push('/register');
          } else {
            // 处理其他可能的错误状态码
            alert('错误：' + message);
          }
        } else if (error.request) {
          // 请求已发出，但没有收到响应
          console.error('无响应：', error.request);
          alert('登录请求失败，请检查网络连接！');
        } else {
          // 在设置请求时发生了一些事情，触发了一个错误
          console.error('请求错误：', error.message);
          alert('登录请求失败：' + error.message);
        }
      }
    }
  });
};

const resetForm = () => {
  loginFormRef.value.resetFields();
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
  padding: 0 20px;
}

.box-card {
  width: 100%;
  max-width: 500px;
  margin: auto;
}

.login-text {
  color: #606266;
  font-size: large;
  font-weight: 600;
  text-align: center; /* Center the login text */
}

.bottom-group {
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}
</style>
