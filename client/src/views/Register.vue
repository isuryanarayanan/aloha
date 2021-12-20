<script>
export default {
  name: "Register",
  components: {},
  props: ["id"],
  data() {
    return {
      event: "",
      asietId: "",
      message: "",
			message_part:""
    };
  },
  mounted() {
    this.$store.dispatch("GET_EVENT", this.id).then((e) => {
      this.event = JSON.parse(e.response);
    });
  },
  methods: {
    renderMessage: function (part, msg) {
      this.message = msg;
      this.message_part = part;
    },
    registerForEvent: async function () {
      console.log(this.asietId);
      await this.handleClickSignIn();
    },
    async handleClickSignIn() {
      try {
        const googleUser = await this.$gAuth.signIn();
        if (!googleUser) {
          return null;
        }
        console.log(googleUser.getBasicProfile().getEmail());
        console.log(googleUser.getBasicProfile().getName());
        var token = googleUser.getAuthResponse();
        var id_token = token["id_token"];
        this.$store
          .dispatch("LOGIN", {
            oauth_token: id_token,
            asiet_id: this.asietId,
            event_id: this.event.id,
          })
          .then((e) => {
            if (e.status == 200) {
              this.renderMessage(
                "Success",
                "Registered as " +
                  this.asietId +
                  "@" +
                  googleUser.getBasicProfile().getEmail()
              );
            } else {
              this.renderMessage("Danger", "Uh oh!");
            }
            this.handleClickSignOut();
          });
      } catch (error) {
        console.error(error);
        return null;
      }
    },
    async handleClickSignOut() {
      try {
        await this.$gAuth.signOut();
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<template>
  <div class="container">
    <div class="row">
      <div class="card bg-transparent border-0">
        <h5 class="card-header display-4">{{ event.name }}</h5>
        <div class="card-body">
          <h5 class="card-title">{{ event.timing }}</h5>
          <p class="card-text">{{ event.description }}</p>

          <input
            name="id"
            v-model="asietId"
            placeholder="Enter your phone number"
          />
          <a href="#" @click="registerForEvent" class="btn m-1 btn-primary"
            >Register</a
          >

					<br>
{{message}}
					<hr/>
          <p class="muted">Organizers : {{ event.organizers }}</p>
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
</style>
