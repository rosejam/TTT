<template>
      <div class="row">
        <card class="card-signup" header-classes="text-center" color="orange">
          <template slot="header">
            <h3 class="card-title title-up">회원 등록</h3>
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
              <fg-input
                v-model="email"
                class="no-border"
                placeholder="이메일"
                addon-left-icon="now-ui-icons ui-1_email-85"
                type="email"
              >
              </fg-input>

              <form>
              <fg-input
                v-model="pw"
                class="no-border input-lg"
                addon-left-icon="now-ui-icons ui-1_lock-circle-open"
                placeholder="비밀번호"
                type="password"
                autocomplete="off"
              >
              </fg-input>

              <fg-input
                v-model="pwCheck"
                class="no-border input-lg"
                addon-left-icon="now-ui-icons ui-1_lock-circle-open"
                placeholder="비밀번호 확인"
                type="password"
                autocomplete="off"
              >
              </fg-input>
              </form>

          </template>
          <div class="card-footer text-center">
            <n-button type="neutral" round size="lg" @click="signUp">시작하기</n-button>
          </div>
        </card>
      </div>
</template>
<script>
import { Card, FormGroupInput, Button } from '@/components';
import firebase from 'firebase';

export default {
  name: 'signupForm',
  components: {
    Card,
    [Button.name]: Button,
    [FormGroupInput.name]: FormGroupInput
  },
  data() {
    return {
      email:'',
      pw:'',
      pwCheck:'',
    }
  },
  methods: {
    signUp() {
      firebase.auth().createUserWithEmailAndPassword(this.email, this.pw)
        .then(
          user => {
            console.log("회원 가입 완료>>", user);
            location.reload();
          },
          function(err) {
            alert("에러: " + err.message);
          }
        )
    }
  },
};
</script>
<style></style>
