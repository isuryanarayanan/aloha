<script>
export default {
  name: "Navbar",
};
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-dark navbar-light px-5">
    <a class="navbar-brand" href="#"></a>
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
          <router-link class="nav-link text-light border-bottom" to="/"
            >Home</router-link
          >
        </li>
        <li class="nav-item btn">
          <router-link class="nav-link text-light border-bottom" to="/events"
            >Events</router-link
          >
        </li>
      </ul>
    </div>
  </nav>
</template>

<style scoped></style>
