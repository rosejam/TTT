<template>
    <apexchart type="area" height="350" :options="chartOptions" :series="series"></apexchart>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'

export default {
  name: 'chart',
  bodyClass: 'chart',
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
            //   data: [[1324508400000, 14], [1324594800000, 23] , [1326236400000, 18]]
            },
          ],
          chartOptions: {
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
              text: '자산 변화 추이',
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
                  return val.toFixed(0);
                },
              },
              title: {
                text: 'Price'
              },
            },
            xaxis: {
              type: 'datetime',
            },
            tooltip: {
              shared: false,
              y: {
                formatter: function (val) {
                  return val.toFixed(0);
                }
              }
            }
          },
          
    }
  },
};
</script>
<style></style>
