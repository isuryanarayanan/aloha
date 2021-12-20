<template>
  <div>
    <button
      @click="handleClickSignIn"
      :disabled="!Vue3GoogleOauth.isInit || Vue3GoogleOauth.isAuthorized"
    >
      sign in
    </button>
  </div>
</template>

<script>
import { inject } from "vue";
export default {
  name: "SignIn",
  data() {
    return {
      user: "",
    };
  },
  methods: {
    async handleClickSignIn() {
      try {
        const googleUser = await this.$gAuth.signIn();
        if (!googleUser) {
          return null;
        }
        this.user = googleUser.getBasicProfile().getEmail();
        var token = googleUser.getAuthResponse();
        var id_token = token["id_token"];
        /*console.log("getBasicProfile", googleUser.getAuthResponse());*/

        let xhr = new XMLHttpRequest();
        xhr.open("POST", "http://alohaasiet.pythonanywhere.com/oauth/google/");
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onload = function () {
          console.log("Signed in as: " + xhr.responseText);
        };
        let send_params = { oauth_token: id_token };
        console.log("Sending: " + send_params);
        xhr.send(JSON.stringify(send_params));

        xhr.then((res)=>{
            console.log(res)
        })

      } catch (error) {
        //on fail do something
        console.error(error);
        return null;
      }
    },
  },
  setup(props) {
    const Vue3GoogleOauth = inject("Vue3GoogleOauth");
    return {
      Vue3GoogleOauth,
    };
  },
};
</script>

<style>
button {
  display: inline-block;
  line-height: 1;
  white-space: nowrap;
  cursor: pointer;
  background: #fff;
  border: 1px solid #dcdfe6;
  color: #606266;
  -webkit-appearance: none;
  text-align: center;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  outline: 0;
  margin: 0;
  -webkit-transition: 0.1s;
  transition: 0.1s;
  font-weight: 500;
  padding: 12px 20px;
  font-size: 14px;
  border-radius: 4px;
  margin-right: 1em;
}
button:disabled {
  background: #fff;
  color: #ddd;
  cursor: not-allowed;
}
</style>