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
          <h1 class="title">자산 현황</h1>
        </div>
      </div>
    </div>
    <div class="section">
      <div class="container">
        <h3 class="title">About me</h3>
        <h5 class="description">
          An artist of considerable range, Ryan — the name taken by
          Melbourne-raised, Brooklyn-based Nick Murphy — writes, performs and
          records all of his own music, giving it a warm, intimate feel with a
          solid groove structure. An artist of considerable range.
        </h5>
        <div>
          <n-button :type="tabs.summary ? 'primary' : 'neutral'" outline round @click="clickTab('summary')">
            <i class="fa fa-chart-line"></i> 전체 현황
          </n-button>
          <n-button :type="tabs.stock ? 'primary' : 'neutral'" outline round @click="clickTab('stock')">
            <i class="fa fa-chart-pie"></i> 보유 주식
          </n-button>
          <n-button :type="tabs.predict ? 'primary' : 'neutral'" outline round @click="clickTab('predict')">
            <i class="fa fa-dollar-sign"></i> 예상 수익
          </n-button>
          <!-- 전체 현황 -->
          <div class="summary" v-if="tabs.summary">
            <div class="row">
                <div class="col-12">
                    <card>
                    <template slot="header">
                    <div class="row">
                        <div class="col-sm-6 text-left">
                            <h5 class="card-category">자산</h5>
                            <h2 class="card-title">자산 변화 추이</h2>
                        </div>
                        <div class="col-sm-6">
                        <div class="btn-group btn-group-toggle float-right"
                            data-toggle="buttons">
                            <template>
                                <label v-for="(option, index) in bigLineChartCategories"
                                        :key="option"
                                        class="btn btn-success btn-sm btn-simple"
                                        :class="{active:bigLineChart.activeIndex === index}"
                                        :id="index">
                                    <input type="radio"
                                        @click="initBigChart(index)"
                                        name="options" autocomplete="off"
                                        :checked="bigLineChart.activeIndex === index">
                                    {{ option }}
                                </label>
                            </template>
                        </div>
                        </div>
                    </div>
                    </template>
                        <line-chart
                                    class="chart-area"
                                    ref="bigChart"
                                    chart-id="big-line-chart"
                                    :chart-data="bigLineChart.chartData"
                                    :gradient-colors="bigLineChart.gradientColors"
                                    :gradient-stops="bigLineChart.gradientStops"
                                    :extra-options="bigLineChart.extraOptions">
                        </line-chart>
                    </card>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-6">
                    <card class="chart">
                      <h5 class="card-category">2019년 6월 ~ 2020년 5월</h5>
                      <h3 class="card-title">월별 수익</h3>
                      <bar-chart
                              class="chart-area"
                              chart-id="blue-bar-chart"
                              :chart-data="blueBarChart.chartData"
                              :gradient-stops="blueBarChart.gradientStops"
                              :extra-options="blueBarChart.extraOptions">
                      </bar-chart>
                    </card>
                </div>
                <div class="col-lg-6">
                    <card class="chart">
                      <h5 class="card-category">2019년 6월 ~ 2020년 5월</h5>
                      <h3 class="card-title"><i class="tim-icons icon-send text-success "></i>자산 변화 추이</h3>
                      <line-chart style="height: 100%"
                                  :chart-data="purpleLineChart.chartData"
                                  :gradient-color="purpleLineChart.gradientColors"
                                  :gradient-stops="purpleLineChart.gradientStops"
                                  :extra-options="purpleLineChart.extraOptions">
                      </line-chart>
                    </card>
                </div>
            </div>
          </div>
          <!-- 보유 주식 -->
          <div class="stock" v-if="tabs.stock">
            <div class="col-12">
              <card>
                <template slot="header">
                  <h4 class="card-title">보유 주식</h4>
                </template>
                <div class="table-responsive text-left">
                  <base-table :data="table.data"
                              :columns="table.columns"
                              thead-classes="text-primary">
                  </base-table>
                </div>
              </card>
            </div>
            <div class="row">
            </div>
          </div>
          <!-- 예상 수익 -->
        <div class="predict" v-if="tabs.predict">
            <card class="chart">
            <h5 class="card-category">completedTasks</h5>
            <h3 class="card-title"><i class="tim-icons icon-send text-success "></i> 12,100K</h3>
            <line-chart
                    class="chart-area"
                    chart-id="purple-line-chart"
                    :chart-data="purpleLineChart2.chartData"
                    :gradient-stops="purpleLineChart2.gradientStops"
                    :extra-options="purpleLineChart2.extraOptions">
            </line-chart>
            </card>
        </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { Button } from '@/components';
import { Card } from "@/components/index";
import LineChart from '@/components/Charts/LineChart.js'
import BarChart from '@/components/Charts/BarChart.js'
import * as chartConfigs from '@/components/Charts/config';
import config from '@/config';
import BaseTable from "@/components/BaseTable";

