<template>
  <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
  >
    <el-sub-menu index="2">
      <template #title>资源管理</template>
      <el-menu-item index="2-1">item one</el-menu-item>
      <el-menu-item index="2-2">item two</el-menu-item>
      <el-menu-item index="2-3">item three</el-menu-item>
      <el-sub-menu index="2-4">
        <template #title>item four</template>
        <el-menu-item index="2-4-1">item one</el-menu-item>
        <el-menu-item index="2-4-2">item two</el-menu-item>
        <el-menu-item index="2-4-3">item three</el-menu-item>
      </el-sub-menu>
    </el-sub-menu>
    <el-sub-menu index="2">
      <template #title>Workspace</template>
      <el-menu-item index="2-1">item one</el-menu-item>
      <el-menu-item index="2-2">item two</el-menu-item>
      <el-menu-item index="2-3">item three</el-menu-item>
      <el-sub-menu index="2-4">
        <template #title>item four</template>
        <el-menu-item index="2-4-1">item one</el-menu-item>
        <el-menu-item index="2-4-2">item two</el-menu-item>
        <el-menu-item index="2-4-3">item three</el-menu-item>
      </el-sub-menu>
    </el-sub-menu>
    <el-menu-item index="4">报障</el-menu-item>
  </el-menu>
  <component :is="currentComponent"></component>
</template>

<script setup>
import {ref} from 'vue'
import ReportBugs from "../components/ReportBugs.vue";


const activeIndex = ref('4');
// 选择报障后页内渲染reportbugs.vue页面
const currentComponent = ref(null);
const handleSelect = (index) => {
  console.log(index);
  if (index === '4') {
    currentComponent.value = ReportBugs;
  } else {
    // 根据需要更新为其他组件或重置
    currentComponent.value = null;
  }
};
</script>

<style scoped>
</style>