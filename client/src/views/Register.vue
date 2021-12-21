<script>
export default {
  name: "Register",
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
    this.$store.dispatch("GET_EVENT", this.id).then((e) => {
      this.event = JSON.parse(e.response);
    });
  },
  methods: {
    addTeamMember: function () {
      this.team.push(this.team_input);
    },
    deleteTeamMember: function (index) {
      if (index > -1) {
        this.team.splice(index, 1);
      }
    },
    renderMessage: function (part, msg) {
      this.message = msg;
      this.message_part = part;
    },
    registerForEvent: async function () {
      await this.handleClickSignIn();
    },
    async handleClickSignIn() {
      try {
        const googleUser = await this.$gAuth.signIn();
        if (!googleUser) {
          return null;
        }
        var token = googleUser.getAuthResponse();
        var id_token = token["id_token"];
        var stt = "";
        if (this.team.length == 0) {
          stt = "none";
        } else {
          this.team.forEach((e) => {
            stt = stt + e + ",";
          });
        }

        this.$store
          .dispatch("LOGIN", {
            oauth_token: id_token,
            username: this.username,
            phone_number: this.phone_number,
            semester: this.semester,
            batch: this.batch,
            team: stt,
            event_id: this.event.id,
          })
          .then((e) => {
            if (e.status == 200) {
              this.renderMessage(
                "Success",
                "Registered as " +
                  this.phone_number +
                  "@" +
                  googleUser.getBasicProfile().getEmail()
              );
            } else {
              console.log(e.response);
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
          <h5 class="card-title">
            Time: {{ event.timing }} | venue: {{ event.venue }}
          </h5>
          <p class="card-text">
            <span
              v-html="event.description.replace(/(?:\r\n|\r|\n)/g, '<br />')"
            ></span>
          </p>

          <div class="">
            <div class="card p-5">
              <div class="form-group">
                <label for="exampleInputEmail3">Full Name</label>
                <input
                  type="text"
                  class="form-control"
                  id="exampleInputEmail1"
                  aria-describedby="emailHelp"
                  placeholder="Enter your name"
                  v-model="username"
                />
              </div>
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
                <select
                  class="form-control"
                  v-model="semester"
                  id="exampleFormControlSelect1"
                >
                  <option>1</option>
                  <option>3</option>
                  <option>5</option>
                  <option>7</option>
                </select>
              </div>
              <div class="form-group">
                <label for="exampleInputEmail2">Batch</label>
                <input
                  type="text"
                  class="form-control"
                  id="exampleInputEmail2"
                  aria-describedby="emailHelp"
                  placeholder="Enter batch Eg CSB, CSA"
                  v-model="batch"
                />
              </div>
              <div v-if="event.team_based" class="form-group">
                <label for="exampleInputEmail2">Add Team Member</label>
                <input
                  type="text"
                  class="form-control"
                  id="exampleInputEmail2"
                  aria-describedby="emailHelp"
                  placeholder="Enter member name and phone number"
                  v-model="team_input"
                />
                <div class="btn btn-success" @click="addTeamMember()">add</div>
                <div class="" v-for="member in team" :key="member">
                  <hr />
                  <div
                    class="btn btn-sm btn-danger"
                    @click="deleteTeamMember(team.indexOf(member))"
                  >
                    delete
                  </div>
                  {{ member }}
                </div>
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
              <button
                @click="registerForEvent"
                type="submit"
                class="btn btn-primary"
              >
                Submit
              </button>
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
