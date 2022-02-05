import { createRouter, createWebHistory } from 'vue-router'

const routes = [
	{
		path: '/',
		name: 'Feeds',
		component: () => import('@/pages/Feeds.vue'),
	},
]

let router = createRouter({
	history: createWebHistory('/'),
	routes,
})

export default router
