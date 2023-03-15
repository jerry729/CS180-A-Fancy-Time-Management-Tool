<script lang="ts">
import { defineComponent, ref } from "vue";
import { useUserStore, type User } from "@/stores/user";
import { updateUser } from "@/service/user";
import { message } from "ant-design-vue";
import { useRouter } from "vue-router";

export default defineComponent({
  setup() {
    const { user } = useUserStore();
    const form = ref<User>(user!);
    const router = useRouter();

    const onFinish = async () => {
      await updateUser(form.value);
      message.success("Modified successfully");
      router.push("/login");
    };

    return {
      form,
      onFinish,
    };
  },
});
</script>

<template>
  <main class="settings-container">
    <div class="form-wrapper">
      <a-form
        :model="form"
        hideRequiredMark
        layout="vertical"
        autocomplete="off"
        @finish="onFinish"
      >
        <!-- 使用 a-form-item 组件来创建表单项 -->
        <a-form-item label="User ID">
          <a-input v-model:value="form.id" disabled />
        </a-form-item>
        <a-form-item label="Change UserName">
          <a-input v-model:value="form.user_name" />
        </a-form-item>
        <a-form-item label="Change Password">
          <a-input v-model:value="form.password" type="password" />
        </a-form-item>
        <a-button type="primary" htmlType="submit">修改</a-button>
      </a-form>
    </div>
  </main>
</template>

<style lang="less" scoped>
.settings-container {
  width: 100%;
  height: 100%;
  overflow: auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

.form-wrapper {
  display: flex;
  flex-direction: column;
  width: 400px;
}

button {
  width: 100%;
  margin-top: 10px;
}
</style>
