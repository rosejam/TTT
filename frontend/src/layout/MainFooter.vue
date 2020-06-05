<template>
  <footer
    class="footer"
    :class="{ [`footer-${type}`]: type }"
    :data-background-color="backgroundColor"
  >
    <div class="container">
      <nav>
        <ul>
          <!-- TTT 서비스 소개 -->
          <li>
            <div v-popover:info>
            <n-button type="neutral" link>TTT가 뭐야?</n-button>
            </div>
            <el-popover
              ref="info"
              popper-class="popover"
              placement="bottom"
              width="200"
              trigger="hover"
            >
              <div class="popover-body">
                <h4>TTT?</h4>
                1. <b>Tiny Testing Tool</b>의 줄임말로, 저희 서비스를 일컫는 말입니다. <br/><br/>
                2. 또한 <b>Trust, Trend, Tactic</b> 의 <b>3T</b>를 가치로 삼고 있습니다. <br/>
              </div>
            </el-popover>
          </li>

          <!-- ROA 팀 소개 -->
          <li>
            <div v-popover:team>
            <n-button type="neutral" link>Team ROA</n-button>
            </div>
            <el-popover
              ref="team"
              popper-class="popover"
              placement="bottom"
              width="200"
              trigger="hover"
            >
              <div class="popover-body">
                <h4>ROA</h4>
                <b>서비스 개발 및 운영팀</b>의 이름으로, 로보어드바이저(Robot Adviser)의 준말입니다.<br/>
              </div>
            </el-popover>
          </li>

          <!-- 문의 -->
          <li>
            <div v-popover:contact>
            <n-button type="neutral" link>Contact us</n-button>
            </div>
            <el-popover
              ref="contact"
              popper-class="popover"
              placement="bottom"
              width="200"
              trigger="hover"
            >
              <div class="popover-body">
                <h4>Contact us</h4>
                문의사항은 <a href="mailto:ddason.inc@gmail.com">ddason.inc@gmail.com</a> 으로 문의주세요.
              </div>
            </el-popover>
          </li>

          <li>
            <n-button type="neutral" link @click="$router.push('/term')">서비스 이용약관</n-button>
          </li>

        </ul>
      </nav>
      <div class="copyright">
        <n-button type="neutral" link disabled>
          &copy; {{ year }}, Created By ROA
        </n-button>
      </div>
    </div>
  </footer>
</template>
<script>
import { Button } from '@/components';
import { Popover } from 'element-ui';

export default {
  components: {
    [Button.name]: Button,
    [Popover.name]: Popover,
  },
  props: {
    backgroundColor: String,
    type: String
  },
  data() {
    return {
      year: new Date().getFullYear(),
    };
  }
};
</script>
<style></style>
