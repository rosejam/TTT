<template>
  <div
    class="section section-signup"
    style="background-image: url('img/bg11.jpg'); background-size: cover; background-position: top center; min-height: 700px;"
  >
    <div class="container">
      <div class="row">
        <card class="card-signup" header-classes="text-center" color="orange">
          <template slot="header">
            <h3 class="card-title title-up">회원 가입</h3>
            <div class="social-line">
              <a
                href="#pablo"
                class="btn btn-neutral btn-facebook btn-icon btn-round"
              >
                <i class="fab fa-facebook-square"></i>
              </a>
              <a
                href="#pablo"
                class="btn btn-neutral btn-twitter btn-icon btn-lg btn-round"
              >
                <i class="fab fa-twitter"></i>
              </a>
              <a
                href="#pablo"
                class="btn btn-neutral btn-google btn-icon btn-round"
              >
                <i class="fab fa-google-plus"></i>
              </a>
            </div>
          </template>
          <template>
            <v-form ref="form" v-model="valid" :lazy-validation="lazy">
              <fg-input
                v-model="email"
                :rules="emailRules"
                class="no-border"
                placeholder="이메일"
                addon-left-icon="now-ui-icons ui-1_email-85"
              >
              </fg-input>

              <fg-input
                v-model="password"
                :rules="passwordRules"
                class="no-border input-lg"
                addon-left-icon="now-ui-icons ui-1_lock-circle-open"
                placeholder="비밀번호"
              >
              </fg-input>

              <fg-input
                v-model="passwordCheck"
                :rules="passwordCheckRules"
                class="no-border input-lg"
                addon-left-icon="now-ui-icons ui-1_lock-circle-open"
                placeholder="비밀번호 확인"
              >
              </fg-input>
            </v-form>
          </template>
          <div class="card-footer text-center">
            <n-button
              :disabled="!valid"
              type="neutral"
              round size="lg"
            >
            가입하기
            </n-button>
          </div>
        </card>
      </div>
      <div class="col text-center">
        <router-link
          to="/login"
          class="btn btn-simple btn-round btn-white btn-lg"
        >
          View Login Page
        </router-link>
      </div>
    </div>
  </div>
</template>
<script>
import { Card, FormGroupInput, Button } from '@/components';

export default {
  components: {
    Card,
    [Button.name]: Button,
    [FormGroupInput.name]: FormGroupInput
  },
  data() {
    return {
      valid: true,
      error: "",
      email: "",
      emailRules: [
        v => !!v || "이메일을 입력하세요",
        v => /.+@.+\..+/.test(v) || "이메일 형식이 올바르지 않습니다"
      ],
      password: "",
      passwordRules: [
        v => !!v || "비밀번호를 입력하세요",
        v =>
          /^(?=.*[a-zA-Z])(?=.*\d)(?=.*\W).{8,20}$/.test(v) ||
          "비밀번호는 8~20자 사이의 영문,숫자, 특수문자로 구성해주세요"
      ],
      passwordCheck: "",
      passwordCheckRules: [
        v => !!v || "비밀번호 확인을 입력하세요",
        v => this.password == this.passwordCheck || "비밀번호가 같지 않습니다"
      ],
      lazy: false,
    }
  },
};
</script>
<style></style>
