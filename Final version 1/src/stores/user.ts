import { ref } from "vue";
import { defineStore } from "pinia";

export interface User {
  id: number;
  user_name: string;
  password: string;
}

export const useUserStore = defineStore("counter", () => {
  const user = ref<User | undefined>(getSessionUser());

  function setUser(data: User) {
    user.value = data;
    saveSessionUser(data);
  }

  function saveSessionUser(data: User) {
    sessionStorage.setItem("user", JSON.stringify(data));
  }

  function getSessionUser(): User | undefined {
    const userStr = sessionStorage.getItem("user");
    if (userStr) {
      return JSON.parse(userStr);
    }
    return undefined;
  }

  return { user, setUser };
});
