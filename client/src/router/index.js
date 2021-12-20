import { createRouter, createWebHistory } from "vue-router";
import Home from "/src/views/Home.vue";
import Events from "/src/views/Events.vue";
import Register from "/src/views/Register.vue";
import NotFound from "/src/views/NotFound.vue";

const routes = [
  { path: "/", name: "Home", component: Home },
  { path: "/events", name: "Events", component: Events },
  { path: "/register/:id", name: "Register", component: Register,props:true },
  { path: "/:catchAll(.*)", name: "NotFound", component: NotFound },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
