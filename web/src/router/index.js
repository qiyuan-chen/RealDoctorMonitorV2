import {createRouter, createWebHistory} from 'vue-router'
import LoginPage from "../views/LoginPage.vue";
import RegisterPage from "../views/RegisterPage.vue";
import HomePage from "../views/HomePage.vue";
import ReportBugs from "../components/ReportBugs.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'login',
            component: LoginPage
        },
        {
            path: '/register',
            name: 'register',
            component: RegisterPage
        },
        {
            path: '/home',
            name: 'home',
            component: HomePage
        },
        {
            path: '/report-bugs',
            name: 'ReportBugs',
            component: ReportBugs
        }
    ]
})

export default router
