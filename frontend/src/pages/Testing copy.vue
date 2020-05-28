<template>
  <div class="content">

    <!-- 페이지 헤더 -->
    <div class="page-header page-header-small">

      <!-- 배경사진 -->
      <parallax
        class="page-header-image"
        style="background-image: url('img/bg6.jpg')"
      >
      </parallax>

      <!-- 페이지 타이틀 -->
      <div class="content-center">
        <div class="container">
          <h1 class="title">포트폴리오 테스트</h1>
        </div>
      </div>
    </div>

    <!-- 컨텐츠 -->
    <div class="section text-center">
      <div class="container">
        <h3>
          과거 데이터를 기반으로<br/>
          <b>테스트</b>를 진행해보세요!
        </h3>
      </div>

        <!-- 기간 select -->
        <div class="row">
          <div class="col-md-1">
            기간 설정
          </div>
          <div class="col-md-2">
            <v-select v-model="period" :options="periodOptions" :reduce="content => content.code" label="content" />
          </div>
        </div>
        <br/>
        <div class="row">

          <!-- 시작일 select -->
          <div class="col-md-1">
            시작 연도
          </div>
          <div class="col-md-1">
            <v-select v-model="startYear" :options=yearOptions></v-select>
          </div>
          <div class="col-md-1" v-if="isMonth">
            시작 월
          </div>
          <div class="col-md-1" v-if="isMonth">
            <v-select v-model="startMonth" :options=monthOptions></v-select>
          </div>

          <!-- 종료일 -->
          <div class="col-md-1">
            종료 연도
          </div>
          <div class="col-md-1">
            <v-select v-model="endYear" :options=yearOptions></v-select>
          </div>
          <div class="col-md-1" v-if="isMonth">
            종료 월
          </div>
          <div class="col-md-1" v-if="isMonth">
            <v-select v-model="endMonth" :options=monthOptions></v-select>
          </div>
        </div>
        <br/>

        <!-- Include YTD -->
        <!-- <div class="row">
          <div class="col-md-1">
            Include YTD
          </div>
        </div>
        <br/> -->

        <!-- 초기금액 -->
        <div class="row">
          <div class="col-md-1">
            초기금액
          </div>
          <div class="col-md-2">
            <fg-input v-model="initAmount"></fg-input>
          </div>
          <div>
            원
          </div>
        </div>

        <!-- Cashflows -->
        <!-- <div class="row">
          <div class="col-md-1">
            Cashflows
          </div>
        </div> -->

        <!-- 자산 재분배 -->
        <br/>
        <div class="row">
          <div class="col-md-1">
            자산 재분배
          </div>
          <div class="col-md-2">
            <v-select v-model="rebalancing" :options="rebalancingOptions" :reduce="content => content.code" label="content" />
          </div>
        </div>
        <br/>

        <!-- 포트폴리오 테이블 -->
        <div class="table" style="width:95%; margin:auto">
          <table class="table" style="width:95%">
            <thead>
              <tr>
                <td></td>
                <td><strong>종목</strong></td>
                <td><strong>포트폴리오 1</strong></td>
                <td><strong>포트폴리오 2</strong></td>
                <td><strong>포트폴리오 3</strong></td>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(row, index) in rows" :key="index" :row="row">
                <td>
                  종목{{index+1}}
                  <n-button @click="removeRow(index)" type="neutral">
                    <i class="fa fa-trash-alt"></i>
                  </n-button>
                </td>
                <td>
                  <autocomplete-vue
                    classPrefix="my-custom-class"
                      v-model="row.stock"
                      :list="[{name: 'LG전자(123)'}, {name: '삼성전자(142)'}, {name: '현대자동차(241)'}]"
                      placeholder="종목 검색"
                      :threshold="0"
                  ></autocomplete-vue>
                  <!-- threshold: 필요 글자수 -->
                </td>
                <td><input type="number" v-model="row.portfolio1" :disabled="row.stock==''" style="width:100%">%</td>
                <td><input type="number" v-model="row.portfolio2" :disabled="row.stock==''" style="width:100%">%</td>
                <td><input type="number" v-model="row.portfolio3" :disabled="row.stock==''" style="width:100%">%</td>
              </tr>
              <tr>
                <td>합계</td>
                <td></td>
                <td>{{sum1}}%</td>
                <td>{{sum2}}%</td>
                <td>{{sum3}}%</td>
              </tr>
              <tr>
                <n-button type="primary" icon round @click="addRow()">
                  <i class="fa fa-plus"></i>
                </n-button>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- 포트폴리오 테이블 끝 -->

        <n-button @click="test(rows)">시뮬레이션</n-button>
    </div>
  </div>
</template>
<script>
import { Button, DropDown, Tabs, TabPane, FormGroupInput, Switch, Modal } from '@/components';
import { Popover } from 'element-ui';
import { Card } from "@/components/index";
import BaseTable from "@/components/BaseTable";

export default {
  name: 'testing',
  bodyClass: 'testing-page',
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
      period: 'Year to Year',
      periodOptions: [{code: 'Y', content: 'Year to Year'}, {code: 'M', content: 'Month to Month'}],
      startYear: 0,
      startMonth: 1,
      endYear: 2020,
      endMonth: 1,
      yearOptions: [2020],
      monthOptions: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
      initAmount: 1000000,
      rebalancing: 0,
      rebalancingOptions: [{code: 1, content: '재분배하지 않음'}, {code: 2, content: '1년마다'}, {code: 3, content: '6개월마다'}],
      columns: ["stock", "portfolio1", "portfolio2", "portfolio3"],
      rows: [
        { stock: "", portfolio1: 0, portfolio2: 0, portfolio3: 0, },
        { stock: "", portfolio1: 0, portfolio2: 0, portfolio3: 0, },
        { stock: "", portfolio1: 0, portfolio2: 0, portfolio3: 0, },
      ],
    }
  },
  methods:{
    addRow() {
      console.log(this.rows);
      this.rows.push({ stock: "", portfolio1: 0, portfolio2: 0, portfolio3: 0, });
    },
    removeRow(index) {
      console.log('remove...', index)
      this.rows.splice(index, 1);
    },
    test(rows) {
      console.log(rows);
    },
    calc(p) {

      var sum = 0;

      if(p==1) {
        for (let i = 0; i < this.rows.length; i++) {
          const row = this.rows[i];
          sum += Number(row.portfolio1);
        }
      }
      else if(p==2) {
        for (let i = 0; i < this.rows.length; i++) {
          const row = this.rows[i];
          sum += Number(row.portfolio2);
        }
      }
      else {
        for (let i = 0; i < this.rows.length; i++) {
          const row = this.rows[i];
          sum += Number(row.portfolio3);
        }
      }

      return sum;
    }
  },
  computed: {
    isMonth() {
      if(this.period == 'M') return true;
      else return false;
    },
    sum1() {
      return this.calc(1);
    },
    sum2() {
      return this.calc(2);
    },
    sum3() {
      return this.calc(3);
    },
  },
};
</script>
<style></style>
