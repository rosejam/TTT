<template>
  <div class="content">
    <div class="page-header page-header-small">
      <parallax
        class="page-header-image"
        style="background-image: url('img/bg6.jpg')"
      >
      </parallax>
      <div class="content-center">
        <div class="container">
          <h1 class="title">거래 내역</h1>
        </div>
      </div>
    </div>
    <div class="section text-center">
      <div class="container">
        <h3>
          어떤 주식을 사고 팔았는지<br/>
          <b>한눈에 확인</b>해보세요!
        </h3>
      </div>
      <div>
          <fg-input  class="col-sm-6 col-12"
                     placeholder="종목 검색"
                     type="search"
                     id="search">
          </fg-input>
      </div>
          <n-button round>검색</n-button>
    </div>
    <div class="row">
      <div class="col-12">
        <card>
          <template slot="header">
            <h4 class="card-title">거래 내역</h4>
          </template>
          <div class="table-responsive text-left">
            <base-table :data="table1.data"
                        :columns="table1.columns"
                        thead-classes="text-primary">
            </base-table>
          </div>
        </card>
      </div>

      <div class="col-12">
        <card class="card-plain">
          <template slot="header">
                <h4 class="card-title"> Table on Plain Background</h4>
                <p class="category"> Here is a subtitle for this table</p>
              </template>
          <div class="table-full-width table-responsive text-left">
            <base-table :title="table2.title" :sub-title="table2.subTitle" :data="table2.data"
                        :columns="table2.columns">
            </base-table>
          </div>
        </card>
      </div>

    </div>
  </div>
</template>
<script>
import { Button, DropDown, Tabs, TabPane, FormGroupInput, Switch, Modal } from '@/components';
import { Popover } from 'element-ui';
import { Card } from "@/components/index";
import BaseTable from "@/components/BaseTable";

const tableColumns = ["일시", "종목", "거래종류", "거래수량", "거래금액"];
const tableData = [
  {
    id: 1,
    일시: "2020-05-20 10:13:23",
    종목: "SK하이닉스",
    거래종류: "매수",
    거래수량: "46",
    거래금액: "10000000"
  },
  {
    id: 2,
    일시: "2020-05-19 14:12:43",
    종목: "삼성전자",
    거래종류: "매도",
    거래수량: "36",
    거래금액: "34000000"
  },
  {
    id: 3,
    일시: "2020-05-19 14:10:32",
    종목: "현대자동차",
    거래종류: "매도",
    거래수량: "33",
    거래금액: "26000000"
  },
  {
    id: 4,
    일시: "2020-05-19 13:21:43",
    종목: "멀티캠퍼스",
    거래종류: "매수",
    거래수량: "68",
    거래금액: "30000000"
  },
  {
    id: 5,
    일시: "2020-05-19 13:01:04",
    종목: "삼성전자",
    거래종류: "매수",
    거래수량: "32",
    거래금액: "33000000"
  },
  {
    id: 6,
    일시: '2020-05-18 15:13:11',
    종목: 'SK텔레콤',
    거래종류: '매도',
    거래수량: '11',
    거래금액: "4000000"
  },
  {
    id: 7,
    일시: '2020-05-20 14:42:32',
    종목: '삼성SDS',
    거래종류: '매수',
    거래수량: '23',
    거래금액: "12000000"
  }
];

export default {
  name: 'tr_history',
  bodyClass: 'tr_history-page',
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
      table1: {
        title: "Simple Table",
        columns: [...tableColumns],
        data: [...tableData]
      },
      table2: {
        title: "Table on Plain Background",
        columns: [...tableColumns],
        data: [...tableData]
      },
    }
  },
};
</script>
<style></style>
