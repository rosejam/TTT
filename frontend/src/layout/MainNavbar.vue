<template>
  <navbar
    position="fixed"
    type="primary"
    :transparent="transparent"
    :color-on-scroll="colorOnScroll"
    menu-classes="ml-auto"
  >
    <template slot-scope="{ toggle, isToggled }">
      <router-link class="navbar-brand" to="/">
        Tiny Testing Tool
      </router-link>
    </template>
    <template slot="navbar-menu">

      <!-- 테스트 페이지 이동 버튼 -->
      <li class="nav-item">
          <!-- <n-button type="neutral" link @click="$router.push('/testing')">
            <i class="now-ui-icons design-2_ruler-pencil"></i> 테스트
          </n-button> -->
          <router-link class="navbar-brand" to="/testing">
            <i class="now-ui-icons design-2_ruler-pencil"></i> 테스트
          </router-link>
      </li>

      <!-- 포트폴리오 페이지 이동 버튼 -->
      <li v-if="userInfo.email!=null" class="nav-item">
          <router-link class="navbar-brand" to="/portfolio">
            <i class="now-ui-icons files_paper"></i> 내 포트폴리오
          </router-link>
      </li>

      <!-- 내 정보 페이지 이동 버튼 -->
      <li v-if="userInfo.email!=null" class="nav-item">
        <router-link class="navbar-brand" to="/profile">
          <i class="now-ui-icons users_single-02"></i> 내 정보
        </router-link>
      </li>

      <!-- 로그인 버튼 -->
      <li class="nav-item" v-if="userInfo.email==null">
        <nav-link
          class="nav-link btn btn-neutral"
          to="/login">
          <p>로그인</p>
        </nav-link>
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
import { mapState, mapActions, mapMutations } from "vuex";
import { DropDown, NavbarToggleButton, Navbar, NavLink, Button } from '@/components';
import { Popover } from 'element-ui';
import firebase from 'firebase';

export default {
  name: 'main-navbar',
  props: {
    transparent: Boolean,
    colorOnScroll: Number
  },
  components: {
    DropDown,
    Navbar,
    NavbarToggleButton,
    NavLink,
    [Button.name]: Button,
    [Popover.name]: Popover,
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
