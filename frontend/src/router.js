import Vue from 'vue';
import Router from 'vue-router';
// 메인
import Index from './pages/Index.vue';
// 로그인
import Login from './pages/Login.vue';
import Signup from './pages/Signup.vue';
// 증권 정보
import StockInfo from './pages/StockInfo.vue';
import StockDetail from './pages/StockDetail.vue';
// 자산 관리
import Asset from './pages/Asset.vue';
import TradingHistory from './pages/TradingHistory.vue';
import AlgoSetting from './pages/AlgoSetting.vue';
// 알고리즘마켓
import AlgoMarket from './pages/AlgoMarket.vue';
// 내 정보
import Profile from './pages/Profile.vue';
// 네비게이션 바
import MainNavbar from './layout/MainNavbar.vue';
// 푸터
import MainFooter from './layout/MainFooter.vue';
// 기타 페이지
import Dashboard from './pages/Dashboard.vue';
import Landing from './pages/Landing.vue';
// import Chart_practice from './pages/Chart_practice.vue';

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
    {
      path: '/signup',
      name: 'signup',
      components: { default: Signup, header: MainNavbar },
      props: {
        header: { colorOnScroll: 400 }
      }
    },
    // 증권 정보
    {
      path: '/stockinfo',
      name: 'stockinfo',
      components: { default: StockInfo, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      }
    },
    // 상세 증권 정보
    {
      path: '/stockdetail',
      name: 'stockdetail',
      components: { default: StockDetail, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      }
    },
    // 자산 관리
    {
      path: '/asset',
      name: 'asset',
      components: { default: Asset, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      }
    },
    {
      path: '/tr_history',
      name: 'tr_history',
      components: { default: TradingHistory, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      }
    },
    {
      path: '/algosetting',
      name: 'algosetting',
      components: { default: AlgoSetting, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      }
    },
    // 알고리즘 마켓
    {
      path: '/algomarket',
      name: 'algomarket',
      components: { default: AlgoMarket, header: MainNavbar, footer: MainFooter },
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
    // 기타 페이지
    {
      path: '/dash',
      name: 'dash',
      components: { default: Dashboard, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      }
    },
    {
      path: '/landing',
      name: 'landing',
      components: { default: Landing, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      }
    },
    // {
    //   path: '/practice',
    //   name: 'practice',
    //   components: { default: Chart_practice, header: MainNavbar, footer: MainFooter },
    //   props: {
    //     header: { colorOnScroll: 400 },
    //     footer: { backgroundColor: 'black' }
    //   }
    // },

  ],
  scrollBehavior: to => {
    if (to.hash) {
      return { selector: to.hash };
    } else {
      return { x: 0, y: 0 };
    }
  }
});
