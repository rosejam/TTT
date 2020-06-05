<template>
  <router-link to="/testing">
    <div class="page-header clear-filter" filter-color="orange" >
      <div
        class="page-header-image"
        style="background-image: url('img/header.jpg')"
      ></div>
      <div class="content">
        <div class="container">
          <div class="col-md-5 ml-auto mr-auto">
            <card type="login" plain>
              <div slot="header" class="logo-container">
                <img v-lazy="'img/TTT-logo.png'" alt="" />
              </div>
            </card>
            <!-- <img v-lazy="'img/TTT-logo.png'" alt="" /> -->
          </div>
        </div>
      </div>
    </div>
  </router-link>
</template>
<script>
import { Card } from '@/components';

export default {
  name: 'login',
  bodyClass: 'login-page',
  components: {
    Card,
  },
};
</script>
<style></style>
