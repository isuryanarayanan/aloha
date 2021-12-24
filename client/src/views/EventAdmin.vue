<script>
export default {
  name: "Event",
  components: {},
  props: ["id"],
  data() {
    return {
      event: "",
      phone_number: "",
      semester: "",
      batch: "",
      team_input: "",
      team: [],
      username: "",
      message: "",
      message_part: "",
    };
  },
  mounted() {
    this.$store.dispatch("GET_EVENTS_DETAILS", this.id).then((e) => {
      this.event = JSON.parse(e.response);
      console.log(JSON.stringify(this.event));
    });
  },
  methods: {},
};
</script>

<template>
  <div class="">
    <table class="table table-striped table-dark">
      <thead>
        <tr>
          <th scope="col">email</th>
          <th scope="col">name</th>
          <th scope="col">phone</th>
          <th scope="col">semester</th>
          <th scope="col">batch</th>
        </tr>
      </thead>
      <tbody v-for="user in event" :key="user.id">
        <tr>
          <th scope="row">{{ user.email }}</th>
          <td>{{ user.name }}</td>
          <td>{{ user.phone }}</td>
          <td>{{ user.semester }}</td>
          <td>{{ user.batch }}</td>
          <div class="" v-if="user.team != 0">
					Team
					<hr>
            <div class="" v-for="m in user.team" :key="m[0]">
              {{ m }}
            </div>
          </div>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.container {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.brand {
  font-family: myFirstFont;
}
</style>
