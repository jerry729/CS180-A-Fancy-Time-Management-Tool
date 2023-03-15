<script lang="ts">
import { defineComponent, ref, reactive } from "vue";
import dayjs from "dayjs";
import { message } from "ant-design-vue";
import type { Dayjs } from "dayjs";
import type { FormInstance } from "ant-design-vue";
import { useUserStore } from "@/stores/user";
import ScheduleDetail from "@/components/ScheduleDetail.vue";
import {
  createTask,
  deleteTask,
  getTaskList,
  updateTask,
  type Task,
} from "@/service/task";

interface FormState extends Task {
  date?: Dayjs[];
}

export default defineComponent({
  components: {
    ScheduleDetail,
  },
  setup() {
    const { user } = useUserStore();
    const calendarMode = ref<string>("month");
    const value = ref<Dayjs>();
    const visible = ref<boolean>(false);
    const formRef = ref<FormInstance>();
    const list = ref<FormState[]>();

    const formState = reactive<Partial<FormState>>({
      id: undefined,
      Task_name: "",
      date: [],
    });

    const getList = async () => {
      list.value = await getTaskList();
    };

    getList();

    const getListData = (value: Dayjs) => {
      const data = list?.value?.filter((item) => {
        return dayjs(value).isBetween(
          dayjs(item.Task_start_time),
          dayjs(item.Task_end_time),
          "day",
          "[]"
        );
      });
      return (
        data?.map((item) => ({
          ...item,
          key: item.id,
          type: "success",
        })) || []
      );
    };

    const getMonthData = (value: Dayjs) => {
      console.log(value);
      return null;
    };

    const onSelect = (value: Dayjs) => {
      if (calendarMode.value === "month") {
        formState.date = [value, value];
        formState.Task_name = "";
        formState.id = undefined;
        visible.value = true;
      }
    };

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

    const onPanelChange = (value: Dayjs, mode: string) => {
      calendarMode.value = mode;
    };

    const deleteSchedule = async (schedule: FormState) => {
      const id = schedule.id;
      await deleteTask(id);
      await getList();
      message.success("Delete succeeded");
    };

    const editSchedule = (schedule: FormState) => {
      visible.value = true;
      formState.date = [
        dayjs(schedule.Task_start_time),
        dayjs(schedule.Task_end_time),
      ];
      formState.Task_name = schedule.Task_name;
      formState.id = schedule.id;
    };

    return {
      visible,
      handleOk,
      value,
      list,
      getListData,
      getMonthData,
      onSelect,
      onPanelChange,
      calendarMode,
      formRef,
      formState,
      deleteSchedule,
      editSchedule,
    };
  },
});
</script>

<template>
  <main class="calendar-container">
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
    <a-calendar
      v-model:value="value"
      @select="onSelect"
      @panelChange="onPanelChange"
    >
      <template #dateCellRender="{ current }">
        <ul class="events">
          <li v-for="item in getListData(current)" v-bind:key="item.key">
            <schedule-detail
              @remove="deleteSchedule"
              @edit="editSchedule"
              :item="item"
            />
          </li>
        </ul>
      </template>
      <template #monthCellRender="{ current }">
        <div v-if="getMonthData(current)" class="notes-month">
          <section>{{ getMonthData(current) }}</section>
        </div>
      </template>
    </a-calendar>
  </main>
</template>

<style lang="less" scoped>
.calendar-container {
  width: 100%;
  height: 100%;
  overflow: auto;

  .ant-picker-calendar-full {
    width: 1000px;
    margin: auto;
  }

  .events {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .events .ant-badge-status {
    overflow: hidden;
    white-space: nowrap;
    width: 100%;
    text-overflow: ellipsis;
    font-size: 12px;
  }
  .notes-month {
    text-align: center;
    font-size: 28px;
  }
  .notes-month section {
    font-size: 28px;
  }
}
</style>
