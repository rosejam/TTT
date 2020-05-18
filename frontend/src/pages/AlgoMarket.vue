<template>
  <div>
    <div class="page-header page-header-small">
      <parallax
        class="page-header-image"
        style="background-image: url('img/bg6.jpg')"
      >
      </parallax>
      <div class="content-center">
        <div class="container">
          <h1 class="title">알고리즘 마켓</h1>
        </div>
      </div>
    </div>
    <div class="section text-center">
      <div class="container">
        <h3>
          여러분들이 만든 알고리즘을 사고팔 수 있는<br/>
          <b>알고리즘 마켓</b>입니다
        </h3>
      </div>
      <div>
          <fg-input  class="col-sm-6 col-12"
                     placeholder="알고리즘 검색"
                     type="search"
                     id="search">
          </fg-input>
      </div>
          <n-button round>검색</n-button>
    </div>
  </div>
</template>
<script>
import { Button, DropDown, Tabs, TabPane, FormGroupInput, Switch, Modal } from '@/components';
import { Popover } from 'element-ui';

export default {
  name: 'profile',
  bodyClass: 'profile-page',
  components: {
    [Button.name]:Button,
    DropDown,
    Tabs,
    TabPane,
    [FormGroupInput.name]: FormGroupInput,
    [Switch.name]: Switch,
    [Popover.name]: Popover,
    Modal,
  },
  data() {
    return {
      modals: {
        save: false
      },
      switches: {
        defaultOn: true,
        defaultOff: false
      }
    }
  },
};
</script>
<style></style>
