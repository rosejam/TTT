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
import { mapActions } from "vuex";
export default {
  async created() {
    await this.init();
  },
  methods: {
    ...mapActions("user", ["getUserInfo"]),
    
    async init() {

      // 새로고침 시 state 초기화 방지
      if(localStorage.getItem("user_token")) {
        await this.getUserInfo();
      }

    }
  },
};
</script>
