import Vuex from "vuex";

const store = new Vuex.Store({
  state: {
    events: [],
  },
  getters: {
    getEvents: (state) => {
      return state.events;
    },
  },
  mutations: {
    set_events: function (state, arg) {
      state.events = arg;
    },
  },
  actions: {
    GET_EVENTS: function ({ getters, dispatch, commit }) {
      let xhr = new XMLHttpRequest();
      let promise = new Promise((resolve, reject) => {
				xhr.open("GET", "https://alohaasiet.pythonanywhere.com/organizer/event");
        xhr.setRequestHeader("Content-Type", "Application/json");

        xhr.onload = () => {
          resolve(xhr);
        };

        xhr.onerror = () => {
          reject(xhr);
        };
        xhr.send();
      });
      promise.then((e) => {
        commit("set_events", JSON.parse(e.response));
      });
      return promise;
    },
    GET_EVENTS_DETAILS: function ({ getters, dispatch, commit }, id) {
      let xhr = new XMLHttpRequest();
      let promise = new Promise((resolve, reject) => {
        xhr.open(
          "GET",
					"https://alohaasiet.pythonanywhere.com/organizer/event/registered/" + id + ""
        );
        xhr.setRequestHeader("Content-Type", "Application/json");

        xhr.onload = () => {
          resolve(xhr);
        };

        xhr.onerror = () => {
          reject(xhr);
        };
        xhr.send();
      });
      //promise.then((e) => {
      //commit("set_events", JSON.parse(e.response));
      //});
      return promise;
    },
    GET_EVENT: function ({ getters, dispatch, commit }, id) {
      let xhr = new XMLHttpRequest();
      let promise = new Promise((resolve, reject) => {
				xhr.open("GET", "https://alohaasiet.pythonanywhere.com/organizer/event/" + id + "/");
        xhr.setRequestHeader("Content-Type", "Application/json");

        xhr.onload = () => {
          resolve(xhr);
        };

        xhr.onerror = () => {
          reject(xhr);
        };
        xhr.send();
      });

      return promise;
    },
    LOAD_USER_GOOGLE: function () {},
    LOAD_USER_SERVER: function () {},
    LOGIN: function ({ getters, dispatch, commit }, params) {
      let xhr = new XMLHttpRequest();
      let promise = new Promise((resolve, reject) => {
				xhr.open("POST", "https://alohaasiet.pythonanywhere.com/oauth/google/");
        xhr.setRequestHeader("Content-Type", "Application/json");

        xhr.onload = () => {
          resolve(xhr);
        };

        xhr.onerror = () => {
          reject(xhr);
        };
        xhr.send(JSON.stringify(params));
      });
      return promise;
    },
  },
});

export default store;
