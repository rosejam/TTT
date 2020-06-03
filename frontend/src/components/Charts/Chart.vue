<template>
  <div class="content">
    <div class="row" style="margin:auto">
      <div class="col-md-2"></div>
      <div class="col-md-9">
          <div class="row">
            <div class="col-md-10"></div>
            <div class="col-md-2">
                <img src="img/chart_line_color.png" alt="">
            </div>
          </div>
          <br/>
          <div class="chart" ref="chart"></div>
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
        backgroundColor: '#EEEEEE',
        textColor: '#000000',
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
      lineColor: 'rgba(67, 83, 254, 1)',
      lineWidth: 2,
    });

    var porfolio2_series = chart.addAreaSeries({
      lineColor: 'rgba(255, 192, 0, 1)',
      lineWidth: 2,
	  });
	
	  var porfolio3_series = chart.addAreaSeries({
      lineColor: 'rgba(255, 33, 102, 1)',
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
