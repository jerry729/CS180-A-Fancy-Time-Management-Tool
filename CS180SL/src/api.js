import axios from "axios";

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/', // This should be the URL of your backend API
  withCredentials: true,
});

export default {
  // Define functions for making API requests here
  async login(username, password) {
    try {
      const response = await apiClient.post("/login", {
        username,
        password,
      });
      return response.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  },
};