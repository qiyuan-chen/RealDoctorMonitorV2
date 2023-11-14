<template>
  <el-container class="login-container">
    <el-card class="box-card">
      <el-header class="login-text">注册</el-header>
      <el-form :model="registerForm" :rules="rules" ref="loginFormRef">
        <el-form-item label="用户名" prop="username" label-position="right" label-width="100px">
          <el-input v-model="registerForm.username" autocomplete="off" style="width: 80%"/>
        </el-form-item>
        <el-form-item label="邮箱" prop="password" label-position="right" label-width="100px">
          <el-input v-model="registerForm.password" autocomplete="off" style="width: 80%"/>
        </el-form-item>
        <el-form-item label="密码" prop="password" label-position="right" label-width="100px">
          <el-input type="password" v-model="registerForm.password" autocomplete="off" style="width: 80%"/>
        </el-form-item>
        <el-form-item class="bottom-group">
          <el-button type="success" @click="handleLogin" style="width: 100px">注册</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </el-container>
</template>

<script setup>
import {ref} from 'vue'
import axios from 'axios';
// 使用路由

const registerForm = ref({
  username: '',
  email: '',
  password: ''
});
const registerFormRef = ref(null);

// 自定义验证规则
const validatePassword = (rule, value, callback) => {
  if (!value) {
    return callback(new Error('请输入密码'));
  }
  if (value.length < 6) {
    return callback(new Error('密码长度不能少于6位'));
  }
  if (!/[A-Za-z]/.test(value)) {
    return callback(new Error('密码必须包含英文字符'));
  }
  if (!/\d/.test(value)) {
    return callback(new Error('密码必须包含数字'));
  }
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


const handleRegister = () => {
  registerFormRef.value.validate(async (valid) => {
    if (valid) {
      try {
        const response = await axios.post('http://localhost/login', registerForm.value);
        const {status, message} = response.data;
        // 根据状态做出相应的处理
        if (status === 'error') {
          alert('登录失败：' + message);
        } else if (status === 'success') {
          alert('登录成功：' + message);
        } else if (status === 'first_time') {
          alert('初次登录：' + message);
        }
      } catch (error) {
        // 处理请求失败的情况
        console.error('登录请求失败：', error);
        alert('登录请求失败，请检查网络连接！');
      }
    } else {
      alert('请填写正确的信息！');
    }
  });
};

const resetForm = () => {
  registerFormRef.value.resetFields();
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
