<script>
import { mapGetters } from "vuex";

export default {
  name: "Events",
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
.event-container {
  overflow-x: hidden;
  height: 100%;
  width: 100%;
}
.event-card {
  width: 100%;
}
</style>
