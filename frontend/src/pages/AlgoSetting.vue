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
          <h1 class="title">알고리즘 설정</h1>
        </div>
      </div>
    </div>
    <div class="section">
      <div class="container text-center">
        <h3>
          알고리즘 수치를 조정해<br/>
          <b>나만의 알고리즘</b>을 만들어보세요!
        </h3>
      </div>
      <div class="row">
          <fg-input  class="col-sm-6 col-12"
                     label="원하는 수익률(%)"
                     placeholder="Number"
                     type="search">
          </fg-input>
          원금 보장(안전우선)
          <n-switch v-model="switches.defaultOn" on-text="ON" off-text="OFF"></n-switch>
          <!-- <n-switch v-model="switches.defaultOff" on-text="ON" off-text="OFF"></n-switch> -->

          <div class="col-5">
          <drop-down class="btn-group">
            <template slot="title">
            <button type="button" class="btn btn-primary">TTT's 알고리즘</button>
              <button type="button" class="btn btn-primary dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <span class="sr-only">Toggle Dropdown</span>
              </button>
            </template>
            <div v-popover:warning>
            <h6 class="dropdown-header">TTT가 미리 만들어둔 알고리즘이에요!</h6>
            <a class="dropdown-item" href="#">골든크로스-데드크로스 알고리즘</a>
            <a class="dropdown-item" href="#">수익 우선 알고리즘</a>
            <a class="dropdown-item" href="#">원금 보장 우선 알고리즘</a>
            </div>
            <el-popover
              ref="warning"
              popper-class="popover"
              placement="bottom"
              width="200"
              trigger="hover"
            >
              <div class="popover-body">
                ※주의:
                클릭 시 기존 설정이 초기화됩니다.
              </div>
            </el-popover>
          </drop-down>
        </div>
        <n-button type="primary" outline round @click.native="modals.save = true">
          <i class="fa fa-save"></i> 알고리즘 저장
        </n-button>
        <modal :show.sync="modals.save" headerClasses="justify-content-center" style="color:black" modal-classes="modal-sm">
          <h4 slot="header" class="title title-up">알고리즘 저장</h4>
          <p>현재 알고리즘 설정을 저장하시겠습니까?</p>
          <div class="pull-left">
          <n-button type="neutral" round>취소</n-button>
          </div>
          <div class="pull-right">
          <n-button type="primary" round>저장</n-button>
          </div>
        </modal>
      </div>
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
