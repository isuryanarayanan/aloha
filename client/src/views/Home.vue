<script>
import { mapGetters } from "vuex";

export default {
  name: "Home",
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
  <div class="row m-0">
    <div class="col-sm-12 text-center bg-dark">
      <div class="brand text-light py-3">
        <h4>DEPARTMENT OF</h4>
        <h1>COMPUTER SCIENCE AND ENGG.</h1>
        <h4>PRESENTS</h4>
      </div>
      <img class="image-banner" src="../assets/aloha-logo-little-1.png" />
    </div>

    <div class="col-sm-12 card bg-transparent border-0 about text-center">
      <div class="">
        <figure
          class="bg-dark p-3 py-5 rounded text-light"
          style="
            border-right: 0.5rem solid #a34e78;
            border-left: 0.5rem solid #a34e78;
          "
        >
          <blockquote class="blockquote about-brand pb-2">
            <p class="brand-2 brand-small ">
              Aloha, a frosty, congenial fiesta organized by the CSE Department
              of Adi Shankara Institute of Engineering and Technology, Kalady is
              the much awaited one-day extravaganza of the year and is all set
              to commence on 23rd December, 2021. It is a concoction of art, fun
              and learning that invokes this Christmas time with much vibe and
              efficacy. This post Covid'19 event is a symbol of great
              expectation, excitement and endowment for each computer science
              student bringing them all under a single screen and enjoying the
              celebration together. Filled with a set of top-notch technical and
              non-technical events, games and competitions that arouse your
              competency and a multitude of surprises, Aloha marks the year-end
              with much desired contentment and fondness. Aloha sets a platform
              for the students to network and know their peers and seniors,
              thus, creating a bewitching bonds between them.
            </p>
          </blockquote>
          <figcaption class="blockquote-footer mb-0 font-italic">
            Team
          </figcaption>
        </figure>
      </div>
    </div>
    <div class="col-sm-12 card bg-transparent border-0 p-0">
      <h1 class="brand p-5">Events</h1>
    </div>
    <div class="col-sm-12 row m-auto">
      <div
        class="col-sm-4 border py-2 bg-dark text-light"
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
              >Register here</router-link
            >
          </a>
        </p>
      </div>
    </div>

    <footer class="w-100 contact-footer flex-shrink-0">
      <div class="row text-center pb-5">
        <div class="col-sm-4"></div>
        <div class="col-sm-4 row text-center">
          <div class="rounded-link col-4 m-auto">
            <a href="https://www.instagram.com/cseasiet"
              ><i class="fa fa-instagram" aria-hidden="true"></i
            ></a>
          </div>
          <div class="rounded-link col-4 m-auto">
            <a href="https://www.linkedin.com/company/department-of-cse-asiet"
              ><i class="fa fa-linkedin" aria-hidden="true"></i
            ></a>
          </div>
          <div class="rounded-link col-4 m-auto">
            <a href="https://www.facebook.com/CSEASIET"
              ><i class="fa fa-facebook" aria-hidden="true"></i
            ></a>
          </div>
        </div>
        <div class="col-sm-4"></div>
      </div>
      <div class="row text-center pt-5">
        <div class="col-sm-4">
          <h5 class="h1 brand text-dark">Sidharth</h5>
          <p class="small text-muted">
            K Sidharth <br />
            +91 89211 46719
          </p>
          <p class="small text-muted mb-0">@ Event Organizer</p>
          <hr />
        </div>
        <div class="col-sm-4">
          <h5 class="h1 brand text-dark">Fayis</h5>
          <p class="small text-muted">
            Mohammed Fayis E<br />
            +91 96453 15315
          </p>
          <p class="small text-muted mb-0">@ Event Organizer</p>
          <hr />
        </div>
        <div class="col-sm-4">
          <h5 class="h1 brand text-dark">Surya</h5>
          <p class="small text-muted">
            Surya Narayanan<br />
            a.suryanarayanan2000@gmail.com
          </p>
          <p class="small text-muted mb-0">
            <a class="text-primary" href="https://github.com/isuryanarayanan"
              >@ Developer</a
            >
          </p>
          <hr />
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.contact-footer {
  margin-top: 100px;
}
.rounded-link {
  background: #222;
  width: 50px;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 100%;
}
.rounded-link a {
  color: white;
}
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
  margin-bottom: 100px;
}
.about {
  margin-top: 5%;
}

.brand-small {
  font-size: 14px;
}
.about-brand{
	padding-left: 10%;
	padding-right: 10%;
}
</style>
