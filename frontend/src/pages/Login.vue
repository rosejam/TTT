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

            <fg-input
              v-model="email"
              class="no-border input-lg"
              addon-left-icon="now-ui-icons ui-1_email-85"
              placeholder="이메일"
              type="email"
            >
            </fg-input>

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

            <template slot="raw-content">
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
              <div class="pull-right">
                <h6>
                  <n-button type="neutral" @click.native="modals.help = true" link>
                    TTT가 뭐야?
                  </n-button>
                  <modal :show.sync="modals.help" headerClasses="justify-content-center" style="color:black">
                    <h4 slot="header" class="title title-up">TTT?</h4>
                    <p>
                      1. Tiny Testing Tool의 줄임말입니다. <br/>
                      2. 또한 Trust, Trend, Tactic 의 3T를 가치로 삼고 있습니다. <br/>
                    </p>
                    <!-- <template slot="footer">
                      <n-button>Nice Button</n-button>
                      <n-button type="danger" @click.native="modals.classic = false">Close</n-button>
                    </template> -->
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
import { mapState, mapActions, mapMutations } from "vuex";
import { Card, Button, FormGroupInput, Modal } from '@/components';
import MainFooter from '@/layout/MainFooter';
import SignupForm from '@/pages/components/SignupForm';
import firebase from 'firebase';

export default {
  name: 'login-page',
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
    ...mapActions("user", ["setUser"]),
    async login() {
      await firebase.auth()
                    .signInWithEmailAndPassword(this.email, this.pw)
                    .then(
                      user => {
                        localStorage.setItem("email", this.email);
                        // this.$session.set('user', user);
                        // firebase.auth().currentUser.getIdToken().then(idToken => {
                        //   console.log(idToken);
                        // });
                      },
                      function(err) {
                        alert("에러: " + err.message);
                      }
                    );
      
      const email = this.email;
      await this.setUser();
      this.$router.push("/");
    },
  },
};
</script>
<style></style>
