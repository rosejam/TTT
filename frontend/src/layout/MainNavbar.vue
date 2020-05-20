<template>
  <navbar
    position="fixed"
    type="primary"
    :transparent="transparent"
    :color-on-scroll="colorOnScroll"
    menu-classes="ml-auto"
  >
    <template slot-scope="{ toggle, isToggled }">
      <router-link v-popover:popover1 class="navbar-brand" to="/">
        auto trading system
      </router-link>
      <el-popover
        ref="popover1"
        popper-class="popover"
        placement="bottom"
        width="200"
        trigger="hover"
      >
        <div class="popover-body">
          Move to Main
        </div>
      </el-popover>
    </template>
    <template slot="navbar-menu">
      <li v-if="userLogined" class="nav-item">
        <a
          class="nav-link"
          href="/stockinfo"
        >
          <i class="now-ui-icons ui-1_zoom-bold"></i>
          <p>증권 정보</p>
        </a>
      </li>
      <drop-down
              v-if="userLogined"
              tag="li"
              title="자산 관리"
              icon="now-ui-icons business_bank"
              class="nav-item"
      >
        <nav-link to="/asset">
          <!-- <i class="fa fa-chart-line"></i> 자산 현황 -->
          <i class="now-ui-icons business_money-coins"></i> 자산 현황
        </nav-link>
        <nav-link to="/tr_history">
          <i class="now-ui-icons files_paper"></i> 거래 내역
        </nav-link>
        <nav-link to="/algosetting">
          <i class="now-ui-icons ui-2_settings-90"></i> 알고리즘 설정
        </nav-link>
      </drop-down>
      <li v-if="userLogined" class="nav-item">
        <a
          class="nav-link"
          href="/algomarket"
        >
          <i class="now-ui-icons shopping_shop"></i>
          <p>알고리즘 마켓</p>
        </a>
      </li>
      <li v-if="userLogined" class="nav-item">
        <a
          class="nav-link"
          href="/profile"
        >
          <i class="now-ui-icons users_single-02"></i>
          <p>내정보</p>
        </a>
      </li>
      <li class="nav-item" v-if="!userLogined">
        <nav-link
          class="nav-link btn btn-neutral"
          to="/login">
          <p>로그인</p>
        </nav-link>
      </li>
      <li class="nav-item" v-else>
        <!-- <nav-link
          class="nav-link btn btn-neutral"
          to="/"
          @click="logout">
          <p>로그아웃</p>
        </nav-link> -->
        <n-button
          @click="logout"
          type="neutral"
        >
          로그아웃
        </n-button>
      </li>
      <li class="nav-item">
        <a
          class="nav-link"
          rel="tooltip"
          title="Follow us on Twitter"
          data-placement="bottom"
          href="https://twitter.com/CreativeTim"
          target="_blank"
        >
          <i class="fab fa-twitter"></i>
          <p class="d-lg-none d-xl-none">Twitter</p>
        </a>
      </li>
      <li class="nav-item">
        <a
          class="nav-link"
          rel="tooltip"
          title="Like us on Facebook"
          data-placement="bottom"
          href="https://www.facebook.com/CreativeTim"
          target="_blank"
        >
          <i class="fab fa-facebook-square"></i>
          <p class="d-lg-none d-xl-none">Facebook</p>
        </a>
      </li>
      <li class="nav-item">
        <a
          class="nav-link"
          rel="tooltip"
          title="Follow us on Instagram"
          data-placement="bottom"
          href="https://www.instagram.com/CreativeTimOfficial"
          target="_blank"
        >
          <i class="fab fa-instagram"></i>
          <p class="d-lg-none d-xl-none">Instagram</p>
        </a>
      </li>
    </template>
  </navbar>
</template>

<script>
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
      userLogined: false
    }
  },
  mounted() {
    this.logined;
  },
  computed: {
    logined() {
      console.log(firebase.auth().currentUser);
      firebase.auth().onAuthStateChanged(user => {
        if(user) {
          this.userLogined = true;
        }
        else {
          this.userLogined = false;
        }
      })
    }
  },
  methods: {
    logout() {
      firebase.auth().signOut()
              .then(() => {
                this.$router.replace("/");
              })
              .catch;
    }
  },
};
</script>

<style scoped></style>
