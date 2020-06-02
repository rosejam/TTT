<template>
  <div class="content">

    <!-- 페이지 헤더 -->
    <div class="page-header page-header-small">

      <!-- 배경사진 -->
      <parallax
        class="page-header-image"
        style="background-image: url('img/calculator.jpg')"
      >
      </parallax>

      <!-- 페이지 타이틀 -->
      <div class="content-center">
        <div class="container">
          <h1 class="title">포트폴리오 테스트</h1>
        </div>
      </div>
    </div>

    <!-- 컨텐츠 영역 -->
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
          <v-select v-model="testData.period" :options="periodOptions" :reduce="content => content.code" label="content" />
        </div>

        <!-- 초기금액 설정 -->
        <div class="col-md-1">
          <p>초기금액(원)</p>
        </div>
        <div class="col-md-2">
          <fg-input type="number" v-model="testData.initAmount"></fg-input>
        </div>

        <!-- 자산 재분배 -->
        <div class="col-md-1">
          <p>재분배 주기</p>
        </div>
        <div class="col-md-2">
          <v-select v-model="testData.rebalancing" :options="rebalancingOptions" :reduce="content => content.code" label="content" />
        </div>
      </div>
      <br/>

      <div class="row">

        <!-- 시작일 select -->
        <div class="col-md-1">
          <p>시작 연도</p>
        </div>
        <div class="col-md-2">
          <v-select v-model="testData.startYear" :options=yearOptions></v-select>
        </div>
        <div class="col-md-1" v-if="isMonth">
          <p>시작 월</p>
        </div>
        <div class="col-md-1" v-if="isMonth">
          <v-select v-model="testData.startMonth" :options=monthOptions></v-select>
        </div>

        <!-- 종료일 -->
        <div class="col-md-1">
          <p>종료 연도</p>
        </div>
        <div class="col-md-2">
          <v-select v-model="testData.endYear" :options=yearOptions></v-select>
        </div>
        <div class="col-md-1" v-if="isMonth">
          <p>종료 월</p>
        </div>
        <div class="col-md-1" v-if="isMonth">
          <v-select v-model="testData.endMonth" :options=monthOptions></v-select>
        </div>
      </div>
      <br/>

      <!-- 설정한 기간 -->
      <div class="period">
        <span>설정 기간: {{testData.startYear}} 년</span> <span v-if="isMonth"> {{testData.startMonth}} 월</span> <span>~ {{testData.endYear}} 년</span> <span v-if="isMonth"> {{testData.endMonth}} 월 </span>
      </div>
      <br/>

      <!-- 포트폴리오 저장 버튼 -->
      <!-- <n-button type="primary" outline round @click.native="modals.save = true"
                v-if="userInfo.email!=null">
        <i class="fa fa-save"></i> &nbsp; 포트폴리오 저장
      </n-button> -->

      <!-- 포트폴리오 테이블 -->
      <div style="width:95%; margin:auto">
        <table class="table" style="width:95%">
          <thead>
            <tr>
              <td>종목</td>
              <td><strong>#1</strong></td>
              <td><strong>#2</strong></td>
              <td><strong>#3</strong></td>
              <td></td>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(row, index) in testData.stocks" :key="index" :row="row">
                <td>
                  <v-select v-model="row.stock" :options="stockList" :reduce="content => content.code" label="content" />
                </td>
                <!-- <td style="width:15%"><fg-input type="number" v-model="row.portfolio1" :disabled="row.stock==''" style="width:50%"></fg-input>%</td> -->
                <td style="width:15%">
                  <fg-input type="number"
                            v-model="row.portfolio1"
                            placeholder="비율(%)"
                            :disabled="row.stock==null">
                  </fg-input>
                </td>
                <td style="width:15%">
                  <fg-input type="number"
                            v-model="row.portfolio2"
                            placeholder="비율(%)"
                            :disabled="row.stock==null">
                  </fg-input>
                </td>
                <td style="width:15%">
                  <fg-input type="number"
                            v-model="row.portfolio3"
                            placeholder="비율(%)"
                            :disabled="row.stock==null">
                  </fg-input>
                </td>
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

      <!-- 테스트 버튼 -->
      <n-button type="primary" outline round @click="test(testData)">
        <i class="now-ui-icons objects_spaceship"></i> &nbsp; 테스트
      </n-button>

      <!-- 차트 영역 -->
      <div v-if="testClicked" class="row text-center" style="margin:auto">
        <card>
          <n-button icon round @click="testClicked=false">
            <i class="now-ui-icons ui-1_simple-remove"></i>
          </n-button>
          <chart
            :portfolio1_data="portfolio1_data"
            :portfolio2_data="portfolio2_data"
            :portfolio3_data="portfolio3_data"
          ></chart>
        </card>
      </div>

      <!-- 포트폴리오 저장 버튼 -->
      <n-button type="primary" outline round @click.native="modals.save = true"
                v-if="userInfo.email!=null && testClicked">
        <i class="fa fa-save"></i> &nbsp; 포트폴리오 저장
      </n-button>

      <!-- 저장 버튼 클릭 시 Modal 창 -->
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
      
    </div>
  </div>
