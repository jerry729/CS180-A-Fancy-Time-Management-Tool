<template>
  <div class ="page-container">
    <div class="team-page">
      <h1 class="title">My Team</h1>
      <ul class="members">
        <li v-for="member in team" :key="member.id" class="member">
          <h3 class="name">{{ member.name }}</h3>
          <p class="role">{{ member.role }}</p>
          <button class="remove-btn" @click="removeMember(member.id)">Remove</button>
        </li>
        <li v-if="team.length < 4 && !showAddMember" class="add-member">
          <h3 class="name" color = "blue"><a @click="showAddMember = true">+ Add New Member</a></h3>
        </li>
        <li v-if="showAddMember" class="add-member-form">
          <h3 class="name">Add New Member</h3>
          <form @submit.prevent="addMember">
            <div class="form-item">
              <label for="name">Name:</label>
              <input type="text" id="name" v-model="newMember.name" required>
            </div>
            <div class="form-item">
              <label for="role">Role:</label>
              <input type="text" id="role" v-model="newMember.role" required>
            </div>
            <div class="form-item">
              <button type="submit">Add Member</button>
              <button type="button" @click="cancelAddMember">Cancel</button>
            </div>
          </form>
        </li>
      </ul>
      <router-link to="/" class="back-btn">&#8592; Back to Schedule</router-link>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, ref } from 'vue';
import { message } from 'ant-design-vue';

interface TeamMember {
  id: number;
  name: string;
  role: string;
}

export default defineComponent({
  setup() {
    const team = reactive<TeamMember[]>([
      { id: 1, name: 'Xingyan', role: 'Backend' },
      { id: 2, name: 'Zhaorui', role: 'Backend' },
      { id: 3, name: 'Chenlong', role: 'Frontend' },
      { id: 4, name: 'Nathanael', role: 'Frontend' },
    ]);

    const newMember = reactive<TeamMember>({
      id: 0,
      name: '',
      role: '',
    });

    const showAddMember = ref(false);

    const addMember = () => {
      const member = {
        id: team.length + 1,
        name: newMember.name,
        role: newMember.role,
      };
      team.push(member);
      message.success('Team member added successfully');
      showAddMember.value = false;
      newMember.name = '';
      newMember.role = '';
    };

    const cancelAddMember = () => {
      showAddMember.value = false;
      newMember.name = '';
      newMember.role = '';
    };

    const removeMember = (id: number) => {
      const index = team.findIndex((member) => member.id === id);
      if (index !== -1) {
        team.splice(index, 1);
        message.success('Team member removed successfully');
      }
    };

    return { team, newMember, showAddMember, addMember, cancelAddMember, removeMember};
  },
});
</script>
<style scoped>
.view-team-container {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  font-size: 16px;
  color: black;
  background-color: #f2f2f2;
}

a {
  text-decoration: none;
  color: black;
}

h1, h2, h3, h4, h5, h6 {
  margin: 0;
  padding: 0;
  font-weight: normal;
}

ul {
  margin: 0;
  padding: 0;
  list-style: none;
}

/* Header styles */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  padding: 20px;
}

.logo {
  font-size: 24px;
  font-weight: bold;
}

.nav-links {
  display: flex;
  align-items: center;
}

.nav-link {
  margin-left: 20px;
}

/* Team page styles */
.team-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  border-radius: 10px;
}

.title {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 40px;
  text-align: center;
}

.members {
  display: flex;
  flex-wrap: wrap;
  margin: -10px;
}

.member {
  flex: 1 0 25%;
  margin: 10px;
  padding: 20px;
  background-color: #f9f9f9;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  border-radius: 10px;
}

.name {
  font-size: 24px;
  font-weight: bold;
}

.role {
  margin-top: 10px;
  color: blue;
}

.remove-btn {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #333;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.remove-btn:hover {
  background-color: #222;
}

.add-member-form {
  flex: 1 0 100%;
  margin: 10px;
  padding: 20px;
  background-color: gray;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  border-radius: 10px;
}

.form-item {
  margin-bottom: 20px;
}

.page-container {
  display: fixed;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%
}

label {
  display: block;
  margin-bottom: 5px;
}

input[type="text"] {
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 100%;
  box-sizing: border-box;
}

button[type="submit"], button[type="button"] {
  padding: 10px 20px;
  background-color: #333;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
  transition: background-color 0.3s ease;
}

button[type="submit"]:hover, button[type="button"]:hover {
  background-color: #222;
}

button[type="submit"]:focus, button[type="button"]:focus {
  outline: none;
  box-shadow: 0 0 0 2px #ccc;
}
</style>