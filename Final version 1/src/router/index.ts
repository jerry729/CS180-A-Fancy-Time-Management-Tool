import { createRouter, createWebHistory } from "vue-router";
import Layout from "@/components/Layout.vue";
import HomeView from "@/views/HomeView.vue";
import CalendarView from "@/views/CalendarView.vue";
import SettingsView from "@/views/SettingsView.vue";
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";
import MakeTeam from "@/views/MakeTeam.vue";
import ViewTeam from "@/views/ViewTeam.vue";
import TeamActivity from "@/views/TeamActivity.vue";
import { useUserStore } from "@/stores/user";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "layout",
      component: Layout,
      children: [
        {
          path: "/",
          name: "home",
          component: HomeView,
          meta: {
            requiresAuth: true,
          },
        },
        {
          path: "/calendar",
          name: "calendar",
          component: CalendarView,
          meta: {
            requiresAuth: true,
          },
        },
        {
          path: "/settings",
          name: "settings",
          component: SettingsView,
          meta: {
            requiresAuth: true,
          },
        },
        {
          path:"/team",
          name: "MakeTeam",
          component: MakeTeam,
          meta: {
            requiresAuth: true,
          },
        },
        {
          path: "/view-team",
          name: "ViewTeam",
          component: ViewTeam,
          meta: {
            requiresAuth: true,
          },
        },
        {
          path: "/team-activity",
          name: "TeamAcitivity",
          component: TeamActivity,
          meta: {
            requiresAuth: true,
          },
        },
      ],
    },
    {
      path: "/login",
      name: "Login",
      component: LoginView,
    },
    {
      path: "/register",
      name: "Register",
      component: RegisterView,
    },
  ],
});

router.beforeEach((to, from, next) => {
  const { user } = useUserStore();
  if (to.meta.requiresAuth && !user) {
    next("/login");
  } else {
    next();
  }
});

export default router;
