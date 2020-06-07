<template>
  <div>
    <strong>{{title}}</strong>
    <apexchart type="donut" height="350" :options="options" :series="series"></apexchart>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'

export default {
  name: 'donut-chart',
  bodyClass: 'donut-chart',
  components: {
    apexchart: VueApexCharts,
  },
  props: {
    title: { type: String },
    donut_chart_labels: { type: Array },
    donut_chart_series: { type: Array },
  },
  data() {
    return {
      options: {
        labels: this.donut_chart_labels,
          plotOptions: {
            pie: {
                customScale: 0.7,
                donut: {
                  labels: {
                      show: true,
                  },
                  size: '50%'
                }
            }
        }
      },
      series: this.donut_chart_series,
    }
  },
  mounted() {
    for (let i = 0; i < this.donut_chart_series.length; i++) {
      if(this.donut_chart_series[i] == 0) {
        this.donut_chart_series.splice(i, 1);
        this.donut_chart_labels.splice(i--, 1);
      }
    }
  },
};
</script>
<style></style>
