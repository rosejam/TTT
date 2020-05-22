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
    <div class="row">
      <div class="col-12">
        <card>
          <template slot="header">
            <h4 class="card-title">알고리즘 목록</h4>
          </template>
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
</template>
<script>
import { Button, DropDown, Tabs, TabPane, FormGroupInput, Switch, Modal } from '@/components';
import { Popover } from 'element-ui';
import { Card } from "@/components/index";
import BaseTable from "@/components/BaseTable";

const tableColumns = ["알고리즘이름", "판매자"];
const tableData = [
  {
    id: 1,
    알고리즘이름: "A 알고리즘",
    판매자: "ssafy1234"
  },
  {
    id: 2,
    알고리즘이름: "B 알고리즘",
    판매자: "ssafy1234"
  },
  {
    id: 3,
    알고리즘이름: "C 알고리즘",
    판매자: "ssafy1234"
  },
  {
    id: 4,
    알고리즘이름: "D 알고리즘",
    판매자:"hellossafy"
  },
  {
    id: 5,
    알고리즘이름: "E 알고리즘",
    판매자:"hellossafy"
  },
  {
    id: 6,
    알고리즘이름: "F 알고리즘",
    판매자:"트레이딩전문"
  },
  {
    id: 7,
    알고리즘이름: "G 알고리즘",
    판매자:"트레이딩전문"
  },
  {
    id: 8,
    알고리즘이름: "H 알고리즘",
    판매자:"주식에미치다"
  },
  {
    id: 9,
    알고리즘이름: "I 알고리즘",
    판매자:"주식에미치다"
  },
  {
    id: 10,
    알고리즘이름: "J 알고리즘",
    판매자:"주식에미치다"
  },
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
