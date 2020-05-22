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
          <h1 class="title">증권 정보</h1>
        </div>
      </div>
    </div>
    <div class="section text-center">
      <div class="container">
        <h3>
          다양한 <b>증권 정보</b>를 검색해보세요!
        </h3>
      </div>
      <div style="text-center">
          <fg-input  class="col-sm-6 col-12"
                     placeholder="종목명·지수명·펀드명·환율명·원자재명 입력"
                     type="search"
                     id="search">
          </fg-input>
      </div>
          <n-button @click="showSamsung" round>검색</n-button>
    </div>

    <!-- 더미 테이블 -->
    <div v-if="ss" style="margin:auto; width: 80%">
      <b-table :fields="table.fields" :items="table.items">
        <template v-slot:cell(종목명)="data">
          <!-- `data.value` is the value after formatted by the Formatter -->
          <a :href="`/stockdetail`">{{ data.value }}</a>
          <!-- <a :href="`/${data.value.replace(/[^a-z]+/i,'-').toLowerCase()}`">{{ data.value }}</a> -->
        </template>
      </b-table>
    </div>
  </div>
</template>
<script>
import { Card } from "@/components/index";
import { Button, DropDown, Tabs, TabPane, FormGroupInput, Switch, Modal } from '@/components';
import { Popover } from 'element-ui';
import BaseTable from "@/components/BaseTable";

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
    BaseTable
  },
  data() {
    return {
      ss: false,
      modals: {
        save: false
      },
      switches: {
        defaultOn: true,
        defaultOff: false
      },
      table: {
        fields: [
          '종목명',
          '현재가',
          '매도호가',
          '매수호가',
          '거래량',
          '거래대금'
        ],
        items: [
          { 종목명: '삼성전자', 현재가: '48,800', 매도호가: '48,900', 매수호가: '48,850', 거래량: '11,227,615', 거래대금: '552,427,000,000' },
          { 종목명: '삼성전자우', 현재가: '42,400', 매도호가: '42,500', 매수호가: '42,450', 거래량: '984,540', 거래대금: '42,048,000,000' },
        ]
      },
    }
  },
  methods: {
    showSamsung() {
      this.ss = true;
    },
    goDetail() {
      this.$router.replace("/stockdetail");
    }
  },
};
</script>
<style></style>
