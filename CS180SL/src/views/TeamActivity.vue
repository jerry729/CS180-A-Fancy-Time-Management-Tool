<template>
  <div class="activity-planning">
    <h1>Team Activity Planning</h1>
    <a-row :gutter="[16, 16]">
      <a-col :span="12">
        <a-card class="card">
          <h2>Proposed Activities</h2>
          <ul>
            <li v-for="activity in proposedActivities" :key="activity.id">
              <a-checkbox v-model:checked="activity.selected">{{ activity.name }}</a-checkbox>
            </li>
          </ul>
        </a-card>
      </a-col>
      <a-col :span="12">
        <a-card class="card">
        <h2>Selected Activities</h2>
        <ul>
          <li v-for="activity in selectedActivities" :key="activity.id">
            {{ activity.name }}
            <a-button size="small" type="danger" @click="removeActivity(activity.id)">Remove</a-button>
          </li>
        </ul>
      </a-card>
      </a-col>
    </a-row>
    <a-divider />
    <h2>Add Activity</h2>
    <a-form :model="form" @finish="addActivity">
      <a-form-item
        label="Activity Name"
        name="activityName"
        rules="[{ required: true, message: 'Please enter an activity name' }]"
      >
        <a-input v-model:value="form.activityName" />
      </a-form-item>
      <a-form-item>
        <a-button type="primary" html-type="submit">Add Activity</a-button>
      </a-form-item>
    </a-form>
  </div>
</template>

<script>
import { defineComponent, reactive, computed } from "vue";
import { message } from "ant-design-vue";

export default defineComponent({
  name: "ActivityPlanning",
  setup() {
    const form = reactive({
      activityName: "",
    });
    
    const removeActivity = (id) => {
      const activityIndex = activities.findIndex((activity) => activity.id === id);
      if (activityIndex !== -1) {
        activities.splice(activityIndex, 1);
        message.success("Removed activity");
      }
    };

    const activities = reactive([
      { id: 1, name: "Hiking", selected: false },
      { id: 2, name: "Biking", selected: false },
      { id: 3, name: "Picnic", selected: false },
      { id: 4, name: "Movie Night", selected: false },
      { id: 5, name: "Board Games", selected: false },
    ]);

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

    const proposedActivities = computed(() => activities.filter((activity) => !activity.selected));
    const selectedActivities = computed(() => activities.filter((activity) => activity.selected));

  return {
      form,
      addActivity,
      removeActivity,
      proposedActivities,
      selectedActivities,
    };
  },
});
</script>

<style scoped>
.activity-planning {
  padding: 24px;
  height: 100vh;
  width: 100%;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
}

h1,
h2 {
  color: #001529;
}

h1 {
  font-size: 36px;
  margin-bottom: 24px;
}

h2 {
  font-size: 24px;
  margin-bottom: 16px;
}

.card {
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.06);
  padding: 24px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 8px;
}
</style>

<style>
body {
  background-color: white;
  margin: 0;
}
</style>