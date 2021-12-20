import { createApp } from "vue";
import router from "./router/index";
import store from "./store/index";
import App from "./App.vue";
import gAuthPlugin from "vue3-google-oauth2";

var development =
  "1027589441319-hc37u1500vd6p3engsq9pgcllcstfs4l.apps.googleusercontent.com";
var deployment =
	"1027589441319-13rlrl6k4hlht32in3a90m8nm3jt9aab.apps.googleusercontent.com";

const gAuthOptions = {
	clientId: deployment,
  scope: "profile email openid",
  prompt: "consent",
  fetch_basic_profile: false,
};

const app = createApp(App);
app.use(gAuthPlugin, gAuthOptions);
app.use(router);
app.use(store);
app.mount("#app");
