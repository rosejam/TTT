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
          <h1 class="title">증권 정보</h1>
        </div>
      </div>
    </div>
    <div class="section text-center">
      <div class="container">
        <h3>
          다양한 <b>증권 정보</b>를 검색해보세요!
        </h3>
      </div>
    </div>

    <!-- 더미 테이블 -->
    <b-container fluid>
      <!-- User Interface controls -->
      <b-row>

        <b-col lg="6" class="my-1">
          <b-form-group
            label="검색"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="filterInput"
            class="mb-0"
          >
            <b-input-group size="sm">
              <fg-input
                v-model="filter"
                type="search"
                id="filterInput"
                placeholder="종목코드·종목명 입력"
              ></fg-input>
              <!-- 종목명·지수명·펀드명·환율명·원자재명 입력 -->
                <n-button :disabled="!filter" @click="filter = ''" icon round size="sm">
                  <i class="now-ui-icons ui-1_simple-remove"></i>
                </n-button>
            </b-input-group>
          </b-form-group>
        </b-col>

        <b-col lg="6" class="my-1">
          <b-form-group
            label="검색 필터링"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            description=""
            class="mb-0">
            <b-form-checkbox-group v-model="filterOn" class="mt-1">
              <b-form-checkbox value="code">종목코드</b-form-checkbox>
              <b-form-checkbox value="name">종목명</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>
        </b-col>

        <b-col sm="5" md="6" class="my-1">
          <b-form-group
            label="페이지당 개수"
            label-cols-sm="6"
            label-cols-md="4"
            label-cols-lg="3"
            label-align-sm="right"
            label-size="sm"
            label-for="perPageSelect"
            class="mb-0"
          >
            <b-form-select
              v-model="perPage"
              id="perPageSelect"
              size="sm"
              :options="pageOptions"
            ></b-form-select>
          </b-form-group>
        </b-col>

        <b-col sm="7" md="6" class="my-1">
          <b-pagination
            v-model="currentPage"
            :total-rows="totalRows"
            :per-page="perPage"
            align="fill"
            size="sm"
            class="my-0"
          ></b-pagination>
        </b-col>
      </b-row>

      <!-- Main table element -->
      <b-table
        show-empty
        small
        stacked="md"
        :items="items"
        :fields="fields"
        :current-page="currentPage"
        :per-page="perPage"
        :filter="filter"
        :filterIncludedFields="filterOn"
        :sort-by.sync="sortBy"
        :sort-desc.sync="sortDesc"
        :sort-direction="sortDirection"
        @filtered="onFiltered"
      >
        <template v-slot:cell(name)="row">
            <!-- {{row.item.code}} -->
          <a href="/stockdetail">
            {{row.value}}
          </a>
        </template>

        <template v-slot:row-details="row">
          <b-card>
            <ul>
              <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
            </ul>
          </b-card>
        </template>
      </b-table>

    </b-container>
  </div>
</template>
<script>
import { Card } from "@/components/index";
import { Button, DropDown, Tabs, TabPane, FormGroupInput, Switch, Modal } from '@/components';
import { Popover } from 'element-ui';
import BaseTable from "@/components/BaseTable";

