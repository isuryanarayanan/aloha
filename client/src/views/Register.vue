<script>
export default {
  name: "Register",
  components: {},
  props: ["id"],
  data() {
    return {
      event: "",
			phone_number:"",
			semester:"",
			batch:"",
      asietId: "",
      message: "",
      message_part: "",
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
      console.log(this.phone_number);
      console.log(this.semester);
      console.log(this.batch);
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
            phone_number: this.phone_number,
						semester:this.semester,
						batch:this.batch,
            event_id: this.event.id,
          })
          .then((e) => {
            if (e.status == 200) {
              this.renderMessage(
                "Success",
                "Registered as " +
                  this.phone_number+
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
        <h5 class="card-header display-4 brand">{{ event.name }}</h5>
        <div class="card-body">
          <h5 class="card-title">{{ event.timing }}</h5>
          <p class="card-text">{{ event.description }}</p>

          <div class="row">
            <div class="col-sm-6 card p-5">
              <div class="form-group">
                <label for="exampleInputEmail1">Phone Number</label>
                <input
                  type="text"
                  class="form-control"
                  id="exampleInputEmail1"
                  aria-describedby="emailHelp"
                  placeholder="Enter Phone Number"
									v-model="phone_number"
                />
                <small id="emailHelp" class="form-text text-muted"
                  >We'll never share your data with anyone else.</small
                >
              </div>
              <div class="form-group">
                <label for="exampleFormControlSelect1">Select semester</label>
                <select class="form-control" v-model="semester" id="exampleFormControlSelect1">
                  <option>1</option>
                  <option>3</option>
                  <option>5</option>
                  <option>7</option>
                </select>
              </div>
              <div class="form-group">
                <label for="exampleFormControlSelect2">Select batch</label>
                <select class="form-control" v-model="batch" id="exampleFormControlSelect2">
                  <option>1</option>
                  <option>2</option>
                </select>
              </div>
              <div class="form-group form-check">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="exampleCheck1"
                />
                <label class="form-check-label" for="exampleCheck1"
                  >Remember me</label
                >
              </div>
              <button @click="registerForEvent" type="submit" class="btn btn-primary">Submit</button>
            </div>
          </div>
          
          <br />
          {{ message }}
          <hr />
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
.brand {
  font-family: myFirstFont;
}
</style>
