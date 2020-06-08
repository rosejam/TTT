<template>
  <div class="row">
    <div class="col-2">
      시작 금액: 
    </div>
    <div class="col-3 text-left">
      [{{data[0][1] | currency}}원]
    </div>
    <div class="col-2">
      종료 금액: 
    </div>
    <div class="col-5 text-left">
      [{{data[data.length-1][1] | currency}}원]<br/>
      <div v-html="html"></div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'up-down',
  bodyClass: 'up-down',
  props: {
    data: { type: Array },
  },
  data() {
    return {
    }
  },
  computed: {
    html() {
      return this.upDown();
    }
  },
  methods: {
    // 자산 변화 비율
    upDown() {
      const startPrice = this.data[0][1];
      const endPrice = this.data[this.data.length-1][1];
      const ratio = ((endPrice - startPrice) / startPrice * 100).toFixed(4);

      let prefix = '+';
      let updown;
      if(ratio > 0) updown = '▲';
      else if(ratio < 0) {
        prefix = '';
        updown = '▼';
      }
      else updown = '';

      let span = "<span>";
      if(ratio > 0) {
        span = "<span style='color: red'>"
      }
      else if(ratio < 0) {
        span = "<span style='color: blue'>"
      }

      const html = span + "(" + prefix + ratio + "%" + updown + ")</span>";

      return html;
    },


  },

  filters: {
    // 숫자 3자리마다 , 찍기
    currency: value => {
      let num = Number(value);
      if (!num) return '';
      return num.toFixed(0).replace(/(\d)(?=(\d{3})+(?:\.\d+)?$)/g, "$1,");
    } 
  },
};

</script>
<style></style>
