<script>
import { mapGetters } from "vuex";

export default {
name: "Home",
  components: {},
  computed: {
    ...mapGetters({ events: "getEvents" }),
  },
  data() {
    return {};
  },
  mounted() {
    this.$store.dispatch("GET_EVENTS");
  },
};

</script>

<template>
  <div class="row m-0">
    <div class="col-sm-12 text-center bg-dark">
      <div class="brand">
        <p class="text-light brand-text">
          Department of computer science asiet presents,
        </p>
      </div>
      <img class="image-banner" src="../assets/aloha-logo-little-1.png" />
    </div>
  </div>
<div class="event-container text-center m-0 flex row">
    <div class="col-md-4" v-for="event in events" :key="event.id">
      <div class="card border-0 my-3">
        <h5 class="card-header display-4 ">{{ event.name }}</h5>
        <div class="card-body">
          <p class="card-title">{{ event.timing }}</p>
          <p class="muted">Organizers : {{ event.organizers }}</p>
          <div class="card-body">
            <router-link
              class="nav-link btn btn-primary text-light"
              :to="{ name: 'Register', params: { id: event.id } }"
              >Register</router-link
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.image-banner {
  /*position: absolute;*/
  width: 90%;
  top: 0;
  left: 0;
}
.brand-text {
  font-size: 40px;
  width: 100%;
  /*position: absolute;*/
}
</style>
