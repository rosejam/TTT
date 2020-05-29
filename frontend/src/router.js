import Vue from 'vue';
import Router from 'vue-router';
// 메인
import Index from './pages/Index.vue';
// 로그인
import Login from './pages/Login.vue';
// 포트폴리오
import Testing from './pages/Testing.vue';
// 내 정보
import Profile from './pages/Profile.vue';
// 네비게이션 바
import MainNavbar from './layout/MainNavbar.vue';
// 푸터
import MainFooter from './layout/MainFooter.vue';

import Chart_practice from './pages/Chart_practice.vue'
import Chart_practice2 from './pages/Chart_practice2.vue'

Vue.use(Router);

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
      }
    },
    
    // 내 정보
    {
      path: '/testing',
      name: 'testing',
      components: { default: Testing, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      }
    },
    // 내 정보
    {
      path: '/profile',
      name: 'profile',
      components: { default: Profile, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      }
    },
    {
      path: '/practice',
      name: 'practice',
      components: { default: Chart_practice, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      }
    },
    {
      path: '/practice2',
      name: 'practice2',
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
