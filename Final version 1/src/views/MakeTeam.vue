<template>
<div class="make-team-container">
        <a-form :form="form" @submit="handleSubmit" layout="vertical">
        <a-form-item label="Team Name" :colon="false">
            <a-input v-model="teamName"/>
        </a-form-item>
        <a-form-item label="Team Members" :colon="false">
            <div class="team-members">
            <a-select
                mode="tags"
                v-model="teamMembers"
                placeholder="Enter email addresses"
            />
            <a-button class="add-member-button" type="primary" @click="addMember">Add Member</a-button>
            <div class="team-members-list">
                <ul>
                <li v-for="member in teamMembers" :key="member">{{ member }}</li>
                </ul>
            </div>
            </div>
        </a-form-item>
        <a-form-item>
            <a-button type="primary" html-type="submit">Create Team</a-button>
        </a-form-item>
        <a-form-item>
            <a-button class="back-button" @click="goBack">Back</a-button>
            </a-form-item>
        </a-form>
</div>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";
import { Form, Input, Select, Button } from "ant-design-vue";
export default defineComponent({
methods: {
    goBack() {
        this.$router.push('/');
    }
},
components: {
    "a-form": Form,
    "a-form-item": Form.Item,
    "a-input": Input,
    "a-select": Select,
    "a-button": Button,
},
setup() {
    const form = reactive({});
    const teamName = reactive([]);
    const teamMembers = reactive([]);
    const addMember = () => {
    teamMembers.push();
    };
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
    addMember,
    handleSubmit,
    };
},
});
</script>

<style lang="less" scoped>
.make-team-container {
width: 100vw;
height: 100vh;
margin: 0 auto;
padding: 32px;
display: flex;
justify-content: center;
align-items: center;

background-image: linear-gradient(to top, #a6c1ee 0%, #fbc2eb 100%);
}

.team-members {
display: flex;
width: 300px;
flex-direction: row;
align-items: center;
}

.team-members-list {
margin-left: 32px;
}

.team-members-list ul {
list-style: none;
margin: 0;
padding: 0;
}

.team-members-list li {
margin-bottom: 8px;
}

.add-member-button {
  margin-left: 16px;
}


</style>


