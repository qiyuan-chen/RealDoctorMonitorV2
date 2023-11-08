import {createRouter, createWebHistory} from 'vue-router'
import LoginPage from "../views/LoginPage.vue";
import test from "../views/test.vue"

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'login',
            component: LoginPage
        },
        {
            path: '/test',
            name: 'test',
            component: test
        }
    ]
})

export default router
