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
  methods: {
    copyLink: function (e) {
      navigator.clipboard.writeText(
        "https://aloha.herokuapp.com/register/" + e
      );
      alert("Link Copied to ClipBoard");
    },
  },
  mounted() {
    this.$store.dispatch("GET_EVENTS");
  },
};
</script>

<template>
  <div class="event-container m-0 flex row">
    <div class="col-sm-12 card bg-transparent border-0 p-0 col-sm-6">
      <h1 class="brand p-5">Events</h1>
    </div>
    <div
      class="col-sm-4 card border py-2 bg-dark text-light"
      v-for="event in events"
      :key="event.id"
    >
      <div class="p-2 text-center">
        <h3 class="brand">{{ event.name }}</h3>
      </div>
      <hr />
      <p class="brand-2 brand-small text-center">
				<span v-html="event.short_description.replace(/(?:\r\n|\r|\n)/g, '<br />')"></span>
        <br />
        <br />
        <a class="btn brand-2 btn-primary register-btn">
          <router-link
            class="text-light"
            :to="{ name: 'Register', params: { id: event.id } }"
            >Register</router-link
          >
        </a>
      </p>
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
.brand-small {
  font-size: 14px;
}
</style>
