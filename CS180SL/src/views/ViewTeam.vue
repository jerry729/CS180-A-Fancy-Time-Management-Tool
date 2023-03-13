<template>
    <div class="team-page">
      <h1 class="title">My Team</h1>
      <div class="members">
        <div v-for="member in team" :key="member.id" class="member">
          <h3 class="name">{{ member.name }}</h3>
          <p class="role">{{ member.role }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, reactive } from 'vue';
  
  interface TeamMember {
    id: number;
    name: string;
    role: string;
  }
  
  export default defineComponent({
    setup() {
      const team = reactive<TeamMember[]>([
        { id: 1, name: 'John', role: 'Developer' },
        { id: 2, name: 'Sarah', role: 'Designer' },
        { id: 3, name: 'David', role: 'Project Manager' },
        { id: 4, name: 'Alice', role: 'QA Engineer' },
      ]);
  
      return { team };
    },
  });
  </script>
  
  <style scoped>
  .team-page {
    background-color: #f9c8a6;
    color: #383838;
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
    margin-top: 2rem;
  }
  
  .member {
    background-color: #d1eecc;
    border-radius: 1rem;
    margin-right: 2rem;
    margin-bottom: 2rem;
    padding: 2rem;
    text-align: center;
    transition: all 0.2s ease;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
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
  </style>