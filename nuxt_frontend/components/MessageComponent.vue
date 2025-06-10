<template>
  <div>
    <h1>Message from Python Backend:</h1>
    <h2>{{ message }}</h2>
  </div>
</template>

<script setup>
const { data } = useFetch("/api/message", { server: false });
const message = computed(() => data.value?.message ?? "Loading...");
</script>
