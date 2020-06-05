<template>
  <navbar
    position="fixed"
    type="primary"
    :transparent="transparent"
    :color-on-scroll="colorOnScroll"
    menu-classes="ml-auto"
  >
    <template>
      <router-link class="navbar-brand" to="/">
        <img v-if="$route.path != '/'" class="n-logo" src="img/TTT-logo.png" alt="" style="width:40px; height:auto"/>
      </router-link>
    </template>
    <template slot="navbar-menu">

      <!-- 테스트 페이지 이동 버튼 -->
      <li class="nav-item">
          <router-link class="navbar-brand" to="/testing">
            <i class="now-ui-icons design-2_ruler-pencil"></i> 테스트
          </router-link>
      </li>

      <!-- 포트폴리오 페이지 이동 버튼 -->
      <li v-if="userInfo.uid!=null" class="nav-item">
          <router-link class="navbar-brand" to="/portfolio">
            <i class="now-ui-icons files_paper"></i> 내 포트폴리오
          </router-link>
      </li>

      <!-- 로그인 버튼 -->
      <li class="nav-item" v-if="userInfo.uid==null">
        <n-button
          @click="$router.push('/login')"
          type="neutral"
        >
          로그인
        </n-button>
      </li>

      <!-- 로그아웃 버튼 -->
      <li class="nav-item" v-else>
        <n-button
          @click="logout"
          type="neutral"
        >
          로그아웃
        </n-button>
      </li>
    </template>
  </navbar>
</template>

<script>
import { mapState, mapMutations } from "vuex";
import { Navbar, Button } from '@/components';
import firebase from 'firebase';

export default {
  name: 'main-navbar',
  props: {
    transparent: Boolean,
    colorOnScroll: Number
  },
  components: {
    Navbar,
    [Button.name]: Button,
  },
  data() {
    return {
    }
  },
  computed: {
    ...mapState("user", ["userInfo"]),
  },
  methods: {
    ...mapMutations("user", ["setUserInfo"]),

    // 로그아웃
    logout() {
      firebase.auth().signOut()
              .then(() => {
                // user state 비워줌
                this.setUserInfo(null);
                // localStorage에 저장되어있는 정보 삭제
                localStorage.removeItem("user");
                localStorage.removeItem("user_token");
                // 에러 처리
                this.$router.replace("/").catch(err => {
                  if(err.name != "NavigationDuplicated" ){
                    throw error;
                  }
                });
              });
      
    }
  },
};
</script>

<style scoped>
  [v-cloak] {
    display: none;
  }
</style>
