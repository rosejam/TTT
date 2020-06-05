<!-- / -->
<template>
  <div>
    <div class="page-header clear-filter" filter-color="orange">
      <parallax
        class="page-header-image"
        style="background-image:url('img/header.jpg')"
      >
      </parallax>
      <div class="container">
        <div class="content-center brand">
          <img class="n-logo" src="img/TTT-logo.png" alt="" />
          <h1 class="h1-seo">Tiny Testing Tool</h1>
          <h3>주식투자를 위한<br/>가장 완벽한 테스트 도구</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Parallax } from '@/components';

export default {
  name: 'index',
  bodyClass: 'index-page',
  components: {
    Parallax,
  }
};
</script>
<style></style>
