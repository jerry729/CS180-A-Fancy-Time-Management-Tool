import request from "@/service/request";

export interface Task {
  id: number;
  Task_owner_user: number;
  Task_owner_scheduler: number;
  Task_name: string;
  Task_description: string;
  Task_start_time: string;
  Task_end_time: string;
}

export async function getTaskList(params?: Task): Promise<Task[]> {
  return request.get("/tasks/", {
    params,
  });
}

export async function createTask(data: Partial<Task>): Promise<Task[]> {
  return request.post("/tasks/", data);
}

export async function updateTask(data: Partial<Task>): Promise<Task[]> {
  return request.put(`/tasks/${data.id}/`, data);
}

export async function deleteTask(id: number) {
  return request.delete(`/tasks/${id}/`);
}
