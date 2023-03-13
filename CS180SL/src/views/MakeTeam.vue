<template>
<div class="make-team-container">
    <a-form :form="form" @submit="handleSubmit" layout="vertical">
    <a-form-item label="Team Name" :colon="false">
        <a-input v-model:value="teamName" />
    </a-form-item>
    <a-form-item label="Team Members" :colon="false">
        <a-select
        mode="tags"
        v-model:value="teamMembers"
        placeholder="Enter email addresses"
        style="width: 100%"
        />
    </a-form-item>
    <a-form-item>
        <a-button type="primary" html-type="submit">Create Team</a-button>
    </a-form-item>
    </a-form>
</div>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";
import { Form, Input, Select, Button } from "ant-design-vue";

export default defineComponent({
components: {
    "a-form": Form,
    "a-form-item": Form.Item,
    "a-input": Input,
    "a-select": Select,
    "a-button": Button,
},
setup() {
    const form = reactive({});
    const teamName = reactive("");
    const teamMembers = reactive([]);

    const handleSubmit = () => {
    console.log("Submitting form with data:", {
        teamName: teamName,
        teamMembers: teamMembers,
    });
    // Handle form submission logic here...
    };

    return {
    form,
    teamName,
    teamMembers,
    handleSubmit,
    };
},
});
</script>

<style lang="less" scoped>
.make-team-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 32px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: white;
}
</style>