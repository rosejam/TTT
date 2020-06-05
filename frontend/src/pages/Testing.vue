<!-- /test -->
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
        <div class="col-md-2"></div>
        <div class="row col-md-10 ym">

          <!-- 기간 select -->
          <div class="col-md-1">
            <p>기간 설정</p>
          </div>
          <div class="col-md-2">
            <v-select v-model="testData.period" :options="periodOptions" :reduce="content => content.code" label="content" placeholder="테스트 기간 선택"/>
          </div>

          <!-- 시작 금액 설정 -->
          <div class="col-md-1">
            <p>시작금액(원)</p>
          </div>
          <div class="col-md-2">
            <fg-input type="number" v-model="testData.initAmount"></fg-input>
          </div>

          <!-- 자산 재분배 -->
          <div class="col-md-1">
            <p>재분배 주기</p>
          </div>
          <div class="col-md-2">
            <v-select v-model="testData.rebalancing" :options="rebalancingOptions" :reduce="content => content.code" label="content" placeholder="재분배 주기 선택"/>
          </div>
        </div>
      </div>
      <br/>

      <!-- 시작일, 종료일 설정 -->
      <div class="row" v-if="testData.period != null">
        <div class="col-md-2"></div>
        <div class="row col-md-8 ym">

          <!-- 시작일 select -->
          <div class="col-md-1">
            <p>시작 연도</p>
          </div>
          <div class="col-md-2">
            <v-select v-model="testData.startYear" :options=yearOptions></v-select>
          </div>
          <div class="col-md-1" v-if="testData.period == 'M'">
            <p>시작 월</p>
          </div>
          <div class="col-md-2" v-if="testData.period == 'M'">
            <v-select v-model="testData.startMonth" :options=monthOptions></v-select>
          </div>

          <!-- 종료일 -->
          <div class="col-md-1">
            <p>종료 연도</p>
          </div>
          <div class="col-md-2">
            <v-select v-model="testData.endYear" :options=yearOptions></v-select>
          </div>
          <div class="col-md-1" v-if="testData.period == 'M'">
            <p>종료 월</p>
          </div>
          <div class="col-md-2" v-if="testData.period == 'M'">
            <v-select v-model="testData.endMonth" :options=monthOptions></v-select>
          </div>
        </div>
      </div>
      <br/>

      <!-- 설정한 기간 -->
      <div class="period" v-if="testData.period != null">
        <span>{{testData.startYear}} 년</span> <span v-if="testData.period == 'M'"> {{testData.startMonth}} 월</span> <span>~ {{testData.endYear}} 년</span> <span v-if="testData.period == 'M'"> {{testData.endMonth}} 월 </span>
      </div>
      <br/>

      <!-- 포트폴리오 설정 테이블 영역 -->
      <div class="row" style="width:100%">
        <div class="col-md-2"></div>
        <div class="table-container col-md-8">
          <table class="table" style="width:95%">

            <!-- 테이블 column 이름 -->
            <thead>
              <tr>
                <td>종목</td>
                <td><strong>#1</strong></td>
                <td><strong>#2</strong></td>
                <td><strong>#3</strong></td>
                <td></td>
              </tr>
            </thead>

            <!-- 테이블 내용 -->
            <tbody>
              <tr v-for="(row, index) in testData.stocks" :key="index" :row="row">

                <!-- 종목 검색 -->
                <td>
                  <v-select v-model="row.stock" :options="stockOptions" :reduce="content => content.code" label="content" placeholder="클릭해서 종목 검색"/>
                </td>

                <!-- #1 -->
                <td nowrap width="120">
                  <fg-input type="number"
                            v-model="row.portfolio1"
                            placeholder="비율(%)"
                            :disabled="row.stock==null">
                  </fg-input>
                </td>

                <!-- #2 -->
                <td nowrap width="120">
                  <fg-input type="number"
                            v-model="row.portfolio2"
                            placeholder="비율(%)"
                            :disabled="row.stock==null">
                  </fg-input>
                </td>

                <!-- #3 -->
                <td nowrap width="120">
                  <fg-input type="number"
                            v-model="row.portfolio3"
                            placeholder="비율(%)"
                            :disabled="row.stock==null">
                  </fg-input>
                </td>

                <!-- 행 삭제 버튼 -->
                <td style="width:1%">
                  <n-button @click="removeRow(index)" type="neutral">
                    <i class="fa fa-trash-alt"></i>
                  </n-button>
                </td>

              </tr>

              <!-- 비율(%) 합계 -->
              <tr>
                <td>합계</td>
                <td>{{sum1}}%</td>
                <td>{{sum2}}%</td>
                <td>{{sum3}}%</td>
                <td></td>
              </tr>

              <!-- 종목 추가 버튼 -->
              <tr>
                <td>
                  <n-button type="primary" icon round @click="addRow(1)">
                    <strong style="font-size:20px">+1</strong>
                  </n-button>
                  <n-button type="primary" icon round @click="addRow(5)">
                    <strong style="font-size:20px">+5</strong>
                  </n-button>
                  <n-button type="primary" icon round @click="addRow(10)">
                    <strong style="font-size:20px">+10</strong>
                  </n-button>
                  </td>
                <td colspan="3"></td>
                <td>
                  <n-button icon round @click="removeAll">
                    <i class="fa fa-trash-alt"></i>
                  </n-button>
                </td>
              </tr>

            </tbody>
          </table>
        </div>
        <div class="col-md-2"></div>
      </div>
      <!-- 포트폴리오 설정 테이블 끝 -->

      <!-- 테스트 버튼 -->
      <n-button type="primary" outline round @click="test(testData)">
        <i class="now-ui-icons objects_spaceship"></i> &nbsp; 테스트
      </n-button>

      <!-- 테스트 결과 로딩중 -->
      <div v-if="loading">
        <b-spinner variant="secondary" style="width: 3rem; height: 3rem;" label="Large Spinner"></b-spinner>
        <h3>입력값으로 테스트하는 중입니다</h3>
      </div>

      <!-- 차트 영역 -->
      <div v-if="testClicked" class="row text-center">
        <div class="col-1"></div>
        <div class="col-10">
          <card>

            <!-- 차트 -->
            <h3>테스트 결과</h3>
            <line-chart
              :portfolio1_data="portfolio1_data"
              :portfolio2_data="portfolio2_data"
              :portfolio3_data="portfolio3_data"
            ></line-chart>

            <!-- 포트폴리오 저장 버튼 -->
            <n-button type="primary" outline round @click.native="modals.save = true"
                      v-if="userInfo.uid!=null && testClicked">
              <i class="fa fa-save"></i> &nbsp; 포트폴리오 저장
            </n-button>
          </card>
        </div>
      </div>


      <!-- 저장 버튼 클릭 시 Modal 창 -->
      <modal :show.sync="modals.save" headerClasses="justify-content-center" style="color:black" modal-classes="modal-sm">
        <h4 slot="header" class="title title-up">포트폴리오 저장</h4>
        <fg-input  class="col-12"
                   v-model="portName"
                   placeholder="포트폴리오 이름">
        </fg-input>
        <div class="pull-left">
        <n-button type="neutral" round @click="modals.save = false">취소</n-button>
        </div>
        <div class="pull-right">
        <n-button type="primary" round @click="savePortfolio(testData)">저장</n-button>
        </div>
      </modal>

      <modal :show.sync="modals.complete" headerClasses="justify-content-center" style="color:black" modal-classes="modal-sm">
        <h4 slot="header" class="title title-up">저장 완료</h4>
        <n-button @click="modals.complete=false" type="primary">확인</n-button>
      </modal>
      
    </div>
  </div>
