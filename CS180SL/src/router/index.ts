import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";
import MakeTeam from "@/views/MakeTeam.vue";
import ViewTeam from "@/views/ViewTeam.vue";
import TeamActivity from "@/views/TeamActivity.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
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
    {
      path:"/team",
      name: "MakeTeam",
      component: MakeTeam,
    },
    {
      path:"/view-team",
      name: "ViewTeam",
      component: ViewTeam,
    },
    {
      path:"/team-activity",
      name: "TeamAcitivity",
      component: TeamActivity,
    },
  ],
});

export default router;