</template>
<script>
import { mapState, mapActions, mapMutations } from "vuex";
import api from "@/api";
import { Button, FormGroupInput, Modal } from '@/components';
import { Card } from "@/components/index";
import Chart from '@/components/Charts/Chart.vue';

export default {
  name: 'testing',
  bodyClass: 'testing-page',
  components: {
    [Button.name]:Button,
    [FormGroupInput.name]: FormGroupInput,
    Modal,
    Card,
    Chart,
  },
  data() {
    return {
      testClicked: false,   // 테스트 버튼 눌렀는지 여부

      periodOptions: [{code: 'Y', content: 'Year to Year'}, {code: 'M', content: 'Month to Month'}],
      yearOptions: [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
      monthOptions: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
      rebalancingOptions: [{code: -1, content: '재분배하지 않음'}, {code: 12, content: '1년마다'}, {code: 6, content: '6개월마다'}, {code: 3, content: '3개월마다'}],
      stockList: [{code: 'A066570', content: 'LG전자[A066570]'}, {code: 'A005930', content: '삼성전자[A005930]'}, {code: 'A005380', content: '현대자동차[A005380]'}],
      columns: ["stock", "portfolio1", "portfolio2", "portfolio3"],
      // 테스트 데이터
      testData: {
        period: {code: 'Y', content: 'Year to Year'},
        startYear: 2000,
        startMonth: 1,
        endYear: 2020,
        endMonth: 4,
        initAmount: 1000000,
        rebalancing: {code: -1, content: '재분배하지 않음'},
        stocks: [
          { stock: null, portfolio1: null, portfolio2: null, portfolio3: null },
          { stock: null, portfolio1: null, portfolio2: null, portfolio3: null },
          { stock: null, portfolio1: null, portfolio2: null, portfolio3: null },
        ],
      },
      modals: {
        save: false,
      },
      portfolio1_data: [
        { time: '2018-10-19', value: 219.31 },
        { time: '2018-10-22', value: 220.65 },
        { time: '2018-10-23', value: 222.73 },
        { time: '2018-10-24', value: 215.09 },
        { time: '2018-10-25', value: 219.8 },
        { time: '2018-10-26', value: 216.3 },
        { time: '2018-10-29', value: 212.24 },
        { time: '2018-10-30', value: 213.3 },
        { time: '2018-10-31', value: 218.86 },
        { time: '2018-11-01', value: 222.22 },
        { time: '2018-11-02', value: 207.48 },
        { time: '2018-11-05', value: 201.59 },
        { time: '2018-11-06', value: 203.77 },
        { time: '2018-11-07', value: 209.95 },
        { time: '2018-11-08', value: 208.49 },
        { time: '2018-11-09', value: 204.47 },
        { time: '2018-11-12', value: 194.17 },
        { time: '2018-11-13', value: 192.23 },
        { time: '2018-11-14', value: 186.8 },
        { time: '2018-11-15', value: 191.41 },
        { time: '2018-11-16', value: 193.53 },
        { time: '2018-11-19', value: 185.86 },
        { time: '2018-11-20', value: 176.98 },
        { time: '2018-11-21', value: 176.78 },
        { time: '2018-11-23', value: 172.29 },
        { time: '2018-11-26', value: 174.62 },
        { time: '2018-11-27', value: 174.24 },
        { time: '2018-11-28', value: 180.94 },
        { time: '2018-11-29', value: 179.55 },
        { time: '2018-11-30', value: 178.58 },
        { time: '2018-12-03', value: 184.82 },
        { time: '2018-12-04', value: 176.69 },
        { time: '2018-12-06', value: 174.72 },
        { time: '2018-12-07', value: 168.49 },
        { time: '2018-12-10', value: 169.6 },
        { time: '2018-12-11', value: 168.63 },
        { time: '2018-12-12', value: 169.1 },
        { time: '2018-12-13', value: 170.95 },
        { time: '2018-12-14', value: 165.48 },
        { time: '2018-12-17', value: 163.94 },
        { time: '2018-12-18', value: 166.07 },
        { time: '2018-12-19', value: 160.89 },
        { time: '2018-12-20', value: 156.83 },
        { time: '2018-12-21', value: 150.73 },
        { time: '2018-12-24', value: 146.83 },
        { time: '2018-12-26', value: 157.17 },
        { time: '2018-12-27', value: 156.15 },
        { time: '2018-12-28', value: 156.23 },
        { time: '2018-12-31', value: 157.74 },
        { time: '2019-01-02', value: 157.92 },
        { time: '2019-01-03', value: 142.19 },
        { time: '2019-01-04', value: 148.26 },
        { time: '2019-01-07', value: 147.93 },
        { time: '2019-01-08', value: 150.75 },
        { time: '2019-01-09', value: 153.31 },
        { time: '2019-01-10', value: 153.8 },
        { time: '2019-01-11', value: 152.29 },
        { time: '2019-01-14', value: 150 },
        { time: '2019-01-15', value: 153.07 },
        { time: '2019-01-16', value: 154.94 },
        { time: '2019-01-17', value: 155.86 },
        { time: '2019-01-18', value: 156.82 },
        { time: '2019-01-22', value: 153.3 },
        { time: '2019-01-23', value: 153.92 },
        { time: '2019-01-24', value: 152.7 },
        { time: '2019-01-25', value: 157.76 },
        { time: '2019-01-28', value: 156.3 },
        { time: '2019-01-29', value: 154.68 },
        { time: '2019-01-30', value: 165.25 },
        { time: '2019-01-31', value: 166.44 },
        { time: '2019-02-01', value: 166.52 },
        { time: '2019-02-04', value: 171.25 },
        { time: '2019-02-05', value: 174.18 },
        { time: '2019-02-06', value: 174.24 },
        { time: '2019-02-07', value: 170.94 },
        { time: '2019-02-08', value: 170.41 },
        { time: '2019-02-11', value: 169.43 },
        { time: '2019-02-12', value: 170.89 },
        { time: '2019-02-13', value: 170.18 },
        { time: '2019-02-14', value: 170.8 },
        { time: '2019-02-15', value: 170.42 },
        { time: '2019-02-19', value: 170.93 },
        { time: '2019-02-20', value: 172.03 },
        { time: '2019-02-21', value: 171.06 },
        { time: '2019-02-22', value: 172.97 },
        { time: '2019-02-25', value: 174.23 },
        { time: '2019-02-26', value: 174.33 },
        { time: '2019-02-27', value: 174.87 },
        { time: '2019-02-28', value: 173.15 },
        { time: '2019-03-01', value: 174.97 },
        { time: '2019-03-04', value: 175.85 },
        { time: '2019-03-05', value: 175.53 },
        { time: '2019-03-06', value: 174.52 },
        { time: '2019-03-07', value: 172.5 },
        { time: '2019-03-08', value: 172.91 },
        { time: '2019-03-11', value: 178.9 },
        { time: '2019-03-12', value: 180.91 },
        { time: '2019-03-13', value: 181.71 },
        { time: '2019-03-14', value: 183.73 },
        { time: '2019-03-15', value: 186.12 },
        { time: '2019-03-18', value: 188.02 },
        { time: '2019-03-19', value: 186.53 },
        { time: '2019-03-20', value: 188.16 },
        { time: '2019-03-21', value: 195.09 },
        { time: '2019-03-22', value: 191.05 },
        { time: '2019-03-25', value: 188.74 },
        { time: '2019-03-26', value: 186.79 },
        { time: '2019-03-27', value: 188.47 },
        { time: '2019-03-28', value: 188.72 },
        { time: '2019-03-29', value: 189.95 },
        { time: '2019-04-01', value: 191.24 },
        { time: '2019-04-02', value: 194.02 },
        { time: '2019-04-03', value: 195.35 },
        { time: '2019-04-04', value: 195.69 },
        { time: '2019-04-05', value: 197 },
        { time: '2019-04-08', value: 200.1 },
        { time: '2019-04-09', value: 199.5 },
        { time: '2019-04-10', value: 200.62 },
        { time: '2019-04-11', value: 198.95 },
        { time: '2019-04-12', value: 198.87 },
        { time: '2019-04-15', value: 199.23 },
        { time: '2019-04-16', value: 199.25 },
        { time: '2019-04-17', value: 203.13 },
        { time: '2019-04-18', value: 203.86 },
        { time: '2019-04-22', value: 204.53 },
        { time: '2019-04-23', value: 207.48 },
        { time: '2019-04-24', value: 207.16 },
        { time: '2019-04-25', value: 205.28 },
        { time: '2019-04-26', value: 204.3 },
        { time: '2019-04-29', value: 204.61 },
        { time: '2019-04-30', value: 200.67 },
        { time: '2019-05-01', value: 210.52 },
        { time: '2019-05-02', value: 209.15 },
        { time: '2019-05-03', value: 211.75 },
        { time: '2019-05-06', value: 208.48 },
        { time: '2019-05-07', value: 202.86 },
        { time: '2019-05-08', value: 202.9 },
        { time: '2019-05-09', value: 200.72 },
        { time: '2019-05-10', value: 197.18 },
        { time: '2019-05-13', value: 185.72 },
        { time: '2019-05-14', value: 188.66 },
        { time: '2019-05-15', value: 190.92 },
        { time: '2019-05-16', value: 190.08 },
        { time: '2019-05-17', value: 189 },
        { time: '2019-05-20', value: 183.09 },
        { time: '2019-05-21', value: 186.6 },
        { time: '2019-05-22', value: 182.78 },
        { time: '2019-05-23', value: 179.66 },
        { time: '2019-05-24', value: 178.97 },
        { time: '2019-05-28', value: 179.07 },
      ],
      portfolio2_data: [
        { time: '2018-10-19', value: 144 },
        { time: '2018-10-22', value: 143.14 },
        { time: '2018-10-23', value: 142.3 },
        { time: '2018-10-24', value: 140.99 },
        { time: '2018-10-25', value: 141.59 },
        { time: '2018-10-26', value: 141.1 },
        { time: '2018-10-29', value: 141.03 },
        { time: '2018-10-30', value: 142.21 },
        { time: '2018-10-31', value: 143.37 },
        { time: '2018-11-01', value: 142.65 },
        { time: '2018-11-02', value: 141.6 },
        { time: '2018-11-05', value: 142.61 },
        { time: '2018-11-06', value: 142.66 },
        { time: '2018-11-07', value: 143.11 },
        { time: '2018-11-08', value: 141.27 },
        { time: '2018-11-09', value: 141.24 },
        { time: '2018-11-12', value: 140.87 },
        { time: '2018-11-13', value: 139.81 },
        { time: '2018-11-14', value: 140.33 },
        { time: '2018-11-15', value: 141.16 },
        { time: '2018-11-16', value: 140.84 },
        { time: '2018-11-19', value: 140.92 },
        { time: '2018-11-20', value: 140.1 },
        { time: '2018-11-21', value: 141.27 },
        { time: '2018-11-23', value: 139.89 },
        { time: '2018-11-26', value: 140.53 },
        { time: '2018-11-27', value: 140.32 },
        { time: '2018-11-28', value: 140.84 },
        { time: '2018-11-29', value: 140.48 },
        { time: '2018-11-30', value: 140.35 },
        { time: '2018-12-03', value: 141.19 },
        { time: '2018-12-04', value: 140.95 },
        { time: '2018-12-06', value: 139.59 },
        { time: '2018-12-07', value: 139.51 },
        { time: '2018-12-10', value: 139.37 },
        { time: '2018-12-11', value: 139.08 },
        { time: '2018-12-12', value: 139.05 },
        { time: '2018-12-13', value: 139.29 },
        { time: '2018-12-14', value: 138.66 },
        { time: '2018-12-17', value: 138.41 },
        { time: '2018-12-18', value: 137.82 },
        { time: '2018-12-19', value: 137.65 },
        { time: '2018-12-20', value: 137.26 },
        { time: '2018-12-21', value: 137.67 },
        { time: '2018-12-24', value: 136.65 },
        { time: '2018-12-26', value: 138.06 },
        { time: '2018-12-27', value: 137.73 },
        { time: '2018-12-28', value: 138.13 },
        { time: '2018-12-31', value: 137.92 },
        { time: '2019-01-02', value: 138.59 },
        { time: '2019-01-03', value: 138.81 },
        { time: '2019-01-04', value: 140.03 },
        { time: '2019-01-07', value: 140.16 },
        { time: '2019-01-08', value: 140.03 },
        { time: '2019-01-09', value: 140.36 },
        { time: '2019-01-10', value: 140.7 },
        { time: '2019-01-11', value: 140.24 },
        { time: '2019-01-14', value: 140.42 },
        { time: '2019-01-15', value: 140.24 },
        { time: '2019-01-16', value: 140.12 },
        { time: '2019-01-17', value: 140.13 },
        { time: '2019-01-18', value: 140.76 },
        { time: '2019-01-22', value: 140.08 },
        { time: '2019-01-23', value: 140.12 },
        { time: '2019-01-24', value: 140.11 },
        { time: '2019-01-25', value: 140.11 },
        { time: '2019-01-28', value: 139.57 },
        { time: '2019-01-29', value: 140.2 },
        { time: '2019-01-30', value: 140.67 },
        { time: '2019-01-31', value: 141.12 },
        { time: '2019-02-01', value: 141.34 },
        { time: '2019-02-04', value: 141.39 },
        { time: '2019-02-05', value: 142.82 },
        { time: '2019-02-06', value: 143.04 },
        { time: '2019-02-07', value: 142.7 },
        { time: '2019-02-08', value: 142.49 },
        { time: '2019-02-11', value: 142.21 },
        { time: '2019-02-12', value: 142.42 },
        { time: '2019-02-13', value: 142.64 },
        { time: '2019-02-14', value: 141.87 },
        { time: '2019-02-15', value: 142.29 },
        { time: '2019-02-19', value: 142.38 },
        { time: '2019-02-20', value: 142.48 },
        { time: '2019-02-21', value: 142.29 },
        { time: '2019-02-22', value: 142.46 },
        { time: '2019-02-25', value: 142.51 },
        { time: '2019-02-26', value: 142.52 },
        { time: '2019-02-27', value: 142.84 },
        { time: '2019-02-28', value: 142.65 },
        { time: '2019-03-01', value: 142.58 },
        { time: '2019-03-04', value: 142.64 },
        { time: '2019-03-05', value: 142.74 },
        { time: '2019-03-06', value: 142.7 },
        { time: '2019-03-07', value: 142.63 },
        { time: '2019-03-08', value: 142.25 },
        { time: '2019-03-11', value: 142.33 },
        { time: '2019-03-12', value: 142.46 },
        { time: '2019-03-13', value: 143.83 },
        { time: '2019-03-14', value: 143.95 },
        { time: '2019-03-15', value: 143.87 },
        { time: '2019-03-18', value: 144.24 },
        { time: '2019-03-19', value: 144.47 },
        { time: '2019-03-20', value: 144.53 },
        { time: '2019-03-21', value: 144.53 },
        { time: '2019-03-22', value: 143.95 },
        { time: '2019-03-25', value: 143.53 },
        { time: '2019-03-26', value: 143.82 },
        { time: '2019-03-27', value: 143.59 },
        { time: '2019-03-28', value: 143.63 },
        { time: '2019-03-29', value: 143.72 },
        { time: '2019-04-01', value: 144.09 },
        { time: '2019-04-02', value: 144.23 },
        { time: '2019-04-03', value: 144.23 },
        { time: '2019-04-04', value: 144.15 },
        { time: '2019-04-05', value: 144.53 },
        { time: '2019-04-08', value: 145.23 },
        { time: '2019-04-09', value: 144.99 },
        { time: '2019-04-10', value: 145.04 },
        { time: '2019-04-11', value: 144.87 },
        { time: '2019-04-12', value: 144.67 },
        { time: '2019-04-15', value: 144.67 },
        { time: '2019-04-16', value: 144.48 },
        { time: '2019-04-17', value: 144.62 },
        { time: '2019-04-18', value: 144.39 },
        { time: '2019-04-22', value: 145.04 },
        { time: '2019-04-23', value: 145.02 },
        { time: '2019-04-24', value: 144.13 },
        { time: '2019-04-25', value: 143.96 },
        { time: '2019-04-26', value: 143.31 },
        { time: '2019-04-29', value: 143.02 },
        { time: '2019-04-30', value: 143.73 },
        { time: '2019-05-01', value: 143.08 },
        { time: '2019-05-02', value: 142.63 },
        { time: '2019-05-03', value: 143.08 },
        { time: '2019-05-06', value: 142.93 },
        { time: '2019-05-07', value: 142.22 },
        { time: '2019-05-08', value: 142.28 },
        { time: '2019-05-09', value: 141.65 },
        { time: '2019-05-10', value: 141.5 },
        { time: '2019-05-13', value: 141.23 },
        { time: '2019-05-14', value: 141.55 },
        { time: '2019-05-15', value: 141.77 },
        { time: '2019-05-16', value: 142.28 },
        { time: '2019-05-17', value: 142.34 },
        { time: '2019-05-20', value: 142.58 },
        { time: '2019-05-21', value: 142.75 },
        { time: '2019-05-22', value: 142.34 },
        { time: '2019-05-23', value: 141.34 },
        { time: '2019-05-24', value: 141.76 },
        { time: '2019-05-28', value: 141.625 },
      ],
      portfolio3_data: [
        { time: '2018-10-19', value: 44 },
        { time: '2018-10-22', value: 43.14 },
        { time: '2018-10-23', value: 42.3 },
        { time: '2018-10-24', value: 40.99 },
        { time: '2018-10-25', value: 41.59 },
        { time: '2018-10-26', value: 41.1 },
        { time: '2018-10-29', value: 41.03 },
        { time: '2018-10-30', value: 42.21 },
        { time: '2018-10-31', value: 43.37 },
        { time: '2018-11-01', value: 42.65 },
        { time: '2018-11-02', value: 41.6 },
        { time: '2018-11-05', value: 42.61 },
        { time: '2018-11-06', value: 42.66 },
        { time: '2018-11-07', value: 43.11 },
        { time: '2018-11-08', value: 41.27 },
        { time: '2018-11-09', value: 41.24 },
        { time: '2018-11-12', value: 40.87 },
        { time: '2018-11-13', value: 39.81 },
        { time: '2018-11-14', value: 40.33 },
        { time: '2018-11-15', value: 41.16 },
        { time: '2018-11-16', value: 40.84 },
        { time: '2018-11-19', value: 40.92 },
        { time: '2018-11-20', value: 40.1 },
        { time: '2018-11-21', value: 41.27 },
        { time: '2018-11-23', value: 39.89 },
        { time: '2018-11-26', value: 40.53 },
        { time: '2018-11-27', value: 40.32 },
        { time: '2018-11-28', value: 40.84 },
        { time: '2018-11-29', value: 40.48 },
        { time: '2018-11-30', value: 40.35 },
        { time: '2018-12-03', value: 41.19 },
        { time: '2018-12-04', value: 40.95 },
        { time: '2018-12-06', value: 39.59 },
        { time: '2018-12-07', value: 39.51 },
        { time: '2018-12-10', value: 39.37 },
        { time: '2018-12-11', value: 39.08 },
        { time: '2018-12-12', value: 39.05 },
        { time: '2018-12-13', value: 39.29 },
        { time: '2018-12-14', value: 38.66 },
        { time: '2018-12-17', value: 38.41 },
        { time: '2018-12-18', value: 37.82 },
        { time: '2018-12-19', value: 37.65 },
        { time: '2018-12-20', value: 37.26 },
        { time: '2018-12-21', value: 37.67 },
        { time: '2018-12-24', value: 36.65 },
        { time: '2018-12-26', value: 38.06 },
        { time: '2018-12-27', value: 37.73 },
        { time: '2018-12-28', value: 38.13 },
        { time: '2018-12-31', value: 37.92 },
        { time: '2019-01-02', value: 38.59 },
        { time: '2019-01-03', value: 38.81 },
        { time: '2019-01-04', value: 40.03 },
        { time: '2019-01-07', value: 40.16 },
        { time: '2019-01-08', value: 40.03 },
        { time: '2019-01-09', value: 40.36 },
        { time: '2019-01-10', value: 40.7 },
        { time: '2019-01-11', value: 40.24 },
        { time: '2019-01-14', value: 40.42 },
        { time: '2019-01-15', value: 40.24 },
        { time: '2019-01-16', value: 40.12 },
        { time: '2019-01-17', value: 40.13 },
        { time: '2019-01-18', value: 40.76 },
        { time: '2019-01-22', value: 40.08 },
        { time: '2019-01-23', value: 40.12 },
        { time: '2019-01-24', value: 40.11 },
        { time: '2019-01-25', value: 40.11 },
        { time: '2019-01-28', value: 39.57 },
        { time: '2019-01-29', value: 40.2 },
        { time: '2019-01-30', value: 40.67 },
        { time: '2019-01-31', value: 41.12 },
        { time: '2019-02-01', value: 41.34 },
        { time: '2019-02-04', value: 41.39 },
        { time: '2019-02-05', value: 42.82 },
        { time: '2019-02-06', value: 43.04 },
        { time: '2019-02-07', value: 42.7 },
        { time: '2019-02-08', value: 42.49 },
        { time: '2019-02-11', value: 42.21 },
        { time: '2019-02-12', value: 42.42 },
        { time: '2019-02-13', value: 42.64 },
        { time: '2019-02-14', value: 41.87 },
        { time: '2019-02-15', value: 42.29 },
        { time: '2019-02-19', value: 42.38 },
        { time: '2019-02-20', value: 42.48 },
        { time: '2019-02-21', value: 42.29 },
        { time: '2019-02-22', value: 42.46 },
        { time: '2019-02-25', value: 42.51 },
        { time: '2019-02-26', value: 42.52 },
        { time: '2019-02-27', value: 42.84 },
        { time: '2019-02-28', value: 42.65 },
        { time: '2019-03-01', value: 42.58 },
        { time: '2019-03-04', value: 42.64 },
        { time: '2019-03-05', value: 42.74 },
        { time: '2019-03-06', value: 42.7 },
        { time: '2019-03-07', value: 42.63 },
        { time: '2019-03-08', value: 42.25 },
        { time: '2019-03-11', value: 42.33 },
        { time: '2019-03-12', value: 42.46 },
        { time: '2019-03-13', value: 43.83 },
        { time: '2019-03-14', value: 43.95 },
        { time: '2019-03-15', value: 43.87 },
        { time: '2019-03-18', value: 44.24 },
        { time: '2019-03-19', value: 44.47 },
        { time: '2019-03-20', value: 44.53 },
        { time: '2019-03-21', value: 44.53 },
        { time: '2019-03-22', value: 43.95 },
        { time: '2019-03-25', value: 43.53 },
        { time: '2019-03-26', value: 43.82 },
        { time: '2019-03-27', value: 43.59 },
        { time: '2019-03-28', value: 43.63 },
        { time: '2019-03-29', value: 43.72 },
        { time: '2019-04-01', value: 44.09 },
        { time: '2019-04-02', value: 44.23 },
        { time: '2019-04-03', value: 44.23 },
        { time: '2019-04-04', value: 44.15 },
        { time: '2019-04-05', value: 44.53 },
        { time: '2019-04-08', value: 45.23 },
        { time: '2019-04-09', value: 44.99 },
        { time: '2019-04-10', value: 45.04 },
        { time: '2019-04-11', value: 44.87 },
        { time: '2019-04-12', value: 44.67 },
        { time: '2019-04-15', value: 44.67 },
        { time: '2019-04-16', value: 44.48 },
        { time: '2019-04-17', value: 44.62 },
        { time: '2019-04-18', value: 44.39 },
        { time: '2019-04-22', value: 45.04 },
        { time: '2019-04-23', value: 45.02 },
        { time: '2019-04-24', value: 44.13 },
        { time: '2019-04-25', value: 43.96 },
        { time: '2019-04-26', value: 43.31 },
        { time: '2019-04-29', value: 43.02 },
        { time: '2019-04-30', value: 43.73 },
        { time: '2019-05-01', value: 43.08 },
        { time: '2019-05-02', value: 42.63 },
        { time: '2019-05-03', value: 43.08 },
        { time: '2019-05-06', value: 42.93 },
        { time: '2019-05-07', value: 42.22 },
        { time: '2019-05-08', value: 42.28 },
        { time: '2019-05-09', value: 41.65 },
        { time: '2019-05-10', value: 41.5 },
        { time: '2019-05-13', value: 41.23 },
        { time: '2019-05-14', value: 41.55 },
        { time: '2019-05-15', value: 41.77 },
        { time: '2019-05-16', value: 42.28 },
        { time: '2019-05-17', value: 42.34 },
        { time: '2019-05-20', value: 42.58 },
        { time: '2019-05-21', value: 42.75 },
        { time: '2019-05-22', value: 42.34 },
        { time: '2019-05-23', value: 41.34 },
        { time: '2019-05-24', value: 41.76 },
        { time: '2019-05-28', value: 41.625 },
      ],
    }
  },
  methods:{
    ...mapActions("stock", ["getTestData"]),

    // 테스트 버튼 클릭 시 실행되는 함수
    async test(data) {
      const stocks = data.stocks;
      for (let i = 0; i < stocks.length; i++) {
        const stock = stocks[i];

        // 입력받은 % 값 검사
        if(stock.portfolio1 < 0 || stock.portfolio1 > 100 ||
           stock.portfolio2 < 0 || stock.portfolio2 > 100 ||
           stock.portfolio3 < 0 || stock.portfolio3 > 100) {
          alert("0~100(%) 사이 숫자만 입력 가능합니다");
          return;
        }
      }

      // % 합계 검사
      if((this.sum1 > 0 && this.sum1 != 100) ||
         (this.sum2 > 0 && this.sum2 != 100) ||
         (this.sum3 > 0 && this.sum3 != 100)) {
          alert("포트폴리오 합계는 100%로 맞춰주세요");
          return;
      }

      // 종료일자 검사
      const year = new Date().getFullYear();
      const month = new Date().getMonth() - 1;
      if(data.endYear >= year && data.endMonth > month) {
        let msg = "종료일자는 " + year.toString() + "년 " + month.toString() + "월 이전으로 설정해주세요"
        alert("종료일자는 " + year.toString() + "년 " + month.toString() + "월 이전으로 설정해주세요");
        return;
      }

      // 시작일자 < 종료일자 검사
      let valid = true;
      if(data.period.code=='Y') {
        if(data.startYear >= data.endYear) {
          valid = false;
        }
      }
      else {
        if(data.startYear > data.endYear) {
          valid = false;
        }
        else if(data.startYear == data.endYear && data.startMonth >= data.endMonth) {
          valid = false;

        }
      }

      if(!valid) {
        alert("시작일자는 종료일자보다 이전으로 설정해주세요");
        return;
      }

      this.testClicked = false;
      console.log('test start...',data);
      const result = await this.getTestData(data);
      // console.log(result);
      this.testClicked = true;
    },
    // 행 추가
    addRow() {
      this.testData.stocks.push({ stock: "", portfolio1: 0, portfolio2: 0, portfolio3: 0, });
    },
    // 행 삭제
    removeRow(index) {
      this.testData.stocks.splice(index, 1);
    },
    // 포트폴리오 % 계산
    calc(p) {
      var sum = 0;

      if(p==1) {
        for (let i = 0; i < this.testData.stocks.length; i++) {
          const row = this.testData.stocks[i];
          sum += Number(row.portfolio1);
        }
      }
      else if(p==2) {
        for (let i = 0; i < this.testData.stocks.length; i++) {
          const row = this.testData.stocks[i];
          sum += Number(row.portfolio2);
        }
      }
      else {
        for (let i = 0; i < this.testData.stocks.length; i++) {
          const row = this.testData.stocks[i];
          sum += Number(row.portfolio3);
        }
      }

      return sum;
    },
  },
  computed: {
    ...mapState("user", ["userInfo"]),
    // 기간이 월~월 인지 여부
    isMonth() {
      if(this.testData.period == 'M') return true;
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
<style>
.period {
  font-size: 3vh;
}
</style>
