<script lang="ts">
import { login } from "@/service/user";
import { message } from "ant-design-vue";
import { defineComponent, ref, reactive } from "vue";
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores/user";

interface FormState {
  username: string;
  password: string;
  remember: boolean;
}
export default defineComponent({
  setup() {
    const userStore = useUserStore();
    const loading = ref<boolean>(false);
    const router = useRouter();
    const formState = reactive<FormState>({
      username: "",
      password: "",
      remember: true,
    });
    const onFinish = async () => {
      try {
        loading.value = true;
        const res = await login({
          user_name: formState.username,
          password: formState.password,
        });
        if (res?.length > 0) {
          router.push("/");
          userStore.setUser(res[0]);
        } else {
          message.error("Incorrect username or password");
        }
      } finally {
        loading.value = false;
      }
    };

    const onFinishFailed = (errorInfo: any) => {
      console.log("Failed:", errorInfo);
    };
    return {
      loading,
      formState,
      onFinish,
      onFinishFailed,
    };
  },
});
</script>

<template>
  <main>
    <div class="left-banner"></div>
    <div class="login-form">
      <a-form
        :model="formState"
        name="basic"
        :colon="false"
        hideRequiredMark
        layout="vertical"
        autocomplete="off"
        @finish="onFinish"
        @finishFailed="onFinishFailed"
      >
        <h2>Login</h2>
        <h4>Login to your account</h4>
        <a-form-item
          label="Username"
          name="username"
          :rules="[{ required: true, message: 'Please input your username!' }]"
        >
          <a-input v-model:value="formState.username" />
        </a-form-item>

        <a-form-item
          label="Password"
          name="password"
          :rules="[{ required: true, message: 'Please input your password!' }]"
        >
          <a-input-password v-model:value="formState.password" />
        </a-form-item>

        <a-form-item name="remember">
          <a-checkbox v-model:checked="formState.remember">
            Remember me
          </a-checkbox>
        </a-form-item>

        <a-form-item>
          <a-button type="primary" html-type="submit" :loading="loading">
            Sign in
          </a-button>
        </a-form-item>

        <p>
          Don't have an account yet?
          <router-link to="/register">Sign up</router-link>
        </p>
      </a-form>
    </div>
  </main>
</template>

<style lang="less" scoped>
main {
  display: flex;
  width: 100vw;
  height: 100vh;
}

.left-banner {
  width: 40%;
  background-image: linear-gradient(to top, #a6c1ee 0%, #fbc2eb 100%);
}

.login-form {
  width: 100%;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: start;

  form {
    width: 400px;
    h2 {
      width: 100%;
      margin-bottom: 50px;
    }

    h4 {
      margin-bottom: 30px;
    }

    button {
      width: 100%;
    }
  }
  background-color: white;
}
</style>
