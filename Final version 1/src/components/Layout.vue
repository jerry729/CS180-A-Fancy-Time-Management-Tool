<template>
  <a-layout class="layout-container">
    <a-layout-sider class="sider">
      <div class="logo">Schedule management</div>
      <a-menu v-model:selectedKeys="selectedKeys" theme="dark" mode="inline">
        <a-menu-item key="/">
          <home-outlined />
          <span>Home</span>
        </a-menu-item>
        <a-menu-item key="/calendar">
          <calendar-outlined />
          <span>Calendar</span>
        </a-menu-item>
        <a-menu-item key="/team">
          <calendar-outlined />
          <span>MakeTeam</span>
        </a-menu-item>
        <a-menu-item key="/view-team">
          <calendar-outlined />
          <span>ViewTeam</span>
        </a-menu-item>
        <a-menu-item key="/team-activity">
          <calendar-outlined />
          <span>TeamActivity</span>
        </a-menu-item>
        <a-menu-item key="/settings">
          <setting-outlined />
          <span>Settings</span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header>
        {{ user?.user_name }}
        <a-dropdown>
          <a-avatar style="background-color: #87d068">
            <template #icon>
              <user-outlined />
            </template>
          </a-avatar>
          <template #overlay>
            <a-menu>
              <a-menu-item>
                <a href="/login">Logout</a>
              </a-menu-item>
            </a-menu>
          </template>
        </a-dropdown>
      </a-layout-header>
      <a-layout-content>
        <router-view></router-view>
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>
<script lang="ts">
import {
  HomeOutlined,
  CalendarOutlined,
  SettingOutlined,
  UserOutlined,
} from "@ant-design/icons-vue";
import { defineComponent, ref } from "vue";
import { useUserStore } from "@/stores/user";

export default defineComponent({
  components: {
    HomeOutlined,
    CalendarOutlined,
    SettingOutlined,
    UserOutlined,
  },
  watch: {
    selectedKeys() {
      // 跳转页面
      this.$router.push(this.selectedKeys[0]);
    },
  },
  mounted() {
    this.selectedKeys = [this.$route.path];
  },
  setup() {
    const userStore = useUserStore();
    return {
      user: userStore.user,
      selectedKeys: ref<string[]>(["/"]),
    };
  },
});
</script>
<style lang="less">
.layout-container {
  width: 100vw;
  height: 100vh;

  .sider {
    background-image: linear-gradient(to top, #5ee7df 0%, #b490ca 100%);
  }

  .ant-menu {
    background-color: transparent;
  }

  .ant-layout-header {
    padding: 0 24px 0 0;
    background: #fff;
    text-align: end;
  }

  .ant-layout-content {
    margin: 24px 16px;
    padding: 24px;
    background: #fff;
    min-height: 280px;
    overflow: auto;
  }
}

.layout-container .logo {
  background: linear-gradient(
    to right,
    pink,
    orange,
    yellow,
    green,
    cyan,
    blue,
    purple
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: hue 3s linear infinite;
  font-size: 20px;
  font-weight: 700;
  padding: 16px;
}

@keyframes hue {
  0% {
    filter: hue-rotate(0deg);
  }
  100% {
    filter: hue-rotate(360deg);
  }
}
</style>
