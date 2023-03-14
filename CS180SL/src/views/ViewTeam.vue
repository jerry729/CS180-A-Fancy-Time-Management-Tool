<template>
  <div class="team-page">
    <h1 class="title">My Team</h1>
    <ul class="members">
      <li v-for="member in team" :key="member.id" class="member">
        <h3 class="name">{{ member.name }}</h3>
        <p class="role">{{ member.role }}</p>
        <button class="remove-btn" @click="removeMember(member.id)">Remove</button>
      </li>
      <li v-if="team.length < 4 && !showAddMember" class="add-member">
        <h3 class="name"><a @click="showAddMember = true">+ Add New Member</a></h3>
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
.team-page {
  background-color: #f9c8a6;
  color: #383838;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 2rem;
}

.title {
  font-size: 3rem;
  margin-bottom: 2rem;
  text-align: center;
}

.members {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  list-style-type: none;
  margin: 0;
  padding: 0;
  width: 100%;
}

.member {
  background-color: #d1eecc;
  border-radius: 1rem;
  margin: 1rem;
  padding: 2rem;
  text-align: center;
  transition: all 0.2s ease;
  flex: 0 1 calc(25% - 2rem);
  max-width: calc(25% - 2rem);
}

.member:hover {
  transform: translateY(-0.5rem);
}

.name {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #f94144;
}

.role {
  font-size: 1.5rem;
  color: #4d4d4d;
}

.add-member-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 2rem;
}

.add-member-form .form-item {
  display: flex;
  flex-direction: column;
  margin-bottom: 1rem;
  width: 100%;
  max-width: 25rem;
}

.add-member-form .form-item label {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.add-member-form .form-item input {
  font-size: 1.5rem;
  padding: 0.5rem;
  border-radius: 0.5rem;
  border: none;
  background-color: #f5f5f5;
  color: #4d4d4d;
}

.add-member-form .form-item button {
  font-size: 1.5rem;
  padding: 0.5rem;
  border-radius: 0.5rem;
  border: none;
  background-color: #f94144;
  color: white;
  cursor: pointer;
  transition: all 0.2s ease;
  margin-top: 1rem;
}

.add-member-form .form-item button:hover {
  background-color: #f3722c;
}

.add-member {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 2rem;
  flex: 0 1 100%;
  max-width: 100%;
}

.add-member .name a {
  font-size: 2rem;
  color: #f94144;
  text-decoration: none;
  transition: all 0.2s ease;
}

.add-member .name a:hover {
  color: #f3722c;
}

@media only screen and (max-width: 768px) {
  .member {
    flex: 0 1 calc(50% - 2rem);
    max-width: calc(50% - 2rem);
  }
}

@media only screen and (max-width: 576px) {
  .member {
    flex: 0 1 calc(100% - 2rem);
    max-width:
    calc(100% - 2rem);
}
.add-member-form .form-item {
max-width: 100%;
}

.add-member {
flex-direction: row;
margin-top: 1rem;
}

.add-member .name {
flex: 1;
}

.add-member .name a {
font-size: 1.5rem;
}

.add-member-form .form-item button {
margin-top: 0;
}
}
</style>