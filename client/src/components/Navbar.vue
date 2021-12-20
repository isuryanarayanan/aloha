<script>
export default {
  name: "Navbar",
};
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light px-5">
    <a class="navbar-brand" href="#">
      <img
        src="../assets/aloha-logo-little.png"
        width="90"
        height="90"
        class="d-inline-block mx-5"
        alt=""
      />
    </a>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarText"
      aria-controls="navbarText"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarText">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item btn">
          <router-link class="nav-link" to="/">Home</router-link>
        </li>
        <li class="nav-item btn">
          <router-link class="nav-link" to="/events">Events</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<style scoped></style>