// 보유 주식 테이블 더미 데이터
const tableColumns = ["종목", "보유수량", "금액"];
const tableData = [
  {
    id: 1,
    종목: "SK하이닉스",
    보유수량: "46",
    금액: "10000000"
  },
  {
    id: 2,
    종목: "삼성전자",
    보유수량: "36",
    금액: "34000000"
  },
  {
    id: 3,
    종목: "현대자동차",
    보유수량: "33",
    금액: "26000000"
  },
  {
    id: 4,
    종목: "멀티캠퍼스",
    보유수량: "68",
    금액: "30000000"
  },
  {
    id: 5,
    종목: "현대모비스",
    보유수량: "32",
    금액: "33000000"
  },
  {
    id: 6,
    종목: 'SK텔레콤',
    보유수량: '11',
    금액: "4000000"
  },
  {
    id: 7,
    종목: '삼성SDS',
    보유수량: '23',
    금액: "12000000"
  }
];

export default {
  name: 'profile',
  bodyClass: 'profile-page',
  components: {
    [Button.name]:Button,
    Card,
    LineChart,
    BarChart,
    BaseTable,
  },
  data () {
      return {
        tabs: {
          summary: true,
          stock: false,
          predict: false
        },
        blueBarChart: {
            extraOptions: chartConfigs.barChartOptions,
            chartData: {
            labels: ['USA', 'GER', 'AUS', 'UK', 'RO', 'BR'],
            datasets: [{
                label: "Countries",
                fill: true,
                borderColor: config.colors.info,
                borderWidth: 2,
                borderDash: [],
                borderDashOffset: 0.0,
                data: [53, 20, 10, 80, 100, 45],
            }]
            },
            gradientColors: config.colors.primaryGradient,
            gradientStops: [1, 0.4, 0],
        },
        purpleLineChart: {
            extraOptions: chartConfigs.purpleChartOptions,
            chartData: {
            labels: ['JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
            datasets: [{
                label: "Data",
                fill: true,
                borderColor: '#d048b6',
                borderWidth: 2,
                borderDash: [],
                borderDashOffset: 0.0,
                pointBackgroundColor: '#d048b6',
                pointBorderColor: 'rgba(255,255,255,0)',
                pointHoverBackgroundColor: '#d048b6',
                pointBorderWidth: 20,
                pointHoverRadius: 4,
                pointHoverBorderWidth: 15,
                pointRadius: 4,
                data: [80, 100, 70, 80, 120, 80],
            }]
            }
        },
        purpleLineChart2: {
            extraOptions: chartConfigs.purpleChartOptions,
            chartData: {
            labels: ['JUL', 'AUG', 'SEP', 'OCT', 'NOV'],
            datasets: [{
                label: "My First dataset",
                fill: true,
                borderColor: config.colors.danger,
                borderWidth: 2,
                borderDash: [],
                borderDashOffset: 0.0,
                pointBackgroundColor: config.colors.danger,
                pointBorderColor: 'rgba(255,255,255,0)',
                pointHoverBackgroundColor: config.colors.danger,
                pointBorderWidth: 20,
                pointHoverRadius: 4,
                pointHoverBorderWidth: 15,
                pointRadius: 4,
                data: [90, 27, 60, 12, 80],
            }]
            },
            gradientColors: ['rgba(66,134,121,0.15)', 'rgba(66,134,121,0.0)', 'rgba(66,134,121,0)'],
            gradientStops: [1, 0.4, 0],
        },
        bigLineChartCategories:[
            "총 보유 자산",
            "보유 현금",
            "보유 주식"
        ],
        bigLineChart: {
            allData: [
            [45000, 47500, 46500, 43000, 44600, 48000, 49500, 48500, 50000, 52500, 57000, 55500],
            [12000, 10500, 13500, 13000, 10000, 15000, 13000, 18500, 12000, 14500, 17000, 13500],
            [33000, 37000, 33000, 30000, 30600, 33000, 36500, 30000, 38000, 38000, 40000, 42000]
            ],
            activeIndex: 0,
            chartData: { datasets: [{ }]},
            extraOptions: chartConfigs.purpleChartOptions,
            gradientColors: config.colors.primaryGradient,
            gradientStops: [1, 0.4, 0],
            categories: []
        },
        table: {
        title: "Simple Table",
        columns: [...tableColumns],
        data: [...tableData]
      },
      }
  },
  methods: {
    clickTab(c) {
      switch (c) {
        case "summary":
          this.tabs.summary = true;
          this.tabs.stock = false;
          this.tabs.predict = false;
          break;
        case "stock":
          this.tabs.summary = false;
          this.tabs.stock = true;
          this.tabs.predict = false;
          break;
        case "predict":
          this.tabs.summary = false;
          this.tabs.stock = false;
          this.tabs.predict = true;
          break;
        default:
          break;
      }
    },
    initBigChart(index) {
      let chartData = {
        datasets: [{
          fill: true,
          borderColor: config.colors.primary,
          borderWidth: 2,
          borderDash: [],
          borderDashOffset: 0.0,
          pointBackgroundColor: config.colors.primary,
          pointBorderColor: 'rgba(255,255,255,0)',
          pointHoverBackgroundColor: config.colors.primary,
          pointBorderWidth: 20,
          pointHoverRadius: 4,
          pointHoverBorderWidth: 15,
          pointRadius: 4,
          data: this.bigLineChart.allData[index]
        }],
        labels: ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
      }
      this.$refs.bigChart.updateGradients(chartData);
      this.bigLineChart.chartData = chartData;
      this.bigLineChart.activeIndex = index;
    },
  },
  mounted(){
    this.initBigChart(0);
  },
};
</script>
<style></style>
