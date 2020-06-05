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
      <div class="col-md-4">
        <card>
          기간: 2008년 11월 ~ 2013년 10월<br/>
          초기금액: 100000원<br/>
          재분배 주기: 6개월<br/>
          #1: 삼성전자(30%) LG전자(40%) 현대자동차(30%)<br/>
          #2: 쿠팡(15%) 11번가(25%) SK텔레콤(40%) 대우증권(20%)
          <n-button @click.native="modals.save = true">차트 보기</n-button>
          <modal :show.sync="modals.save" headerClasses="justify-content-center" style="color:black" modal-classes="modal-lg">
            <h4 slot="header" class="title title-up">포트폴리오 차트</h4>
            차트<br/>
            차트<br/>
            차트<br/>
          </modal>
        </card>
      </div>
      <div class="col-md-4">
        <card>
          기간: 2008년 11월 ~ 2013년 10월<br/>
          초기금액: 100000원<br/>
          재분배 주기: 6개월<br/>
          #1: 삼성전자(30%) LG전자(40%) 현대자동차(30%)<br/>
          #2: 쿠팡(15%) 11번가(25%) SK텔레콤(40%) 대우증권(20%)
          <n-button>차트 보기</n-button>
        </card>
      </div>
      <div class="col-md-4">
        <card>
          기간: 2008년 11월 ~ 2013년 10월<br/>
          초기금액: 100000원<br/>
          재분배 주기: 6개월<br/>
          #1: 삼성전자(30%) LG전자(40%) 현대자동차(30%)<br/>
          #2: 쿠팡(15%) 11번가(25%) SK텔레콤(40%) 대우증권(20%)
          <n-button>차트 보기</n-button>
        </card>
      </div>
      <div class="col-md-4">
        <card>
          기간: 2008년 11월 ~ 2013년 10월<br/>
          초기금액: 100000원<br/>
          재분배 주기: 6개월<br/>
          #1: 삼성전자(30%) LG전자(40%) 현대자동차(30%)<br/>
          #2: 쿠팡(15%) 11번가(25%) SK텔레콤(40%) 대우증권(20%)
          <n-button>차트 보기</n-button>
        </card>
      </div>
    </div>
  </div>
</template>
<script>
import { Button,FormGroupInput, Modal } from '@/components';
import { Card } from "@/components/index";

export default {
  name: 'portfolio',
  bodyClass: 'portfolio-page',
  components: {
    [Button.name]:Button,
    [FormGroupInput.name]: FormGroupInput,
    Modal,
    Card,
  },
  data() {
    return {
      modals: {
        save: false
      },
    }
  },
};
</script>
<style></style>
