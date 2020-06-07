<template>
    <apexchart type="area" height="350" :options="options" :series="series"></apexchart>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'

export default {
  name: 'line-chart',
  bodyClass: 'line-chart',
  components: {
    apexchart: VueApexCharts,
  },
  props: {
	  portfolio1_data: { type: Array },
	  portfolio2_data: { type: Array },
	  portfolio3_data: { type: Array },
  },
  data() {
    return {
          series: [
            {
              name: "#1",
              data: this.portfolio1_data
            },
            {
              name: "#2",
              data: this.portfolio2_data
            },
            {
              name: "#3",
              data: this.portfolio3_data
            },
          ],
          options: {
            chart: {
              type: 'area',
              stacked: false,
              height: 350,
              zoom: {
                type: 'x',
                enabled: true,
                autoScaleYaxis: true
              },
              toolbar: {
                autoSelected: 'zoom'
              }
            },
            dataLabels: {
              enabled: false
            },
            markers: {
              size: 0,
            },
            title: {
              text: '자산 변화',
              align: 'left'
            },
            fill: {
              type: 'gradient',
              gradient: {
                shadeIntensity: 1,
                inverseColors: false,
                opacityFrom: 0.5,
                opacityTo: 0,
                stops: [0, 90, 100]
              },
            },
            yaxis: {
              labels: {
                formatter: function (val) {
                  return (val / 10000).toFixed(0);
                },
              },
              title: {
                text: '자산(만원)'
              },
            },
            xaxis: {
              type: 'datetime',
            },
            tooltip: {
              shared: false,
              y: {
                formatter: function (val) {
                  return (val / 1000).toFixed(0);
                }
              }
            }
          },
          
    }
  },
};
</script>
<style></style>
