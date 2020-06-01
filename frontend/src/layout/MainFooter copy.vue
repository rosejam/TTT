<template>
  <footer
    class="footer"
    :class="{ [`footer-${type}`]: type }"
    :data-background-color="backgroundColor"
  >
    <div class="container">
      <nav>
        <ul>
          <li>
            <n-button type="neutral" @click.native="modals.desc = true" link>
              TTT가 뭐야?
            </n-button>
            <modal
              :show.sync="modals.desc"
              class="modal"
              headerClasses="justify-content-center"
              style="color:black"
            >
              <h4 slot="header" class="title title-up modal">TTT?</h4>
              <p>
                1. <b>Tiny Testing Tool</b>의 줄임말입니다. <br/>
                2. 또한 <b>Trust, Trend, Tactic</b> 의 <b>3T</b>를 가치로 삼고 있습니다. <br/>
              </p>
            </modal>
          </li>
          <li>
            <n-button type="neutral" @click.native="modals.team = true" link>
              Team ROA
            </n-button>
            <modal
              :show.sync="modals.team"
              class="modal"
              headerClasses="justify-content-center"
              style="color:black"
            >
              <h4 slot="header" class="title title-up">Team ROA</h4>
              <p>
                <b>ROA</b> 로보어드바이저(Robot Adviser)의 준말<br/>
              </p>
            </modal>
          </li>
          <li>
            <n-button type="neutral" @click.native="modals.contact = true" link>
              TTT가 뭐야?
            </n-button>
            <modal
              :show.sync="modals.contact"
              class="modal"
              headerClasses="justify-content-center"
              style="color:black"
            >
              <h4 slot="header" class="title title-up">TTT?</h4>
              <p>
                1. Tiny Testing Tool의 줄임말입니다. <br/>
                2. 또한 Trust, Trend, Tactic 의 3T를 가치로 삼고 있습니다. <br/>
              </p>
            </modal>
          </li>
        </ul>
      </nav>
      <div class="copyright">
        &copy; {{ year }}, Created By ROA
      </div>
    </div>
  </footer>
</template>
<script>
import { Button, Modal } from '@/components';

export default {
  components: {
    [Button.name]: Button,
    Modal,
  },
  props: {
    backgroundColor: String,
    type: String
  },
  data() {
    return {
      year: new Date().getFullYear(),
      modals: {
        desc: false,
        team: false,
        contact: false
      },
    };
  }
};
</script>
<style></style>
