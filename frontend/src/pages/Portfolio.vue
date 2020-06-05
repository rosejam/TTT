<!-- /portfolio -->
<template>
  <div class="content">
    <div class="page-header page-header-small">
      <parallax
        class="page-header-image"
        style="background-image: url('img/portfolio2.jpg')"
      >
      </parallax>
      <div class="content-center">
        <div class="container">
          <h1 class="title">내 포트폴리오</h1>
        </div>
      </div>
    </div>
    <div class="section text-center">
      <div class="container">
        <h3>
          내가 작성한 <b>포트폴리오</b>를<br/>
          한눈에 확인해보세요!
        </h3>
      </div>
    </div>
    <div class="row" style="margin:auto">

      <!-- 내 포트폴리오 개수만큼 for문 -->
      <div class="col-md-4" v-for="(portfolio, i) in userInfo.portfolio" :key="i">
        <card>
          <h2 class="title title-up">#{{portfolio.name}}</h2>
          <p v-if="portfolio.period=='Y'">Year to Year</p>
          <p v-else>Month to Month</p>
          <span>{{portfolio.startYear}} 년</span>
          <span v-if="portfolio.period=='M'"> {{portfolio.startMonth}} 월</span>
          <span> ~ {{portfolio.endYear}} 년</span>
          <span v-if="portfolio.period=='M'"> {{portfolio.endMonth}} 월</span>
          <div class="row">

            <!-- 포트폴리오 삭제 버튼 -->
            <div class="text-left col-6">
              <n-button @click="portfolio.del=true" icon round>
                <i class="fa fa-trash-alt"></i>
              </n-button>
            </div>

            <!-- 자세히 보기 버튼 -->
            <div class="text-right col-6">
              <n-button @click="portfolio.detail=true" type="primary" icon round>
                <i class="now-ui-icons ui-1_zoom-bold"></i>
              </n-button>
            </div>
          </div>

          <!-- 자세히 보기 modal 창 -->
          <modal :show.sync="portfolio.detail" headerClasses="justify-content-center" style="color:black" modal-classes="modal-lg">
            <h1 slot="header">#{{portfolio.name}}</h1>
            <div class="row">
              <div class="col-md-1"></div>
              <div class="col-md-4">
                <p v-if="portfolio.period=='Y'">Year to Year</p>
                <p v-else>Month to Month</p>
                <span>{{portfolio.startYear}} 년</span>
                <span v-if="portfolio.period=='M'"> {{portfolio.startMonth}} 월</span>
                <span> ~ {{portfolio.endYear}} 년</span>
                <span v-if="portfolio.period=='M'"> {{portfolio.endMonth}} 월</span>
                <br/><br/><br/>
                <p>시작 금액: {{portfolio.initAmount}} 원</p>
                <p>재분배 주기: {{rebalncingValue(portfolio.rebalancing)}}</p>
              </div>

              <div class="col-md-7">
                <div class="table-container col-md-8">
                  <table class="table">

                    <!-- 테이블 column 이름 -->
                    <thead>
                      <tr>
                        <td>종목 ({{portfolio.stocks.length}}개)</td>
                        <td><strong>#1</strong></td>
                        <td><strong>#2</strong></td>
                        <td><strong>#3</strong></td>
                        <td></td>
                      </tr>
                    </thead>

                    <!-- 테이블 내용 -->
                    <tbody v-for="(stock, i) in portfolio.stocks" :key="i">
                      <td>
                        {{stock.name}}
                      </td>
                      <td>
                        {{stock.portfolio1}}
                      </td>
                      <td>
                        {{stock.portfolio2}}
                      </td>
                      <td>
                        {{stock.portfolio3}}
                      </td>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>

            <!-- 차트 영역 -->
            <div v-if="portfolio.testClicked" class="row text-center">
              <div class="col-1"></div>
              <div class="col-10">
                <card>

                  <!-- 차트 -->
                  <h3>테스트 결과</h3>
                    <line-chart
                      :portfolio1_data="portfolio.portfolio1_data"
                      :portfolio2_data="portfolio.portfolio2_data"
                      :portfolio3_data="portfolio.portfolio3_data"
                    ></line-chart>

                </card>
              </div>
            </div>

            <div class="row">
              <!-- 포트폴리오 삭제 버튼 -->
              <div class="text-left col-6">
                <n-button v-if="!loading" @click="portfolio.del=true" round>삭제</n-button>
              </div>

              <!-- 차트 보기/닫기 버튼 -->
              <div class="text-right col-6">
                <n-button type="primary" v-if="!portfolio.testClicked && !loading" @click="test(portfolio)" round>차트 보기</n-button>
                <n-button type="primary" v-if="portfolio.testClicked" @click="closeChart(portfolio)" round>차트 닫기</n-button>
              </div>
            </div>

            <!-- 로딩창 -->
            <div v-if="loading" class="text-center">
              <b-spinner variant="secondary" style="width: 3rem; height: 3rem;" label="Large Spinner"></b-spinner>
              <h3>입력값으로 테스트하는 중입니다</h3>
            </div>

          </modal>

          <!-- 포트폴리오 삭제 modal 창 -->
          <modal :show.sync="portfolio.del" headerClasses="justify-content-center" style="color:black">
            <h1 slot="header">#{{portfolio.name}}</h1>
            <h5>정말로 삭제하시겠습니까?</h5>
            <div class="row">
              <div class="col-6 text-left">
                <n-button round @click="delPortfolio(i, portfolio)">삭제</n-button>
              </div>
              <div class="col-6 text-right">
                <n-button type="primary" @click="portfolio.del=false" round>
                  취소
                </n-button>
              </div>
            </div>
          </modal>
        </card>
      </div>  <!-- for문 끝 -->
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import { Button,FormGroupInput, Modal } from '@/components';
import { Card } from "@/components/index";
import LineChart from '@/components/Charts/LineChart.vue';
import { BSpinner } from 'bootstrap-vue';
import test from "@/utils/test";

export default {
  name: 'portfolio',
  bodyClass: 'portfolio-page',
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
      loading: false,
      testClicked: false,
    }
  },
  computed: {
    ...mapState("user", ["userInfo"]),
  },
  created() {
  },
  methods: {
    ...mapActions("stock", ["getTestData"]),
    ...mapActions("user", ["getUserInfo", "deletePortfolio"]),

    // 테스트
    async test(data) {

      data.testClicked = false;
      this.loading = true;

      // 테스트 데이터 get
      const result = await this.getTestData(data);

      // 데이터 전처리
      const preocessed_data = test.preprocess(result);
      data.portfolio1_data = preocessed_data[0];
      data.portfolio2_data = preocessed_data[1];
      data.portfolio3_data = preocessed_data[2];

      this.loading = false;
      data.testClicked = true;
    },
    // 포트폴리오 삭제
    async delPortfolio(i, portfolio) {
      await this.deletePortfolio(portfolio.id);
      await this.getUserInfo();
    },
    // 재분배 주기 문자열 리턴
    rebalncingValue(r) {
      if(r == -1) {
        return "재분배하지 않음";
      }
      else if(r == 12) {
        return "1년";
      }
      else if(r == 6) {
        return "6개월";
      }
      else {
        return "3개월";
      }
    },
    // 차트 닫기
    closeChart(portfolio) {
      portfolio.testClicked = false;
      portfolio.portfolio1_data = null;
      portfolio.portfolio2_data = null;
      portfolio.portfolio3_data = null;
    }
  },
};
</script>
<style></style>
