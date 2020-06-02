<template>
  <div class="content">
    <div class="row" style="margin:auto">
      <div class="col-md-6">
        <card>
          <div class="row">
            <div class="col-md-2">
            </div>
            <div class="col-md-8">
              <h3>테스트 결과</h3>
            </div>
            <div class="col-md-2">
                <img src="img/chart_line_color.png" alt="">
            </div>
          </div>
          <div class="chart" ref="chart"></div>
        </card>
      </div>
    </div>
  </div>
</template>
<script>
import { Card } from "@/components/index";
import * as LightweightCharts from 'lightweight-charts';

export default {
  name: 'chart',
  bodyClass: 'chart-body',
  components: {
	Card,
    LightweightCharts
  },
  props: {
	  portfolio1_data: { type: Array },
	  portfolio2_data: { type: Array },
	  portfolio3_data: { type: Array },
  },
  data() {
    return {
      chart: null,
    }
  },
  mounted() {
    var chart = LightweightCharts.createChart(this.$refs.chart, {
      // width: 600,
      // height: 300,
      priceScale: {
        mode: 1,
      },
      timeScale: {
        borderColor: 'rgba(197, 203, 206, 0.4)',
      },
      layout: {
        backgroundColor: '#100841',
        textColor: '#ffffff',
      },
      grid: {
        vertLines: {
          color: 'rgba(197, 203, 206, 0.4)',
          style: LightweightCharts.LineStyle.Dotted,
        },
        horzLines: {
          color: 'rgba(197, 203, 206, 0.4)',
          style: LightweightCharts.LineStyle.Dotted,
        },
      },
    });

    var porfolio1_series = chart.addAreaSeries({
      topColor: 'rgba(67, 83, 254, 0.7)',
      bottomColor: 'rgba(67, 83, 254, 0.3)',
      lineColor: 'rgba(67, 83, 254, 1)',
      lineWidth: 2,
    });

    var porfolio2_series = chart.addAreaSeries({
      topColor: 'rgba(255, 192, 0, 0.7)',
      bottomColor: 'rgba(255, 192, 0, 0.3)',
      lineColor: 'rgba(255, 192, 0, 1)',
      lineWidth: 2,
	  });
	
	  var porfolio3_series = chart.addAreaSeries({
      topColor: 'rgba(255, 192, 0, 0.7)',
      bottomColor: 'rgba(255, 192, 0, 0.3)',
      lineColor: 'rgba(255, 192, 0, 1)',
      lineWidth: 2,
	  });
	
    porfolio1_series.setData(this.portfolio1_data);
    porfolio2_series.setData(this.portfolio2_data);
    porfolio3_series.setData(this.portfolio3_data);
  },
};
</script>
<style>
  .chart {
    height: 500px;
    width: 100%;
  }
</style>
