<template>
  <div class="activity-planning">
    <h1>Activity Planning</h1>
    <a-row :gutter="[16, 16]">
      <a-col :span="12">
        <h2>Proposed Activities</h2>
        <ul>
          <li v-for="activity in proposedActivities" :key="activity.id">
            <a-checkbox v-model:checked="activity.selected">{{ activity.name }}</a-checkbox>
          </li>
        </ul>
      </a-col>
      <a-col :span="12">
        <h2>Selected Activities</h2>
        <ul>
          <li v-for="activity in selectedActivities" :key="activity.id">
            {{ activity.name }}
          </li>
        </ul>
      </a-col>
    </a-row>
    <a-divider />
    <h2>Add Activity</h2>
    <a-form :form="form" @finish="addActivity">
      <a-form-item
        label="Activity Name"
        name="activityName"
        rules="[{ required: true, message: 'Please enter an activity name' }]"
      >
        <a-input v-model:value="activityName" />
      </a-form-item>
      <a-form-item>
        <a-button type="primary" html-type="submit">Add Activity</a-button>
      </a-form-item>
    </a-form>
  </div>
</template>

<script>
import { defineComponent, reactive } from "vue";
import { message } from "ant-design-vue";

export default defineComponent({
  name: "ActivityPlanning",
  setup() {
    const form = reactive({
      activityName: "",
    });

    const activities = [
      { id: 1, name: "Hiking", selected: false },
      { id: 2, name: "Biking", selected: false },
      { id: 3, name: "Picnic", selected: false },
      { id: 4, name: "Movie Night", selected: false },
      { id: 5, name: "Board Games", selected: false },
    ];

    const addActivity = () => {
      if (!form.activityName) {
        message.warning("Please enter an activity name");
        return;
      }
      const newActivity = {
        id: activities.length + 1,
        name: form.activityName,
        selected: false,
      };
      activities.push(newActivity);
      form.activityName = "";
      message.success(`Added ${newActivity.name}`);
    };

    const proposedActivities = activities.filter((activity) => !activity.selected);
    const selectedActivities = activities.filter((activity) => activity.selected);

    return {
      form,
      activities,
      addActivity,
      proposedActivities,
      selectedActivities,
    };
  },
});
</script>

<style scoped>
.activity-planning {
  padding: 24px;
}
</style>