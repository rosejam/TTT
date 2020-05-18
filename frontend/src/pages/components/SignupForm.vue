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
                class="no-border"
                placeholder="이메일"
                addon-left-icon="now-ui-icons ui-1_email-85"
                type="email"
              >
              </fg-input>

              <fg-input
                class="no-border input-lg"
                addon-left-icon="now-ui-icons ui-1_lock-circle-open"
                placeholder="비밀번호"
                type="password"
              >
              </fg-input>

              <fg-input
                class="no-border input-lg"
                addon-left-icon="now-ui-icons ui-1_lock-circle-open"
                placeholder="비밀번호 확인"
                type="password"
              >
              </fg-input>
          </template>
          <div class="card-footer text-center">
            <n-button type="neutral" round size="lg">시작하기</n-button>
          </div>
        </card>
      </div>
</template>
<script>
import { Card, FormGroupInput, Button } from '@/components';

export default {
  components: {
    Card,
    [Button.name]: Button,
    [FormGroupInput.name]: FormGroupInput
  }
};
</script>
<style></style>
