<script lang="ts">
import { defineComponent, ref, reactive } from "vue";
import {
  EditOutlined,
  DeleteOutlined,
  PlusOutlined,
} from "@ant-design/icons-vue";
import dayjs from "dayjs";
import { message } from "ant-design-vue";
import type { Dayjs } from "dayjs";
import type { FormInstance } from "ant-design-vue";
import {
  createTask,
  deleteTask,
  getTaskList,
  updateTask,
  type Task,
} from "@/service/task";
import { useUserStore } from "@/stores/user";

interface FormState extends Task {
  date?: Dayjs[];
}

export default defineComponent({
  components: {
    EditOutlined,
    DeleteOutlined,
    PlusOutlined,
  },
  setup() {
    const { user } = useUserStore();
    const calendarMode = ref<string>("month");
    const value = ref<Dayjs>();
    const visible = ref<boolean>(false);
    const formRef = ref<FormInstance>();
    const list = ref<Task[]>();

    const formState = reactive<Partial<FormState>>({
      id: undefined,
      Task_name: "",
      date: undefined,
    });

    const getList = async () => {
      list.value = await getTaskList();
    };

    getList();

    const handleOk = async () => {
      const values = await formRef.value!.validateFields();
      visible.value = false;
      formRef.value?.resetFields();

      const data = {
        Task_owner_user: user!.id,
        id: values.id,
        Task_name: values.Task_name,
        Task_start_time: dayjs(values.date[0]).format("YYYY-MM-DDTHH:mm:ssZ"),
        Task_end_time: dayjs(values.date[1]).format("YYYY-MM-DDTHH:mm:ssZ"),
      };

      if (values.id) {
        await updateTask(data);
      } else {
        await createTask(data);
      }
      await getList();
      message.success(
        values.id ? "Modified successfully" : "Added successfully"
      );
    };

    const onRemove = async (schedule: FormState) => {
      const id = schedule.id;
      await deleteTask(id);
      await getList();
      message.success("Delete succeeded");
    };

    const onEdit = (schedule: FormState) => {
      visible.value = true;
      formState.date = [
        dayjs(schedule.Task_start_time),
        dayjs(schedule.Task_end_time),
      ];
      formState.Task_name = schedule.Task_name;
      formState.id = schedule.id;
    };

    const formatDates = (startDate: string, endDate: string) => {
      const start = [
        dayjs(startDate).format("YYYY-MM-DD"),
        `(${dayjs(startDate).format("dddd")})`,
      ].join("");

      const end = [
        dayjs(endDate).format("YYYY-MM-DD"),
        `(${dayjs(endDate).format("dddd")})`,
      ].join("");
      if (start === end) {
        return start;
      }
      return [start, end].join(" ~ ");
    };

    const onAdd = () => {
      formState.date = undefined;
      formState.Task_name = "";
      formState.id = undefined;
      visible.value = true;
    };

    return {
      visible,
      onEdit,
      onRemove,
      handleOk,
      value,
      list,
      calendarMode,
      formRef,
      formState,
      formatDates,
      onAdd,
    };
  },
});
</script>

<template>
  <main class="home-container">
    <a-card v-for="item in list" :key="item.Task_name">
      <template #extra>
        <a-space>
          <edit-outlined @click="onEdit(item)" />
          <a-popconfirm
            title="Are you sure delete this schedule?"
            ok-text="Yes"
            cancel-text="No"
            @confirm="onRemove(item)"
          >
            <delete-outlined />
          </a-popconfirm>
        </a-space>
      </template>
      <div :key="item.id">
        Title: {{ item.Task_name }}
        <br />
        Date: {{ formatDates(item.Task_start_time, item.Task_end_time) }}
      </div>
    </a-card>
    <a-card class="add-item">
      <div @click="onAdd">
        <plus-outlined />
      </div>
    </a-card>
    <a-modal
      v-model:visible="visible"
      :mode="calendarMode"
      :title="formState.id ? 'Edit Schedule' : 'Create Schedule'"
      @ok="handleOk"
    >
      <a-form
        ref="formRef"
        :model="formState"
        name="form_in_modal"
        layout="vertical"
        autocomplete="off"
      >
        <a-form-item
          label="Date"
          name="date"
          :rules="[{ required: true, message: 'Please pick your date!' }]"
        >
          <a-range-picker
            v-model:value="formState['date']"
            value-format="YYYY-MM-DD"
          />
        </a-form-item>
        <a-form-item
          name="Task_name"
          label="Title"
          :rules="[{ required: true, message: 'Please input your title!' }]"
        >
          <a-input v-model:value="formState.Task_name" />
        </a-form-item>
        <a-form-item hidden name="id">
          <a-input v-model:value="formState.id" />
        </a-form-item>
      </a-form>
    </a-modal>
  </main>
</template>

<style lang="less">
.home-container {
  width: 100%;
  overflow: auto;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 50px;

  .ant-card {
    justify-self: center;
    width: 300px;
    min-height: 200px;
    background-color: #f2f2f2;

    .ant-card-head {
      border-bottom: 1px solid #e8e8e8;
    }
  }

  .add-item {
    .ant-card-body {
      cursor: pointer;
      height: 100%;
      padding: 0;
      div {
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
      }
    }
  }
}
</style>
