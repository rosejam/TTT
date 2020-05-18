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
              로그인
            </div>

            <fg-input
              class="no-border input-lg"
              addon-left-icon="now-ui-icons users_circle-08"
              placeholder="이메일"
            >
            </fg-input>

            <fg-input
              class="no-border input-lg"
              addon-left-icon="now-ui-icons ui-1_lock-circle-open"
              placeholder="비밀번호"
            >
            </fg-input>

            <template slot="raw-content">
              <div class="card-footer text-center">
                <a
                  href="#pablo"
                  class="btn btn-primary btn-round btn-lg btn-block"
                  >로그인</a
                >
              </div>
              <div class="pull-left">
                <h6>
                  <!-- <router-link to="/signup" class="link footer-link">
                    TTT's 회원 되기 <i class="now-ui-icons sport_user-run"></i>
                  </router-link> -->
                  <n-button type="neutral" @click.native="modals.classic = true" link>
                    TTT's 회원 되기 <i class="now-ui-icons sport_user-run"></i>
                  </n-button>
                  <modal :show.sync="modals.classic" headerClasses="justify-content-center">
                    <signup-form/>
                    <!-- <h4 slot="header" class="title title-up">Modal title</h4>
                    <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live
                      the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large
                      language ocean. A small river named Duden flows by their place and supplies it with the necessary
                      regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your
                      mouth.</p>
                    <template slot="footer">
                      <n-button>Nice Button</n-button>
                      <n-button type="danger" @click.native="modals.classic = false">Close</n-button>
                    </template> -->
                  </modal>
                </h6>
              </div>
              <div class="pull-right">
                <h6>
                  <a href="#pablo" class="link footer-link">도와줘요 TTT!</a>
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
import { Card, Button, FormGroupInput, Modal } from '@/components';
import MainFooter from '@/layout/MainFooter';
import SignupForm from '@/pages/components/SignupForm';
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
      modals: {
        classic: false
      }
    }
  },
};
</script>
<style></style>
