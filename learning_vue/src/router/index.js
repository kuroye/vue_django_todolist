import { createRouter, createWebHistory } from 'vue-router'
const Todolist = ()=> import('@/pages/TodoListPage.vue')
const TodoForm = ()=> import('@/pages/TodoFormPage.vue')
const Ability = ()=> import('@/pages/ability/AbilityPage.vue')
const AbilityGroup = ()=> import('@/pages/ability/GroupPage.vue')
const SingleGroup = ()=> import('@/pages/ability/SingleGroupPage.vue')
const Profile = ()=> import('@/pages/ProfilePage.vue')
const Register = ()=> import('@/pages/RegisterPage.vue')
const Login = ()=> import('@/pages/LoginPage.vue')
const Lottery = ()=> import('@/pages/LotteryPage.vue')

const routes = [  
    {    path: '/',    name: 'todolist',    component: Todolist  }, 
    {    path: '/auth/register',    name: 'register',    component: Register  }, 
    {    path: '/auth/login',    name: 'login',    component: Login  }, 
    {    path: '/todo-add',    name: 'add todo',    component: TodoForm  }, 
    {    path: '/ability',    name: 'ability',    component: Ability,  }, 
    {    path: '/ability/group',    name: 'add group',    component: AbilityGroup,  }, 
    {    path: '/ability/group/:id',    name: 'single group',    component: SingleGroup,  }, 
    {    path: '/profile',    name: 'profile',    component: Profile,  }, 
    {    path: '/lottery',    name: 'lottery',    component: Lottery,  }, 
]
const router = createRouter({  
    history: createWebHistory(),  
    routes
})


// 全局守卫：登录拦截 本地没有存token,请重新登录
router.beforeEach((to, from, next) => {
	// 判断有没有登录
	if (!localStorage.getItem('token')) {
		if (to.name == "login" || to.name == "register") {
			next();
		} else {
			router.push('/auth/login')
		}
        
	} else {
		next();
	}
});

export default router