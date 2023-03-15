import request from "@/service/request";

interface User {
  id: number;
  user_name: string;
  password: string;
}

export async function register(data: Partial<User>): Promise<User> {
  return request.post("/users/", data);
}

export async function login(params: Partial<User>): Promise<User[]> {
  return request.get("/login/", {
    params,
  });
}

export async function updateUser(data: Partial<User>): Promise<User[]> {
  return request.put(`/users/${data.id}/`, data);
}
