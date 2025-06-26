<template>
  <div class="example-container">
    <h1 class="title">🎉 Example Component 🎉</h1>
    <button class="action-button">Click Me!</button>
  </div>
</template>

<script>
export default {
  name: "ExampleComponent"
}
</script>

<style scoped>
.example-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  /* 4-color gradient that shifts */
  background: linear-gradient(45deg, #ff6ec4, #7873f5, #4ade80, #facc15);
  background-size: 400% 400%;
  animation: gradientShift 10s ease infinite;
  border-radius: 1rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.2);
  text-align: center;
}

.title {
  font-size: 2rem;
  color: white;
  text-shadow: 0 0.25rem 0.5rem rgba(0, 0, 0, 0.3);
  margin: 0;
  animation: bounce 2s infinite;
}

.action-button {
  margin-top: 1.5rem;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  font-weight: bold;
  color: #333;
  background: white;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
}

.action-button:hover {
  transform: scale(1.05);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.2);
}
</style>
