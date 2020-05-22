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
          <h1 class="title">삼성전자 증권 정보</h1>
        </div>
      </div>
    </div>
    <img src="img/삼성전자주식.PNG"/>

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
