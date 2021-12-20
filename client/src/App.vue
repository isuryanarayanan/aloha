<script>
import Navbar from "./components/Navbar.vue";
import { inject } from "vue";
export default {
  name: "App",
  components: {
    Navbar,
  },
  data() {
    return {
      googleOauth: null,
    };
  },
  setup() {
    const Vue3GoogleOauth = inject("Vue3GoogleOauth");
    return {
      Vue3GoogleOauth,
    };
  },
  computed: {
    logOauth: function () {
      if (this.Vue3GoogleOauth.isInit && this.Vue3GoogleOauth.isAuthorized) {
        console.log(this.$store.getters.getUser);
      }
    },
  },
  mounted() {},
};
</script>

<template>
  <div class="app">
    {{ logOauth }}
    <Navbar />
    <router-view></router-view>
  </div>
</template>
<style>
#app {
  width: 100%;
  min-height: 100vh;
  height: 100%;
  background-image: linear-gradient(to top, #cfd9df 0%, #e2ebf0 100%);
}
</style>
