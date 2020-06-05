<!-- 회원가입 양식 -->
<template>
      <div class="row">
        <card class="card-signup" header-classes="text-center" color="orange">
          <template slot="header">
            <h3 class="card-title title-up">회원 등록</h3>
          </template>
          <template>

              <!-- 이메일 입력 -->
              <fg-input
                v-model="email"
                class="no-border"
                placeholder="이메일"
                addon-left-icon="now-ui-icons ui-1_email-85"
                type="email"
              >
              </fg-input>

              <form>
                <!-- 비밀번호 입력 -->
                <fg-input
                  v-model="pw"
                  class="no-border input-lg"
                  addon-left-icon="now-ui-icons ui-1_lock-circle-open"
                  placeholder="비밀번호"
                  type="password"
                  autocomplete="off"
                >
                </fg-input>

                <!-- 비밀번호 확인 입력 -->
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

          <!-- 회원가입 버튼 -->
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

      // 비밀번호 확인
      if(this.pw != this.pwCheck) {
        alert("비밀번호가 다릅니다");
        return;
      }

      // firebase 회원가입
      firebase.auth().createUserWithEmailAndPassword(this.email, this.pw)
        .then(
          user => {
            location.reload();
          },
          function(err) {
            alert(err.message);
          }
        )
    }
  },
};
</script>
<style></style>