export default {
  name: 'profile',
  bodyClass: 'profile-page',
  components: {
    [Button.name]:Button,
    DropDown,
    Tabs,
    TabPane,
    [FormGroupInput.name]: FormGroupInput,
    [Switch.name]: Switch,
    [Popover.name]: Popover,
    Modal,
    Card,
    BaseTable
  },
  data() {
    return {
      ss: false,
      modals: {
        save: false
      },
      switches: {
        defaultOn: true,
        defaultOff: false
      },
      items: [
        { code: '005930', name: '삼성전자', price: '48,800', offer: '48,900', bid: '48,850', volume: '11,227,615', value: '552,427'},
        { code: '005935', name: '삼성전자우', price: '42,400', offer: '42,500', bid: '42,450', volume: '984,540', value: '42,048'},
        { code: '006400', name: '삼성SDI', price: '333,000', offer: '332,000', bid: '331,500', volume: '406,680', value: '136,028'},
        { code: '018260', name: '삼성에스디에스', price: '174,500', offer: '174,000', bid: '173,500', volume: '137,010', value: '23,909'},
        { code: '029780', name: '삼성카드', price: '29,400', offer: '29,350', bid: '29,300', volume: '119,572', value: '3,522'},
        { code: '028260', name: '삼성물산', price: '98,400', offer: '98,500', bid: '98,400', volume: '386,163	', value: '38,489'},
        { code: '032830', name: '삼성생명', price: '44,700', offer: '44,650	', bid: '44,600', volume: '431,908', value: '19,479'},
        { code: '307950', name: '현대오토에버', price: '41,150', offer: '41,000', bid: '40,950', volume: '54,519', value: '2,249'},
        { code: '012330', name: '현대모비스', price: '183,000', offer: '183,500', bid: '183,000', volume: '215,272', value: '39,848'},
        { code: '057050', name: '현대홈쇼핑', price: '67,500', offer: '67,200', bid: '67,100', volume: '27,079', value: '1,842'},
        { code: '005380', name: '현대차', price: '94,200', offer: '94,200', bid: '94,100', volume: '1,472,962', value: '140,507'},
        { code: '069960', name: '현대백화점', price: '66,400', offer: '66,300', bid: '66,200	', volume: '83,184', value: '5,579'},
        { code: '001450', name: '현대해상', price: '24,300', offer: '24,300', bid: '24,250', volume: '216,105', value: '5,286'},
        { code: '000720', name: '현대건설', price: '32,400', offer: '32,150', bid: '32,100', volume: '506,538', value: '16,456'},
        { code: '096770', name: 'SK이노베이션', price: '102,500', offer: '103,000', bid: '102,500', volume: '625,656', value: '64,856'},
        { code: '034730', name: 'SK', price: '227,000', offer: '228,000', bid: '227,500', volume: '397,422', value: '90,611'},
        { code: '017670', name: 'SK텔레콤', price: '208,500', offer: '209,000', bid: '208,500', volume: '200,682', value: '42,155'},
        { code: '001510', name: 'SK증권', price: '625', offer: '625', bid: '624', volume: '4,569,150', value: '2,897'},
        { code: '000660', name: 'SK하이닉스', price: '81,200', offer: '81,200', bid: '81,100', volume: '3,125,431', value: '255,457'},
        { code: '066570', name: 'LG전자', price: '56,100', offer: '56,100', bid: '56,000', volume: '462,461', value: '26,094'},
        { code: '051910', name: 'LG화학', price: '376,000', offer: '375,000', bid: '374,500', volume: '469,520', value: '177,522'},
        { code: '051900', name: 'LG생활건강', price: '1,398,000', offer: '1,398,000', bid: '1,397,000', volume: '21,262', value: '29,914'},
        { code: '034220', name: 'LG디스플레이', price: '10,200', offer: '10,250', bid: '10,200', volume: '2,537,413', value: '26,243'},
        { code: '032640', name: 'LG유플러스', price: '13,150', offer: '13,200', bid: '13,150', volume: '1,798,330', value: '23,859'},
        { code: '003550', name: 'LG', price: '62,500', offer: '62,400', bid: '62,300', volume: '160,189', value: '10,102'},
      ],
      fields: [
        { key: 'code', label: '종목코드', sortable: true, sortDirection: 'desc' },
        { key: 'name', label: '종목명', sortable: true, sortDirection: 'desc' },
        { key: 'price', label: '현재가', sortable: true, class: 'text-center' },
        { key: 'offer', label: '매도호가', sortable: true, class: 'text-center' },
        { key: 'bid', label: '매수호가', sortable: true, class: 'text-center' },
        { key: 'volume', label: '거래량', sortable: true, class: 'text-center' },
        { key: 'value', label: '거래대금', sortable: true, class: 'text-center' },
        { key: 'actions', label: '상세정보' }
      ],
      totalRows: 1,
      currentPage: 1,
      perPage: 10,
      pageOptions: [10, 20, 30, 50, 100],
      sortBy: '',
      sortDesc: false,
      sortDirection: 'asc',
      filter: null,
      filterOn: [],
      infoModal: {
        id: 'info-modal',
        title: '',
        content: ''
      }
    }
  },
  methods: {
    showSamsung() {
      this.ss = true;
    },
    goDetail() {
      this.$router.replace("/stockdetail");
    },
    info(item, index, button) {
      this.infoModal.title = `Row index: ${index}`
      this.infoModal.content = JSON.stringify(item, null, 2)
      this.$root.$emit('bv::show::modal', this.infoModal.id, button)
    },
    resetInfoModal() {
      this.infoModal.title = ''
      this.infoModal.content = ''
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length
      this.currentPage = 1
    }
  },
  computed: {
    sortOptions() {
      // Create an options list from our fields
      return this.fields
        .filter(f => f.sortable)
        .map(f => {
          return { text: f.label, value: f.key }
        })
    }
  },
  mounted() {
    // Set the initial number of items
    this.totalRows = this.items.length
  },
};
</script>
<style></style>
