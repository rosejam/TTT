import Vue from 'vue';
import Router from 'vue-router';
// 메인 페이지
import Index from './pages/Index.vue';
// 로그인 페이지
import Login from './pages/Login.vue';
// 테스트 페이지
import Testing from './pages/Testing.vue';
// 포트폴리오
import Portfolio from './pages/Portfolio.vue';
// 내 정보 페이지
import Profile from './pages/Profile.vue';
// 서비스 이용약관 페이지
import Term from './pages/Term.vue';
// 네비게이션 바
import MainNavbar from './layout/MainNavbar.vue';
// 푸터
import MainFooter from './layout/MainFooter.vue';

import Chart_practice from './pages/Chart_practice.vue'
import practice from './pages/practice.vue'
import Chart_practice2 from './pages/Chart_practice2.vue'

Vue.use(Router);

// 로그인 안하면 접근 불가
const requireLogin = () => (to, from, next) => {
  if (localStorage.getItem("user_token")) {
    return next();
  }
  next("/");
};

// 로그인하면 접근 불가
const requireNotLogin = () => (to, from, next) => {
  if (!localStorage.getItem("user_token")) {
    return next();
  }
  next("/");
};

export default new Router({
  mode: 'history',
  linkExactActiveClass: 'active',
  routes: [
    // 메인
    {
      path: '/',
      name: 'index',
      components: { default: Index, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      }
    },
    // 로그인
    {
      path: '/login',
      name: 'login',
      components: { default: Login, header: MainNavbar },
      props: {
        header: { colorOnScroll: 400 }
      },
      beforeEnter: requireNotLogin()
    },
    
    // 테스트 페이지
    {
      path: '/testing',
      name: 'testing',
      components: { default: Testing, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      }
    },
    // 포트폴리오 페이지
    {
      path: '/portfolio',
      name: 'portfolio',
      components: { default: Portfolio, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      },
      beforeEnter: requireLogin()
    },
    // 내 정보
    {
      path: '/profile',
      name: 'profile',
      components: { default: Profile, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      },
      beforeEnter: requireLogin()
    },
    // 서비스 이용약관
    {
      path: '/term',
      name: 'term',
      components: { default: Term, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      },
    },
    // 연습용 페이지
    {
      path: '/practice',
      name: 'practice',
      components: { default: practice, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      }
    },
    {
      path: '/chart',
      name: 'chart',
      components: { default: Chart_practice, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      }
    },
    {
      path: '/chart2',
      name: 'chart2',
      components: { default: Chart_practice2, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      }
    },

  ],
  scrollBehavior: to => {
    if (to.hash) {
      return { selector: to.hash };
    } else {
      return { x: 0, y: 0 };
    }
  }
});
