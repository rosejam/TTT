<!-- /login -->
<template>
  <div class="page-header clear-filter" filter-color="orange">
    <div
      class="page-header-image"
      style="background-image: url('img/login.jpg')"
    ></div>
    <div class="content">
      <div class="container">
        <div class="col-md-5 ml-auto mr-auto">
          <card type="login" plain>
            <div slot="header" class="logo-container">
              <img v-lazy="'img/TTT-logo.png'" alt="" />
            </div>

            <!-- 이메일 입력 -->
            <fg-input
              v-model="email"
              class="no-border input-lg"
              addon-left-icon="now-ui-icons ui-1_email-85"
              placeholder="이메일"
              type="email"
            >
            </fg-input>

            <!-- 비밀번호 입력 -->
            <fg-input
              v-model="pw"
              @keypress.enter="login"
              class="no-border input-lg"
              addon-left-icon="now-ui-icons ui-1_lock-circle-open"
              placeholder="비밀번호"
              type="password"
              autocomplete="off"
            >
            </fg-input>

            <!-- 로그인 창 하단 -->
            <template slot="raw-content">

              <!-- 로그인 버튼 -->
              <div class="card-footer text-center">
                <n-button
                  @click="login"
                  type="primary"
                  block
                  round
                >
                  로그인
                </n-button>
              </div>

              <!-- 회원가입 버튼 -->
              <div class="pull-left">
                <h6>
                  <n-button type="neutral" @click.native="modals.signup = true" link>
                    TTT's 회원 되기 <i class="now-ui-icons sport_user-run"></i>
                  </n-button>
                  <modal :show.sync="modals.signup" headerClasses="justify-content-center">
                    <signup-form/>
                  </modal>
                </h6>
              </div>

            </template>
          </card>
        </div>
      </div>
    </div>
    <main-footer></main-footer>
  </div>
</template>
<script>
import { mapActions } from "vuex";
import { Card, Button, FormGroupInput, Modal } from '@/components';
import MainFooter from '@/layout/MainFooter';
import SignupForm from '@/pages/components/SignupForm';
import firebase from 'firebase';

export default {
  name: 'login',
  bodyClass: 'login-page',
  components: {
    Card,
    MainFooter,
    [Button.name]: Button,
    [FormGroupInput.name]: FormGroupInput,
    Modal,
    SignupForm
  },
  data(){
    return {
      email:'',
      pw:'',
      modals: {
        signup: false,
        help: false
      }
    }
  },
  methods: {
    ...mapActions("user", ["getUserInfo"]),

    // 로그인
    async login() {

      // firebase 로그인
      await firebase.auth()
                    .signInWithEmailAndPassword(this.email, this.pw)
                    .then(
                      user => {
                        // 로그인 시 uid 저장
                        localStorage.setItem("user", user.user.uid);
                        // 로그인 시 토큰 저장
                        firebase.auth().currentUser.getIdToken().then(idToken => {
                          localStorage.setItem("user_token", idToken);
                        });
                      },
                      function(err) {
                        alert("에러: " + err.message);
                      }
                    );

      // 로그인 완료 후 동작
      if(localStorage.getItem("user_token")) {
        await this.getUserInfo();     // user state에 userInfo 세팅
        this.$router.push("/");   // 메인페이지로 이동
      }

    },
  },
};
</script>
<style></style>
