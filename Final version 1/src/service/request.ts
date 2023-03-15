import { message } from "ant-design-vue";
import axios from "axios";

const instance = axios.create({
  baseURL: "http://localhost:8000/api",
  headers: {
    "Content-type": "application/json",
  },
});

instance.interceptors.request.use((config) => {
  return config;
});

instance.interceptors.response.use(
  (response) => {
    // 对响应数据做些处理
    return response.data;
  },
  (error) => {
    // 对响应错误做些处理
    message.error(error.message || "服务器错误");
    return Promise.reject(error);
  }
);

export default instance;
