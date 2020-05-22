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
        <div class="col-lg-3">
          <card>
            <h3>차익거래 알고리즘</h3>
            <h5>운용금액: 9,123,762원</h5>
            <n-switch v-model="switches.defaultOn" on-text="ON" off-text="OFF"></n-switch>
            <!-- <n-switch v-model="switches.defaultOff" on-text="ON" off-text="OFF"></n-switch> -->
            <div class="row">
              <div class="col-lg-6">
              <fg-input  class="col-12"
                        label="파라미터 A"
                        placeholder="Number"
                        value="10.2">
              </fg-input>
              </div>
              <div class="col-lg-6">
              <fg-input  class="col-12"
                        label="파라미터 B"
                        placeholder="Number"
                        value="12.4">
              </fg-input>
              </div>
            </div>
            <div class="row">
              <div class="col-lg-6">
              <fg-input  class="col-12"
                        label="파라미터 C"
                        placeholder="Number"
                        value="2.4">
              </fg-input>
              </div>
              <div class="col-lg-6">
              <fg-input  class="col-12"
                        label="파라미터 D"
                        placeholder="Number"
                        value="0.3">
              </fg-input>
              </div>
            </div>
          <n-button type="primary" outline round @click.native="modals.save = true">
            <i class="fa fa-save"></i> 알고리즘 저장
          </n-button>
          <modal :show.sync="modals.save" headerClasses="justify-content-center" style="color:black" modal-classes="modal-sm">
            <h4 slot="header" class="title title-up">알고리즘 저장</h4>
            <fg-input  class="col-12"
                      placeholder="알고리즘 이름">
            </fg-input>
            <div class="pull-left">
            <n-button type="neutral" round>취소</n-button>
            </div>
            <div class="pull-right">
            <n-button type="primary" round>저장</n-button>
            </div>
          </modal>
          </card>
        </div>
        <div class="col-lg-3">
          <card>
            <h3>페어트레이딩 알고리즘</h3>
            <h5>운용금액: 30,213,432원</h5>
            <n-switch v-model="switches.defaultOn" on-text="ON" off-text="OFF"></n-switch>
            <!-- <n-switch v-model="switches.defaultOff" on-text="ON" off-text="OFF"></n-switch> -->
            <div class="row">
              <div class="col-lg-6">
              <fg-input  class="col-12"
                        label="파라미터 A"
                        placeholder="Number"
                        value="14.2">
              </fg-input>
              </div>
              <div class="col-lg-6">
              <fg-input  class="col-12"
                        label="파라미터 B"
                        placeholder="Number"
                        value="11.0">
              </fg-input>
              </div>
            </div>
            <div class="row">
              <div class="col-lg-6">
              <fg-input  class="col-12"
                        label="파라미터 C"
                        placeholder="Number"
                        value="-2.3">
              </fg-input>
              </div>
              <div class="col-lg-6">
              <fg-input  class="col-12"
                        label="파라미터 D"
                        placeholder="Number"
                        value="6.7">
              </fg-input>
              </div>
            </div>
          <n-button type="primary" outline round @click.native="modals.save = true">
            <i class="fa fa-save"></i> 알고리즘 저장
          </n-button>
          <modal :show.sync="modals.save" headerClasses="justify-content-center" style="color:black" modal-classes="modal-sm">
            <h4 slot="header" class="title title-up">알고리즘 저장</h4>
            <fg-input  class="col-12"
                      placeholder="알고리즘 이름">
            </fg-input>
            <div class="pull-left">
            <n-button type="neutral" round>취소</n-button>
            </div>
            <div class="pull-right">
            <n-button type="primary" round>저장</n-button>
            </div>
          </modal>
          </card>
        </div>
        <div class="col-lg-3">
          <card>
            <h3>인베스팅 알고리즘</h3>
            <h5>운용금액: 17,321,960원</h5>
            <n-switch v-model="switches.defaultOn" on-text="ON" off-text="OFF"></n-switch>
            <!-- <n-switch v-model="switches.defaultOff" on-text="ON" off-text="OFF"></n-switch> -->
            <div class="row">
              <div class="col-lg-6">
              <fg-input  class="col-12"
                        label="파라미터 A"
                        placeholder="Number"
                        value="1.2">
              </fg-input>
              </div>
              <div class="col-lg-6">
              <fg-input  class="col-12"
                        label="파라미터 B"
                        placeholder="Number"
                        value="16.4">
              </fg-input>
              </div>
            </div>
            <div class="row">
              <div class="col-lg-6">
              <fg-input  class="col-12"
                        label="파라미터 C"
                        placeholder="Number"
                        value="22.5">
              </fg-input>
              </div>
              <div class="col-lg-6">
              <fg-input  class="col-12"
                        label="파라미터 D"
                        placeholder="Number"
                        value="4.3">
              </fg-input>
              </div>
            </div>
          <n-button type="primary" outline round @click.native="modals.save = true">
            <i class="fa fa-save"></i> 알고리즘 저장
          </n-button>
          <modal :show.sync="modals.save" headerClasses="justify-content-center" style="color:black" modal-classes="modal-sm">
            <h4 slot="header" class="title title-up">알고리즘 저장</h4>
            <fg-input  class="col-12"
                      placeholder="알고리즘 이름">
            </fg-input>
            <div class="pull-left">
            <n-button type="neutral" round>취소</n-button>
            </div>
            <div class="pull-right">
            <n-button type="primary" round>저장</n-button>
            </div>
          </modal>
          </card>
        </div>
        <div class="col-lg-3">
          <card>
            <h3>보유 알고리즘 목록</h3>
            <div class="table-responsive text-left">
              <base-table :data="table.data"
                          :columns="table.columns"
                          thead-classes="text-primary">
              </base-table>
            </div>
          </card>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { Button, DropDown, Tabs, TabPane, FormGroupInput, Switch, Modal } from '@/components';
import { Popover } from 'element-ui';
import { Card } from "@/components/index";
import BaseTable from "@/components/BaseTable";

const tableColumns = ["알고리즘이름"];
const tableData = [
  {
    id: 1,
    알고리즘이름: "A 알고리즘",
  },
  {
    id: 2,
    알고리즘이름: "B 알고리즘",
  },
  {
    id: 3,
    알고리즘이름: "C 알고리즘",
  },
  {
    id: 4,
    알고리즘이름: "D 알고리즘",
  }
];

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
    Card,
    BaseTable,
  },
  data() {
    return {
      modals: {
        save: false
      },
      switches: {
        defaultOn: true,
        defaultOff: false
      },
      table: {
        title: "Simple Table",
        columns: [...tableColumns],
        data: [...tableData]
      },
    }
  },
};
</script>
<style></style>
