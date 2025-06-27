<template>
  <div id="app-container">
    <!-- …existing content… -->
    <ExampleComponent></ExampleComponent>
    <!-- Use Vue’s <Suspense> to show a fallback while downloading -->
    <Suspense>
      <template #default>
        <SplitLoadedComponent />
      </template>
      <template #fallback>
        <div class="loading-placeholder">Loading extra feature…</div>
      </template>
    </Suspense>
  </div>
</template>

<script>
import { defineAsyncComponent } from 'vue';
import ExampleComponent from "./components/ExampleComponent";

export default {
  name: 'App',
  components: {
    ExampleComponent,
    // here’s the lazy component:
    SplitLoadedComponent: defineAsyncComponent(() =>
      import('./components/SplitLoadedComponent.vue')
    )
  },
  props: {
    fromDjango: {
      type: String,
      default() {
        return "This is the default value - not provided by Django";
      }
    }
  }
}
</script>

<style scoped>
body {
  margin: 0px !important;
}
#app-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 0px;
  margin: 0px;
  min-height: 100vh;
  /* Static, multi-color gradient background */
  background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fad0c4, #ff9a9e);
  color: white;
  text-align: center;
}

.app-title {
  font-size: 2rem;
  margin: 0;
  text-shadow: 0 4px 6px rgba(0,0,0,0.2);
}

.app-prop {
  font-size: 1.25rem;
  margin: 1rem 0 2rem;
}

.component-card {
  background: rgba(255, 255, 255, 0.85);
  border-radius: 1rem;
  padding: 2rem;
  box-shadow: 0 8px 16px rgba(0,0,0,0.2);
}
</style>
