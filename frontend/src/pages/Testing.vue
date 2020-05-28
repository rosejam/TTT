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

        <div class="row">

          <!-- 기간 select -->
          <div class="col-md-1">
            <p>기간 설정</p>
          </div>
          <div class="col-md-2">
            <v-select v-model="period" :options="periodOptions" :reduce="content => content.code" label="content" />
          </div>

          <!-- 초기금액 설정 -->
          <div class="col-md-1">
            <p>초기금액(원)</p>
          </div>
          <div class="col-md-2">
            <fg-input type="number" v-model="initAmount"></fg-input>
          </div>

          <!-- 자산 재분배 -->
          <div class="col-md-1">
            <p>재분배 주기</p>
          </div>
          <div class="col-md-2">
            <v-select v-model="rebalancing" :options="rebalancingOptions" :reduce="content => content.code" label="content" />
          </div>
        </div>
        <br/>

        <div class="row">

          <!-- 시작일 select -->
          <div class="col-md-1">
            <p>시작 연도</p>
          </div>
          <div class="col-md-2">
            <v-select v-model="startYear" :options=yearOptions></v-select>
          </div>
          <div class="col-md-1" v-if="isMonth">
            <p>시작 월</p>
          </div>
          <div class="col-md-1" v-if="isMonth">
            <v-select v-model="startMonth" :options=monthOptions></v-select>
          </div>

          <!-- 종료일 -->
          <div class="col-md-1">
            <p>종료 연도</p>
          </div>
          <div class="col-md-2">
            <v-select v-model="endYear" :options=yearOptions></v-select>
          </div>
          <div class="col-md-1" v-if="isMonth">
            <p>종료 월</p>
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

        <!-- Cashflows -->
        <!-- <div class="row">
          <div class="col-md-1">
            Cashflows
          </div>
        </div> -->


        <!-- 설정한 기간 -->
        <div class="period">
          <span>설정 기간: {{startYear}} 년</span> <span v-if="isMonth"> {{startMonth}} 월</span> <span>~ {{endYear}} 년</span> <span v-if="isMonth"> {{endMonth}} 월 </span>
        </div>
        <br/>

        <!-- 포트폴리오 저장 버튼 -->
        <n-button type="primary" outline round @click.native="modals.save = true"
        v-if="userLogined">
          <i class="fa fa-save"></i> &nbsp; 포트폴리오 저장
        </n-button>
        <modal :show.sync="modals.save" headerClasses="justify-content-center" style="color:black" modal-classes="modal-sm">
          <h4 slot="header" class="title title-up">포트폴리오 저장</h4>
          <fg-input  class="col-12"
                    placeholder="포트폴리오 이름">
          </fg-input>
          <div class="pull-left">
          <n-button type="neutral" round @click="modals.save = false">취소</n-button>
          </div>
          <div class="pull-right">
          <n-button type="primary" round>저장</n-button>
          </div>
        </modal>

        <!-- 포트폴리오 테이블 -->
        <div style="width:95%; margin:auto">
          <table class="table" style="width:95%">
            <thead>
              <tr>
                <td>종목</td>
                <td><strong>포트폴리오 1</strong></td>
                <td><strong>포트폴리오 2</strong></td>
                <td><strong>포트폴리오 3</strong></td>
                <td></td>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(row, index) in rows" :key="index" :row="row">
                  <td>
                    <!-- <md-autocomplete
                      v-model="row.stock"
                      :md-options="list"
                      md-layout="box"
                      md-dense>
                      <label>종목 검색</label>
                    </md-autocomplete> -->

                    <autocomplete-vue
                      classPrefix="my-custom-class"
                        v-model="row.stock"
                        :list=list
                        placeholder="종목 검색"
                        :threshold="0"
                    ></autocomplete-vue>
                    <!-- threshold: 필요 글자수 -->
                  </td>
                  <td style="width:15%"><input type="number" v-model="row.portfolio1" :disabled="row.stock==''" style="width:80%">%</td>
                  <td style="width:15%"><input type="number" v-model="row.portfolio2" :disabled="row.stock==''" style="width:80%">%</td>
                  <td style="width:15%"><input type="number" v-model="row.portfolio3" :disabled="row.stock==''" style="width:80%">%</td>
                  <td style="width:5%">
                    <n-button @click="removeRow(index)" type="neutral">
                      <i class="fa fa-trash-alt"></i>
                    </n-button>
                  </td>
                </tr>
                <tr>
                  <td>합계</td>
                  <td>{{sum1}}%</td>
                  <td>{{sum2}}%</td>
                  <td>{{sum3}}%</td>
                  <td></td>
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

        <!-- 시뮬레이션 버튼 -->
        <n-button type="primary" outline round @click="test(rows)">
          <i class="now-ui-icons objects_spaceship"></i> &nbsp; 시뮬레이션
        </n-button>
        
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
      startYear: 2019,
      startMonth: 1,
      endYear: 2020,
      endMonth: 4,
      yearOptions: [2020],
      monthOptions: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
      initAmount: 1000000,
      rebalancing: '재분배하지 않음',
      rebalancingOptions: [{code: 1, content: '재분배하지 않음'}, {code: 2, content: '1년마다'}, {code: 3, content: '6개월마다'}],
      employees: [
        'Jim Halpert',
        'Dwight Schrute',
        'Michael Scott',
        'Pam Beesly',
        'Angela Martin',
        'Kelly Kapoor',
        'Ryan Howard',
        'Kevin Malone',
        'Creed Bratton',
        'Oscar Nunez',
        'Toby Flenderson',
        'Stanley Hudson',
        'Meredith Palmer',
        'Phyllis Lapin-Vance'
      ],
      list: [
        {name: 'LG전자(123)'}, {name: '삼성전자(142)'}, {name: '현대자동차(241)'}
      ],
      columns: ["stock", "portfolio1", "portfolio2", "portfolio3"],
      rows: [
        { stock: "", portfolio1: 0, portfolio2: 0, portfolio3: 0, },
        { stock: "", portfolio1: 0, portfolio2: 0, portfolio3: 0, },
        { stock: "", portfolio1: 0, portfolio2: 0, portfolio3: 0, },
      ],
      modals: {
        save: false,
      },
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
    userLogined() {
      var user = this.$session.get('user');
      if(user) {
        return true;
      }
      else {
        return false;
      }
    }
  },
};
</script>
<style>
.period {
  font-size: 3vh;
}
</style>
