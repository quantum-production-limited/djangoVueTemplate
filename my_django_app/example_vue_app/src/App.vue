<template>
  <h2>Props from Django:</h2>
  <p>{{fromDjango}}</p>
  <ExampleComponent />
</template>

<script>
import ExampleComponent from "./components/ExampleComponent";

export default {
  name: 'App',
  props: {
    fromDjango: {
      type: String,
      default() {return "This is the default value - not provided by Django"}
    }
  },
  components: {
    ExampleComponent,
  }
}
</script>

<style>
#example_vue_app_container {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 30px;
  flex: 1;
  display: flex;
  flex-flow: column nowrap;
}
</style>
