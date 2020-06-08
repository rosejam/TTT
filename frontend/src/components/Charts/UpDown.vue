<template>
  <div class="table-container">
    <br/>
    <table class="table">

      <!-- 테이블 column 이름 -->
      <thead>
        <tr>
          <td><strong>구분</strong></td>
          <td><strong>금액</strong></td>
          <td><strong>날짜</strong></td>
        </tr>
      </thead>

      <!-- 테이블 내용 -->
      <tbody>

        <tr>
          <td>시작 금액</td>
          <td>{{data[0][1] | currency}} 원</td>
          <td>{{highAndLow.startDay}}</td>
        </tr>

        <tr>
          <td>최고 금액</td>
          <td>
            {{highAndLow.highAmount | currency}} 원
            <div v-html="html.high"></div>
          </td>
          <td>{{highAndLow.highDay}}</td>
        </tr>

        <tr>
          <td>최저 금액</td>
          <td>
            {{highAndLow.lowAmount | currency}} 원
            <div v-html="html.low"></div>
          </td>
          <td>{{highAndLow.lowDay}}</td>
        </tr>

        <tr>
          <td>종료 금액</td>
          <td>
            {{data[data.length-1][1] | currency}} 원
            <div v-html="html.end"></div>
          </td>
          <td>{{highAndLow.endDay}}</td>
        </tr>

      </tbody>
    </table>
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
    },
    highAndLow() {
      return this.calcHL();
    },
  },
  methods: {

    // 자산 변화 비율
    upDown() {
      const end = this.calcUpDown(this.data[this.data.length-1][1]);
      const high = this.calcUpDown(this.highAndLow.highAmount);
      const low = this.calcUpDown(this.highAndLow.lowAmount);

      return {
        end: end,
        high: high,
        low: low
      };
    },

    calcUpDown(endPrice) {
      const startPrice = this.data[0][1];
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

    // 최고가, 최저가 계산
    calcHL() {

      let highDay, highAmount = 0, lowDay, lowAmount = Number.MAX_VALUE;

      for (let i = 0; i < this.data.length; i++) {
        const amount = this.data[i][1];

        if(amount > highAmount) {
          highAmount = amount;
          highDay = this.data[i][0];
        }

        if(amount < lowAmount) {
          lowAmount = amount;
          lowDay = this.data[i][0];
        }

      }

      // 최고 금액 날짜
      let date = new Date(highDay);
      highDay = this.getDay(date);

      // 최저 금액 날짜
      date = new Date(lowDay);
      lowDay = this.getDay(date);

      // 시작 금액 날짜
      date = new Date(this.data[0][0]);
      const startDay = this.getDay(date);

      // 종료 금액 날짜
      date = new Date(this.data[this.data.length-1][0]);
      const endDay = this.getDay(date);

      return {
        highDay: highDay,
        highAmount: highAmount,
        lowDay: lowDay,
        lowAmount: lowAmount,
        startDay: startDay,
        endDay: endDay,
      };

    },
    
    getDay(date) {
      let year = date.getFullYear();
      let month = date.getMonth() + 1;
      let day = date.getDate();
      if(month < 10) month = "0" + month;
      if(day < 10) day = "0" + day;
      return year + "-" + month + "-" + day;
    }
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