</template>
<script>
import { mapState, mapActions } from "vuex";
import { Button, FormGroupInput, Modal } from '@/components';
import { Card } from "@/components/index";
import LineChart from '@/components/Charts/LineChart.vue';
import { BSpinner } from 'bootstrap-vue';
import test from "@/utils/test";

export default {
  name: 'testing',
  bodyClass: 'testing-page',
  components: {
    [Button.name]:Button,
    [FormGroupInput.name]: FormGroupInput,
    Modal,
    Card,
    LineChart,
    BSpinner,
  },
  data() {
    return {
      testClicked: false,   // 테스트 버튼 눌렀는지 여부
      periodOptions: [{code: 'Y', content: 'Year to Year'}, {code: 'M', content: 'Month to Month'}],
      yearOptions: [],
      monthOptions: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
      rebalancingOptions: [{code: -1, content: '재분배하지 않음'}, {code: 12, content: '1년'}, {code: 6, content: '6개월'}, {code: 3, content: '3개월'}],
      stockOptions: [],
      columns: ["stock", "portfolio1", "portfolio2", "portfolio3"],
      // 테스트 데이터
      testData: {
        period: null,
        startYear: 2000,
        startMonth: 1,
        endYear: 2020,
        endMonth: new Date().getMonth(),
        initAmount: "1000000",
        rebalancing: null,
        stocks: [
          { stock: null, portfolio1: null, portfolio2: null, portfolio3: null },
          { stock: null, portfolio1: null, portfolio2: null, portfolio3: null },
          { stock: null, portfolio1: null, portfolio2: null, portfolio3: null },
        ],
      },
      modals: {
        save: false,
        complete: false,
      },
      portfolio1_data: [],
      portfolio2_data: [],
      portfolio3_data: [],
      portName: '',
      loading: false,
    }
  },
  async mounted() {
    // 연도 선택 옵션 리스트 설정
    let year = new Date().getFullYear();
    for (let i = 2000; i <= year; i++) {
      this.yearOptions.push(i);        
    }

    // 종목 리스트 삽입
    await this.setStockList();
    const list = this.stockList.stockList;
    for (let i = 0; i < list.length; i++) {
      const stock = list[i];
      this.stockOptions.push({code: stock.code, content: stock.name+'['+stock.code+']'});
    }
  },
  methods:{
    ...mapActions("stock", ["getTestData", "getStockList"]),
    ...mapActions("user", ["getUserInfo", "postPortfolio"]),

    // 주식 목록 가져오는 함수
    async setStockList() {
      await this.getStockList();
    },

    // 테스트 버튼 클릭 시 실행되는 함수
    async test(data) {

      // 유효성 검증
      if(!this.validate(data)) return;

      this.testClicked = false;
      this.loading = true;
      
      // 테스트 데이터 get
      const result = await this.getTestData(data);

      // 데이터 전처리
      const preocessed_data = test.preprocess(result);
      this.portfolio1_data = preocessed_data[0];
      this.portfolio2_data = preocessed_data[1];
      this.portfolio3_data = preocessed_data[2];

      this.loading = false;
      this.testClicked = true;
    },

    // 데이터 유효성 검증 함수
    validate(data) {

      // 기간 선택 여부 검사
      if(!data.period) {
        alert('테스트 기간을 설정해주세요');
        return false;
      }

      // 시작 금액 검사
      if(data.initAmount=="") {
        alert("시작 금액을 설정해주세요");
        return;
      }
      else {
        data.initAmount = Number(data.initAmount);
      }

      // 재분배 주기 선택 여부 검사
      if(!data.rebalancing) {
        alert('재분배 주기를 선택해주세요');
        return false;
      }

      // 연도, 월 입력 여부 검사
      if(data.startYear=="") {
        alert("시작 연도를 입력해주세요");
        return;
      }
      if(data.period=="M" && data.startMonth=="") {
        alert("시작 월을 입력해주세요");
        return;
      }
      if(data.endYear=="") {
        alert("종료 연도를 입력해주세요");
        return;
      }
      if(data.period=="M" && data.endMonth=="") {
        alert("종료 월을 입력해주세요");
        return;
      }

      // 종료일자 검사
      const year = new Date().getFullYear();
      const month = new Date().getMonth();
      if(data.endYear >= year && data.endMonth > month) {
        let msg = "종료일자는 " + year.toString() + "년 " + month.toString() + "월 이전으로 설정해주세요"
        alert("종료일자는 " + year.toString() + "년 " + month.toString() + "월 이전으로 설정해주세요");
        return false;
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
        return false;
      }

      // null, 빈값, 종목 중복 처리
      let isNull = true;
      let tmpStockList = [];
      for (let i = 0; i < data.stocks.length; i++) {
        const stock = data.stocks[i];
        if(stock.stock == null || stock.stock == "") {
          data.stocks.splice(i--, 1);
        }
        else {
          if(tmpStockList.includes(stock.stock)) {
            alert("같은 종목은 한 번만 선택해주세요");
            return;
          }
          tmpStockList.push(stock.stock);
          isNull = false;
          if(stock.portfolio1 == null || stock.portfolio1 == "") stock.portfolio1 = "0";
          if(stock.portfolio2 == null || stock.portfolio2 == "") stock.portfolio2 = "0";
          if(stock.portfolio3 == null || stock.portfolio3 == "") stock.portfolio3 = "0";

          // 입력받은 % 비율 값 검사
          if(stock.portfolio1 < 0 || stock.portfolio1 > 100 ||
             stock.portfolio2 < 0 || stock.portfolio2 > 100 ||
             stock.portfolio3 < 0 || stock.portfolio3 > 100) {
            alert("0~100(%) 사이 숫자만 입력 가능합니다");
            return false;
          }
        }
      }
      if(isNull) {
        alert("종목을 1개 이상 입력하세요");
        return;
      }


      // % 합계 검사
      if((this.sum1 > 0 && this.sum1 != 100) ||
         (this.sum2 > 0 && this.sum2 != 100) ||
         (this.sum3 > 0 && this.sum3 != 100)) {
          alert("포트폴리오 합계는 100%로 맞춰주세요");
          return false;
      }

      return true;
    },
    // 행 추가
    addRow(n) {
      for (let i = 0; i < n; i++) {
        this.testData.stocks.push({ stock: null, portfolio1: null, portfolio2: null, portfolio3: null });
      }
    },
    // 행 삭제
    removeRow(index) {
      this.testData.stocks.splice(index, 1);
    },
    // 전체 행 삭제
    removeAll() {
      this.testData.stocks = [
          { stock: null, portfolio1: null, portfolio2: null, portfolio3: null },
          { stock: null, portfolio1: null, portfolio2: null, portfolio3: null },
          { stock: null, portfolio1: null, portfolio2: null, portfolio3: null }
      ];
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
    // 포트폴리오 저장
    async savePortfolio(data) {
      if(this.portName == null || this.portName == "") {
        alert("포트폴리오 이름을 입력하세요");
        return;
      }

      const uid = localStorage.getItem("user");
      data.uid = uid;
      data.name = this.portName;

      await this.postPortfolio(data);
      await this.getUserInfo();
      this.modals.save = false;
      this.portName = "";
      this.modals.complete = true;
    },
  },
  computed: {
    ...mapState("user", ["userInfo"]),
    ...mapState("stock", ["stockList"]),
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
<style scoped>
.table-container {
  overflow-x:auto;
}
.period {
  font-size: 3vh;
}
.ym {
  font-size: 1.5vh;
}
</style>
