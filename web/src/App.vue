<template>
  <div class="common-layout">
    <el-container>
      <el-header>睿医网信办V2.0</el-header>
      <el-main>
        <router-view/>
      </el-main>
      <el-footer>由陈启源开发</el-footer>
    </el-container>
  </div>
</template>
<style>
.el-container {
  height: 100vh;
  display: flex;
}

.el-header,
.el-footer {
  color: #409eff;
  text-align: center;
  line-height: 60px;
}

.el-header {
  font-size: x-large;
  font-weight: 800;
}

.el-footer {
  font-size: medium;
  font-weight: 400;
}

.el-main {
  color: #409eff;
  text-align: center;
  display: flex;
  align-items: center;
}

.el-aside {
  color: #409EFF;
  text-align: center;
  display: flex;
  align-items: center;
}
</style>