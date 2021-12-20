import { createApp } from "vue";
import router from "./router/index";
import store from "./store/index";
import App from "./App.vue";
import gAuthPlugin from "vue3-google-oauth2";

const gAuthOptions = {
  clientId:
    "1027589441319-hc37u1500vd6p3engsq9pgcllcstfs4l.apps.googleusercontent.com",
  scope: "profile email openid",
  prompt: "consent",
  fetch_basic_profile: false,
};

const app = createApp(App);
app.use(gAuthPlugin, gAuthOptions);
app.use(router);
app.use(store);
app.mount("#app");
