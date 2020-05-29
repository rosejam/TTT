<template>
  <div id="app">
    <router-view name="header" />
    <div class="wrapper" id="wrapper">
      <router-view />
    </div>
    <router-view name="footer" />
  </div>
</template>
<script>
import { mapState, mapActions, mapMutations } from "vuex";
export default {
  created() {
    this.init();
  },
  methods: {
    ...mapActions("user", ["setUser"]),
    async init() {
      await this.setUser();
    }
  },
};
</script>
